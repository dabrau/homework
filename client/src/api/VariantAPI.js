export const getVariants = (genes) => {
  const queryParamString = genes.length > 0 ? `?gene=${genes.join(',')}` : '';
  return fetch(`http://localhost:5000/variant${queryParamString}`, {
      mode: 'cors',
      credentials: 'omit'
    })
    .then(resp => resp.json());
};

export const getGeneSuggestions = queryString => {
  return fetch(`http://localhost:5000/suggest?gene=${queryString}`, {
      mode: 'cors',
      credentials: 'omit'
    })
    .then(resp => resp.json());
};