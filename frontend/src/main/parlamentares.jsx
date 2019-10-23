import React from "react";

export default props => {
    if (props.data) {
        return (
            <div className="parlamentares row">
                <div className="col-sm-6">
                    { Object.entries(props.data.federais).map( ([key, obj]) =>(
                        <span>{key} </span>
                    ))}
                </div>
                <div className="col-sm-6">
                { Object.entries(props.data.estaduais).map( ([key, obj]) =>(
                        <span>{key} </span>
                    ))}
                </div>
                

            </div>
        )
    } else {
        return (<div></div>)
    }
}