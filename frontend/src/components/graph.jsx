import React, { Component } from "react";
import "./Graphs.css";
import * as utils from "../utils/commonFunctions";

import CanvasJSReact from "./canvasjs.react";

var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class Graph extends Component {
  constructor(props) {
    super(props);
  }

  test_data = [1, 2, 3, 2.2, 3, 5, 6, 4, 2, 4, 3.3, 4, 3, 3.1];

  render() {
    const options = {
      animationEnabled: true,
      animationDuration: 2000,

      height: this.props.options.chartSize,
      width: this.props.options.chartSize,

      axisX: {
        tickThickness: 0,
        labelFontSize: 0,
        lineThickness: 0,
        gridThickness: 0,
      },
      axisY: {
        stripLines: [
          {
            startValue: 0,
            endValue: 1,
            color: "#ff00ff",
          },
        ],
        tickThickness: 0,
        labelFontSize: 0,
        lineThickness: 0,
        gridThickness: 0,
      },
      data: [
        {
          lineColor: this.props.options.colour,
          markerSize: 1,
          type: "spline",
          dataPoints: this.props.dataPoints,
        },
      ],
    };

    return (
      <React.Fragment>
        <center>
          <div className="center_title">
            <h5 className="GraphTitle" style={this.props.options.titleStyle}>
              {this.props.options.title}
            </h5>
            <p className="GraphTitle" style={this.props.options.titleStyle}>
              {this.props.dataPoints.slice(-1)[0].y}
            </p>
          </div>
          <CanvasJSChart options={options} />
        </center>
      </React.Fragment>
    );
  }
}

export default Graph;
