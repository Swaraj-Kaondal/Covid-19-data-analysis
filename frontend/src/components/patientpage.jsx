import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import Table from "react-bootstrap/Table";

import * as utils from "../utils/commonFunctions";

class PatientPage extends Component {
    state = { isData: false }
    patientUrl = utils.baseURL + utils.patient_filter
    form = {}

    async componentDidMount() {
        const requestOptions = {
            method: 'post',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: JSON.stringify({ data: "" })
        };
        var data = await (await fetch(this.patientUrl, requestOptions)).json();
        this.setState({
            datKeys: Object.keys(data).slice(0, 15),
            data: data,
            isData: true,
            entries: Object.keys(data).length,
        })
        console.log("state issssssssssss" + this.state);
    }
    render() {
        return (
            <React.Fragment>
                <NavLink to="/" className="btn btn-danger">Home Page</NavLink>
                <center>
                    <input type="text" placeholder="age low" name="age1" onChange={this.changeForm} />
                    <input type="text" placeholder="age high" name="age2" onChange={this.changeForm} />
                    <input type="text" placeholder="date low" name="date1" onChange={this.changeForm} />
                    <input type="text" placeholder="date high" name="date2" onChange={this.changeForm} />
                    <input type="text" placeholder="state name" name="state" onChange={this.changeForm} />
                    <input type="text" placeholder="gender" name="gender" onChange={this.changeForm} />
                    <input type="text" placeholder="status" name="status" onChange={this.changeForm} />
                    <br />
                    <input className="btn btn-danger" type="submit" onClick={this.submitForm} />

                    {this.state.isData && (
                        <React.Fragment>
                            <h2> Total entries: {this.state.entries}</h2>
                            <Table
                                striped
                                bordered
                                hover
                                key="patientTable"
                                style={{ width: "80%" }}
                            >
                                <thead className="thead-dark">
                                    <tr>
                                        <th>Patient ID</th>
                                        <th>Name</th>
                                        <th>Gender</th>
                                        <th>Age</th>
                                        <th>Status</th>
                                        <th>Date</th>
                                        <th>State</th>
                                    </tr>
                                </thead>
                                <tbody>{this.state.datKeys.map(this.patientTabl)}</tbody>
                            </Table>
                        </React.Fragment>

                    )}
                    {!this.state.isData && (<h1>Loading...</h1>)}
                </center>
            </React.Fragment>
        );
    }
    patientTabl = (value, index, array) => {
        if (this.state.data[value] != null) {
            return (
                <tr key={value}>
                    <th>{value}</th>
                    <th>{this.state.data[value]["Name"]}</th>
                    <th>{this.state.data[value]["Gender"]}</th>
                    <th>{this.state.data[value]["Age"]}</th>
                    <th>{this.state.data[value]["Status"]}</th>
                    <th>{this.state.data[value]["Date"]}</th>
                    <th>{this.state.data[value]["State"]}</th>
                </tr>
            );
        }
    };

    changeForm = async (event) => {
        var key = event.target.name;
        var value = event.target.value
        var v = { [key]: await value }
        this.form[key] = value;
        console.log(this.form)
    }
    submitForm = async () => {
        const payload = this.state;
        this.setState({ isData: false })
        var data = this.form;
        console.log("i am sending" + JSON.stringify({ data }))
        // data.append(JSON.stringify(payload));
        const requestOptions = {
            method: "post",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: JSON.stringify({ data }),
        };
        var data = await (await fetch(this.patientUrl, requestOptions)).json();
        this.setState({
            data: data,
            datKeys: Object.keys(data).slice(0, 15),
            isData: true,
            entries: Object.keys(data).length,
        })
        console.log(data);

    }
}

export default PatientPage;