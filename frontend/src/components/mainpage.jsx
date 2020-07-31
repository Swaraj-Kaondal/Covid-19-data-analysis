import React, { Component } from 'react';

import "bootstrap/dist/css/bootstrap.min.css";
import CurrentStats from "./currentStats";
import StateTable from "./stateTable";
import FilterForm from "./filterform";
import Navbar from "react-bootstrap/Navbar";

class MainPage extends Component {
    render() {
        return (
            <div className="main">
                <Navbar bg="dark" variant="dark">
                    <Navbar.Brand><h1>Covid-19 Data Analysis</h1></Navbar.Brand>
                </Navbar>
                <FilterForm />
                <CurrentStats />
                <StateTable />
            </div>);
    }
}

export default MainPage;