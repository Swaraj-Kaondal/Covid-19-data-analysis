import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';

class FilterForm extends Component {
    state = {}
    render() {
        return (
            <React.Fragment>
                <center>
                    <NavLink className="btn btn-danger" to="/pat_filter">View Patient Data</NavLink>
                </center>
            </React.Fragment>
        );
    }
}

export default FilterForm;