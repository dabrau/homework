import React, { Component } from 'react';
import { AsyncTypeahead } from 'react-bootstrap-typeahead';
import { FormGroup, InputGroup, Button, Glyphicon } from 'react-bootstrap';
import { getGeneSuggestions } from '../api/VariantAPI';

import 'react-bootstrap-typeahead/css/Typeahead.css';
import './Search.css';

class Search extends Component {
  state = {
    isLoading: false,
    options: [],
    selected: []
  };
  handleChange = selected => this.setState({ selected });
  handleTypeAheadSearch = query => {
    this.setState({ isLoading: true });
    getGeneSuggestions(query)
      .then(options => {
        this.setState({
          isLoading: false,
          options,
        });
      })
      .catch(e => this.setState({ isLoading: false }))
  };
  handleClick = () => this.props.onClick(this.state.selected);

  render() {
    return (
      <div className='search-container'>
        <InputGroup className='search'>
        <AsyncTypeahead
          {...this.state}
          clearButton
          minLength={2}
          allowNew={false}
          multiple={true}
          placeholder='Search for genes...'
          highlightOnlyResult={true}
          selectHintOnEnter={false}
          onChange={this.handleChange}
          onSearch={this.handleTypeAheadSearch}
        />
        <InputGroup.Button className='input-group-append'>
          <Button bsStyle='primary' onClick={this.handleClick} >
            <Glyphicon glyph='search'/>
          </Button>
        </InputGroup.Button>
        </InputGroup>
      </div>
    );
  }
}

export default Search;