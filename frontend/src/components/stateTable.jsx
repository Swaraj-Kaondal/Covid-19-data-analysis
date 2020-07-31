import React, { Component } from "react";

import Drawer from "react-drag-drawer";
import Graph from "./graph";
import * as utils from "../utils/commonFunctions";
import Table from "react-bootstrap/Table";
import "./stateTable.css";

class StateTable extends Component {
  state = { popup: false, isStateData: false, isPatientData: false };
  CdataPoints = [];
  AdataPoints = [];
  RdataPoints = [];
  DdataPoints = [];
  currentState = "";
  tableData = [1, 2, 3, 4, 5, 5, 6, 7, 8, 3, 3, 3, 4, 52, 1];
  chartSize = 300;
  confChart = {
    chartSize: this.chartSize,
    title: "Confirmed",
    colour: "blue",
    titleStyle: { color: "blue" },
  };
  actChart = {
    chartSize: this.chartSize,
    title: "Active",
    colour: "gray",
    titleStyle: { color: "gray" },
  };
  recChart = {
    chartSize: this.chartSize,
    title: "Recovered",
    colour: "green",
    titleStyle: { color: "green" },
  };
  decChart = {
    chartSize: this.chartSize,
    title: "Deceased",
    colour: "red",
    titleStyle: { color: "red" },
  };

  buttonClick = async (v) => {
    var state_data = await utils.getCurrentData(utils.state_wise + v);
    var patient_data = await utils.getCurrentData(this.patientDataUrl + v);
    //console.log("JSON data test" + JSON.stringify(patient_data));
    var patients = [];
    this.setState({ patientData: patient_data });

    patients = Object.keys(patient_data);

    this.setState({ patients: patients.slice(1, 10) });
    this.setState({ isPatientData: true });

    this.CdataPoints = state_data.C;
    this.AdataPoints = state_data.A;
    this.RdataPoints = state_data.R;
    this.DdataPoints = state_data.D;
    this.currentState = v;
    this.setState({ popup: true });
  };

  patientTabl = (value, index, array) => {
    if (this.state.patientData[value] != null) {
      return (
        <tr key={value}>
          <th>{value}</th>
          <th>{this.state.patientData[value]["Name"]}</th>
          <th>{this.state.patientData[value]["Gender"]}</th>
          <th>{this.state.patientData[value]["Age"]}</th>
          <th>{this.state.patientData[value]["Status"]}</th>
          <th>{this.state.patientData[value]["Date"]}</th>
        </tr>
      );
    }
  };

  stateTabl = (value, index, array) => {
    return (
      <tr key={value} onClick={() => this.buttonClick(value)}>
        <th>{value}</th>
        <th>{this.state.stateData[value]["C"]}</th>
        <th>{this.state.stateData[value]["A"]}</th>
        <th>{this.state.stateData[value]["R"]}</th>
        <th>{this.state.stateData[value]["D"]}</th>
        <th>{this.state.stateData[value]["S"]}</th>
      </tr>
    );
  };

  stateDataUrl = utils.all_states;
  patientDataUrl = utils.all_patients;

  async componentDidMount() {
    var stateJsonResponse = await utils.getCurrentData(this.stateDataUrl);

    var states = [];

    // console.log(stateJsonResponse);
    this.setState({ stateData: stateJsonResponse });

    states = Object.keys(stateJsonResponse);

    this.setState({ states: states });
    this.setState({ isStateData: true });

    // console.log("statesL " + this.state.states);
    // console.log(this.state.stateData.Maharashtra.C);
    //console.log(this.state.isStateData + " " + this.state.isPatientData);
  }

  render() {
    // if (this.state.isStateData == true) {
    //   console.log("hello from moint " + JSON.stringify(this.state));
    //   console.log("states: " + this.state.states);
    // } else {
    //   console.log("not yet");
    // }
    return (
      <React.Fragment>
        <center className="main">
          <Drawer
            open={this.state.popup}
            onRequestClose={() => this.setState({ popup: !this.state.popup })}
          >
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />

            <div style={{ background: "white", paddingBottom: "40px" }}>
              <center>
                <h1> {this.currentState}</h1>
              </center>
              <br />
              <br />
              <div className="chart-container">
                <div
                  className="chart-container"
                  style={{ marginRight: 100, paddingLeft: 20 }}
                >
                  <Graph
                    dataPoints={this.CdataPoints.map(utils.jsonify)}
                    options={this.confChart}
                  />
                </div>

                <div
                  className="chart-container"
                  style={{ marginRight: 100, marginLeft: 100 }}
                >
                  <Graph
                    dataPoints={this.AdataPoints.map(utils.jsonify)}
                    options={this.actChart}
                  />
                </div>

                <div
                  className="chart-container"
                  style={{ marginRight: 100, marginLeft: 100 }}
                >
                  <Graph
                    dataPoints={this.RdataPoints.map(utils.jsonify)}
                    options={this.recChart}
                  />
                </div>

                <div
                  className="chart-container"
                  style={{
                    marginLeft: 100,
                    marginRight: 150,
                    paddingRight: 20,
                  }}
                >
                  <Graph
                    dataPoints={this.DdataPoints.map(utils.jsonify)}
                    options={this.decChart}
                  />
                </div>
              </div>
              <center>
                {this.state.isPatientData && (
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
                      </tr>
                    </thead>
                    <tbody>{this.state.patients.map(this.patientTabl)}</tbody>
                  </Table>
                )}
              </center>
            </div>
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
          </Drawer>

          {this.state.isStateData && (
            <Table
              striped
              bordered
              hover
              key="stateTable"
              style={{ width: "80%" }}
            >
              <thead className="thead-dark">
                <tr>
                  <th>State</th>
                  <th>Confirmed</th>
                  <th>Active</th>
                  <th>Recovered</th>
                  <th>Deceased</th>
                  <th>Sentiment</th>
                </tr>
              </thead>
              <tbody>{this.state.states.map(this.stateTabl)}</tbody>
            </Table>
          )}
        </center>
      </React.Fragment>
    );
  }
}

export default StateTable;
