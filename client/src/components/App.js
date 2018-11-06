import React, { Component } from 'react';
import Search from './Search';
import ResultsTable from './ResultsTable'
import { getVariants } from '../api/VariantAPI';
import { Grid, Row, Col } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

class App extends Component {
  state = {
    isFetching: false,
    variants: { attributes: [], hits: 0, results: [] }
  };
  getVariants = genes => {
    this.setState({ isFetching: true });
    getVariants(genes)
      .then(results => this.setState({
        isFetching: false,
        variants: results
      }))
      .catch(e => this.setState({ isFetching: false }))
  }

  render() {
    return (
      <div className='app-container'>
        <Search onClick={this.getVariants} />
        <ResultsTable {...this.state} />
      </div>
    );
  }
}

export default App;