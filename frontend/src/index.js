import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";

import "bootstrap/dist/css/bootstrap.min.css";
// import CurrentStats from "./components/currentStats";
// import StateTable from "./components/stateTable";
// import FetchTest from "./components/fetchtest";
// import Navbar from "react-bootstrap/Navbar";

// import { Router, hashHistory as history } from 'react-router';
// Your routes.js file
// import routes from './routes';

import { BrowserRouter, Route, Switch } from 'react-router-dom';

import PatientPage from './components/patientpage';
import MainPage from "./components/mainpage";

ReactDOM.render(
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/" component={MainPage} exact />
        <Route path="/pat_filter" component={PatientPage} />
        <Route component={Error} />
      </Switch>
    </div>
  </BrowserRouter>
  // <React.StrictMode>
  //   <MainPage />
  // </React.StrictMode>
  // <Router routes={routes} history={history} />
  ,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
