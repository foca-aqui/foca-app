import React from "react"
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css'

import Header from "./header"
import Body from "./body"

export default props => (
    <div className="body">
        <Header />
        <Body />
    </div>
)