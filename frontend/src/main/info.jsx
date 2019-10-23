import React, {Fragment} from 'react'

import "./info.css"

export default props => {
    if (props.state.ocorrencias && !props.state.status) {
        return (
            <Fragment>
                <b><i>Dados de {props.state.search} e mais {props.state.bairros.length} bairros</i></b>
                <ul className="search-results">
                    { props.state.ocorrencias.map( ocorrencias => (
                        <Fragment>
                            {Object.keys(ocorrencias).map( (key, value) => (
                                <li> <label className="info-name">{ocorrencias[key]}</label> <label className="info-value">{key}</label> </li>
                            ))}
                        </Fragment>
                    ))}
                </ul>
            </Fragment>
        )
    } else {
        return( <b> {props.state.status} </b>)
    }
}