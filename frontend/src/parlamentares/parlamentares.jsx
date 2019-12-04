import React from "react";
import "./parlamentares.css"

import Parlamentar from "./parlamentar"

export default props => {
    if (props.data) {
        return (
            <div className="parlamentares">
                { Object.entries(props.data.estaduais).map( ([key, obj]) =>(
                    <Parlamentar key={key} nome={key} />
                ))} 
                { Object.entries(props.data.federais).map( ([key, obj]) =>(
                    <Parlamentar key={key} nome={key} />
                ))} 
            </div>
        )
    } else {
        return (<div></div>)
    }
}