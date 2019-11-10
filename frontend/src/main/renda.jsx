import React, {Fragment} from 'react'

export default props => {
    if (props.state.renda && !props.state.status) {
        return (
            <div>
                {props.state.renda}
            </div>
        )
    } else {
        return( <b> {props.state.status} </b>)
    }
}