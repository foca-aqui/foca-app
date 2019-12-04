import React from "react"
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css'

import Header from "./header"
import Main from "./main"

export default props => (
    <div className="body">
        <Header />
        <Main />
    </div>
)