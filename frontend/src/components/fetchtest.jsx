import React, { Component } from 'react';
import * as utils from "../utils/commonFunctions";

class FetchTest extends Component {
    state = {}
    async componentDidMount() {
        var url = utils.current_stats;
        var a = await utils.getCurrentData(url);
        console.log("testng");
        console.log(JSON.stringify(a));
    }
    render() {
        return (
            <h1>hello</h1>
        );
    }
}

export default FetchTest;