import React, { Component } from "react";
import "./Graphs.css";
import * as utils from "../utils/commonFunctions";

import Graph from "./graph";

class CurrentStats extends Component {
  state = {
    isData: false,
  };
  constructor(props) {
    super(props);
  }

  dataUrl = utils.current_stats;

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

  async componentDidMount() {
    var jsonResponse = await utils.getCurrentData(this.dataUrl);
    this.setState({
      C: await jsonResponse.C,
      A: await jsonResponse.A,
      R: await jsonResponse.R,
      D: await jsonResponse.D,
      isData: true,
    });
  }
  render() {
    return (
      <React.Fragment>
        <div style={{ marginTop: "30px" }}>
          {this.state.isData && (
            <div
              className="chart-container"
              style={{
                justifyContent: "center",
              }}
            >
              <div
                className="chart-container"
                style={{ marginRight: 100, paddingLeft: 20 }}
              >
                <Graph
                  dataPoints={this.state.C.map(utils.jsonify)}
                  options={this.confChart}
                />
              </div>
              <div
                className="chart-container"
                style={{ marginRight: 100, marginLeft: 100 }}
              >
                <Graph
                  dataPoints={this.state.A.map(utils.jsonify)}
                  options={this.actChart}
                />
              </div>
              <div
                className="chart-container"
                style={{ marginRight: 100, marginLeft: 100 }}
              >
                <Graph
                  dataPoints={this.state.R.map(utils.jsonify)}
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
                  dataPoints={this.state.D.map(utils.jsonify)}
                  options={this.decChart}
                />
              </div>
            </div>
          )}
        </div>
      </React.Fragment>
    );
  }
}

export default CurrentStats;
