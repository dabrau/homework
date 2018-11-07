from homework.app.variant import Variant

def test_variant():
    attr = Variant().attributes()
    expected = ['id', 'gene', 'nucleotide_change', 'protein_change', 'other_mappings', 'alias',
        'transcripts', 'region', 'reported_classification', 'inferred_classification', 'source',
        'last_evaluated', 'last_updated', 'url', 'submitter', 'assembly', 'chr', 'genomic_start',
        'genomic_stop', 'ref', 'alt', 'accession', 'reported_ref', 'reported_alt']
    
    assert attr == expected

    variant = Variant(id=1, gene='ABC', nucleotide_change='nuc', url='google.com')
    variant_dict = variant.as_dict()
    assert variant_dict['id'] == 1
    assert variant_dict['gene'] == 'ABC'
    assert variant_dict['nucleotide_change'] == 'nuc'
    assert variant_dict['url'] == 'google.com'
    
    other_attrs = [variant_dict[att] for att in variant_dict.keys() if att not in ['id', 'gene', 'nucleotide_change', 'url']]
    assert all(att is None for att in other_attrs)