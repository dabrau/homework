export const getVariants = (genes) => {
  const queryParamString = genes.length > 0 ? `?gene=${genes.join(',')}` : '';
  return fetch(`/variant${queryParamString}`, {
      mode: 'cors',
      credentials: 'omit'
    })
    .then(resp => resp.json());
};

export const getGeneSuggestions = queryString => {
  return fetch(`/suggest?gene=${queryString}`, {
      mode: 'cors',
      credentials: 'omit'
    })
    .then(resp => resp.json());
};