import React, { Component } from 'react'
import axios from "axios"
import 'babel-polyfill';
import qs from "qs"

import Info from "./info"
import Parlamentares from "../parlamentares/parlamentares"
import "./main.css"
import Seguranca from '../seguranca/component';

const initialState = {
    active: false,
    bairro: null,
    aisp: null,
    mes: null,
    ano: null,
    to_mes: null,
    to_ano: null
}

const API_HOST = "http://localhost:8000/api/"

export default class Main extends Component {
    constructor(props) {
        super(props)

        this.state = initialState

        this.search = this.search.bind(this)
        this.inputChange = this.inputChange.bind(this)
    }

    inputChange(e) {
        if (e.target.id == "search") {
            this.setState({bairro: e.target.value})
        }
    }

    search(params){
        this.setState({active: true})
        console.log(this.state)
    }

    render() {
        return (
            <div className="main row">
                <div className="search col-sm-5">
                    <div id="pesquisaContainer" className="search-box">
                        <b>Que bairro você quer consultar ?</b><br></br>
                        <div>
                            <input onChange={this.inputChange} type="text" id="search" className="form-control" placeholder="Digite um bairro..."></input>
                            <button onClick={this.search} className="search-btn"><i className="fa fa-arrow-circle-right fa-3" aria-hidden="true"></i></button>
                        </div>
                    </div>
                    <Seguranca state={this.state} />
                </div>
                <div className="middle col-sm-2"></div>
                <div className="panel-right col-sm-5">
                    <Parlamentares data={this.state.parlamentares} />
                </div>
            </div>
        )
    }
}