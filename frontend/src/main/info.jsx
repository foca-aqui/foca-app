import React, {Fragment} from 'react'

import "./info.css"

export default props => {
    if (props.ocorrencias) {
        return (
            <Fragment>
                <label>Dados de {props.search} e mais {props.bairros.length} bairros</label>
                <ul className="search-results">
                    { props.ocorrencias.map( ocorrencias => (
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
        return( <ul> </ul>)
    }
}