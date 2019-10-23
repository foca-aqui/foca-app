import React, { Component } from 'react'
import axios from "axios"
import 'babel-polyfill';
import qs from "qs"

import Info from "./info"
import "./body.css"

const initialState = {
    "search": "",
    "ocorrencias": null,
    "bairros": null
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
                url: `${API_HOST}`,
                params: params
            })
            if(response) {
                this.setState({ 
                    ocorrencias: response.data.top_ocorrencias,
                    bairros: response.data.bairros
                })
            }
            
        }
    }

    render() {
        return (
            <div className="main row">
                <div className="search col-sm-5">
                    <b>Que bairro você quer consultar ?</b><br></br>
                    <input onChange={this.inputChange} type="text" id="search" className="form-control" placeholder="Digite um bairro..."></input>
                    <button onClick={this.search} className="search-btn"><i class="fa fa-arrow-circle-right fa-3" aria-hidden="true"></i></button>
                    
                    <Info ocorrencias={this.state.ocorrencias} bairros={this.state.bairros} search={this.state.search}/>
                </div>
                <div className="middle col-sm-2"></div>
                <div className="panel-right col-sm-5"></div>
            </div>
        )
    }
}