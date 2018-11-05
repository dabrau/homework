import React, { Component } from 'react';
import Search from './Search';
import ResultsTable from './ResultsTable'
import { getVariants } from '../api/VariantAPI';
import { Grid, Row, Col } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.min.css';

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
    console.log(this.state, "results")
    return (
      <Grid>
        <Row>
          <Col sm={6} smOffset={3} >
            <Search onClick={this.getVariants} />
          </Col>
        </Row>
        <ResultsTable {...this.state} />
      </Grid>
    );
  }
}

export default App;