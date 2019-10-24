import React from "react";
import "./parlamentares.css"

export default props => {
    if (props.data) {
        return (
            <div className="parlamentares row">
                <div className="col-sm-6">
                    <b>Deputados Federais</b>
                    { Object.entries(props.data.federais).map( ([key, obj]) =>(
                        <span className="dep-fed">{key} </span>
                    ))}
                </div>
                <div className="col-sm-6">
                    <b>Deputados Estaduais</b>
                    { Object.entries(props.data.estaduais).map( ([key, obj]) =>(
                        <span className="dep-est">{key} </span>
                    ))}
                </div>
                

            </div>
        )
    } else {
        return (<div></div>)
    }
}