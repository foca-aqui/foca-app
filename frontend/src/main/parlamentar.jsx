import React, { Component } from "react"
import axios from "axios"
import 'babel-polyfill';

const API_HOST = "http://localhost:8000/api/"

export default class Parlamentar extends Component {
    constructor(props) {
        super(props)

        this.state = {
            "nome": props.nome
        }

        this.getData = this.getData.bind(this)

        this.getData()
       
    }

    async getData() {
        let response = await axios({
            method: "get",
            url: `${API_HOST}ve/`,
            params: {
                "cmd": "get_parlamentar_details",
                "nome": this.state.nome
            }
        })
        if (response) {
            this.setState(response.data)
        }
    }

    render() {
        return (
            <div className="parlamentar row">
                <div className="col-sm-3">
                    {this.state.img_url ? <img src={this.state.img_url} className="photo" /> : ""}
                </div>
                <div className="col-sm-7">
                    <h1>{this.state.nome}</h1>
                    <h2>{this.state.deputado}</h2>
                    <p>
                        Telefone: {this.state.telefone}<br/>
                        E-mail: {this.state.email}
                    </p>
                </div>
            </div>
        )
    }
}