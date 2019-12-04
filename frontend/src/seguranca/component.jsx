import React, {Component} from "react"
import axios from "axios"

import 'babel-polyfill';

const API_HOST = "http://localhost:8000/api/"

export default class Seguranca extends Component {
    constructor(props) {
        super(props)
        this.state = this.props.state
    }



    render() {
        if (this.props.state.active) {
            return(
                <div className="segurancaContainer">
                    <h1>Segurança</h1>
                </div>
            )
        } else {
            return(
                <div>

                </div>
            )
        }
    }
}