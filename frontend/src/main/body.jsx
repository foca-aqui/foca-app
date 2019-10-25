import React, { Component } from 'react'
import axios from "axios"
import 'babel-polyfill';
import qs from "qs"

import Info from "./info"
import Parlamentares from "./parlamentares"
import "./body.css"

const initialState = {
    "search": "",
    "ocorrencias": null,
    "bairros": null,
    "status": null
}
const API_HOST = "http://localhost:8000/api/"

export default class Login extends Component {
    constructor(props) {
        super(props)

        this.state = initialState

        this.inputChange = this.inputChange.bind(this)
        this.search = this.search.bind(this)
    }

    inputChange(e) {
        if (e.target.id == "search") {
            this.setState({"search": e.target.value})
        }
    }

    async search() {
        if (this.state.search.length > 2) {
            var params = {
                "cmd": "get_top_ocorrencias_by_bairro",
                "bairro": this.state.search
            }
            let response = await axios({
                method: "get",
                url: `${API_HOST}oc/`,
                params: params
            })
            if(response && !response.data.status) {
                var brs = ""
                for (var i = 0; i < response.data.bairros.length; i++) {
                    brs += response.data.bairros[i] + ","
                }
                let res = await axios({
                    method: "get",
                    url: `${API_HOST}ve/`,
                    params: {
                        "cmd": "get_parlamentares_by_bairros",
                        "bairros": brs
                    }
                })
                if (res) {
                    this.setState({ 
                        ocorrencias: response.data.top_ocorrencias,
                        bairros: response.data.bairros,
                        parlamentares: res.data,
                        status: null
                    })
                }
            } else {
                this.setState({
                    status: "Ainda não há dados sobre este bairro"
                })
            }
            
        }
    }

    render() {
        return (
            <div className="main row">
                <div className="search col-sm-5">
                    <div className="search-box">
                        <b>Que bairro você quer consultar ?</b><br></br>
                        <div>
                            <input onChange={this.inputChange} type="text" id="search" className="form-control" placeholder="Digite um bairro..."></input>
                            <button onClick={this.search} className="search-btn"><i class="fa fa-arrow-circle-right fa-3" aria-hidden="true"></i></button>
                        </div>
                    </div>
                    <Info state={this.state}/>
                </div>
                <div className="middle col-sm-2"></div>
                <div className="panel-right col-sm-5">
                    <Parlamentares data={this.state.parlamentares} />
                </div>
            </div>
        )
    }
}