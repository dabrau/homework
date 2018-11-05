import React, { Component, Fragment } from 'react';
import ReactTable from 'react-table';
import { Glyphicon } from 'react-bootstrap';

import 'react-table/react-table.css';

const capitalize = ([s, ...tring]) => (
  [s.toUpperCase(), ...tring]
    .join('')
);

const titleCase = attrName => (
  attrName
    .split('_')
    .map(capitalize)
    .join(' ')
);

const simpleAttr = [
  'gene',
  'protein_change',
  'alias',
  'region',
  'reported_classification',
  'last_evaluated',
  'last_updated'
];

const simpleColumns = simpleAttr.map(att => ({ Header: titleCase(att), accessor: att }));
const sourceLinkColumn = {
  Header: 'Source',
  id: 'source',
  accessor: d => ({source: d.source, url: d.url }),
  Cell: row => (<a href={row.value.url} target='_blank'>{row.value.source}</a>)
};

class ExpandableList extends React.Component {
  state = { isExpanded: false };
  handleExpand = () => this.setState({ isExpanded: true });
  handleCollapse = () => this.setState({ isExpanded: false });

  render() {
    if (!this.state.isExpanded) {
      return (
        <span>
          <Glyphicon glyph='triangle-right' onClick={this.handleExpand} />
          {this.props.mappings.join(", ")}
        </span>
      );
    }
    return (
      <div>
        <Glyphicon glyph='triangle-bottom' onClick={this.handleCollapse} />
        <ul>
          {this.props.mappings.map((m, ind) => (
            <li key={ind}>{m}</li>
          ))}
        </ul>
      </div>
    );
  }
}

const nucleotideChangeColumn = {
  Header: 'Nucleotide Change',
  accessor: 'other_mappings',
  Cell: row => {
    const mappings = row.value.split(',');
    if (mappings.length === 0) {
      return null;
    }
    if (mappings.length === 1) {
      return <span>{row.value}</span>;
    }
    return <ExpandableList mappings={mappings} />;
  }
};

const [geneColumn, ...everythingElse] = simpleColumns;
const columns = [geneColumn, nucleotideChangeColumn, ...everythingElse, sourceLinkColumn];


class ResultsTable extends Component {
  render() {
    return (
      <Fragment>
        <span>{`${this.props.variants.hits} results`}</span>
        <ReactTable
          data={this.props.variants.results}
          columns={columns}
          noDataText='No variants found'
          loading={this.props.isFetching}
          className='-striped -highlight'
          defaultPageSize={10}
        />
      </Fragment>
    );
  }
}

export default ResultsTable;