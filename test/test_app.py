from homework.app.variant import Variant, db

def test_variant(client):
    assert client.get('/variant').status_code == 200

    db.session.add_all([
        Variant(id=1, gene='AAA'),
        Variant(id=2, gene='AAA'),
        Variant(id=3, gene='ABB'),
    ])
    db.session.commit()

    # no query string
    rv = client.get('/variant')
    json = rv.get_json()
    assert json['hits'] == 0
    assert json['results'] == []

    # empty query string
    rv = client.get('/variant?gene=')
    json = rv.get_json()
    assert json['hits'] == 0
    assert json['results'] == []

    # match gene
    rv = client.get('/variant?gene=AAA')
    json = rv.get_json()
    assert json['hits'] == 2
    result_ids = [r['id'] for r in json['results']]
    assert result_ids == [1, 2]

    # match multiple genes
    rv = client.get('/variant?gene=AAA,ABB')
    json = rv.get_json()
    assert json['hits'] == 3
    result_ids = [r['id'] for r in json['results']]
    assert result_ids == [1, 2, 3]


def test_suggest(client):
    assert client.get('/suggest').status_code == 200

    db.session.add_all([
        Variant(id=1, gene='AAA'),
        Variant(id=2, gene='aaa'),
        Variant(id=3, gene='ABB'),
        Variant(id=4, gene='ABC'),
        Variant(id=5, gene='ABC'),
        Variant(id=6, gene='ABC'),
        Variant(id=7, gene='BBC')
    ])
    db.session.commit()

    # no query string
    rv = client.get('/suggest')
    json = rv.get_json()
    assert json == [] 

    # empty query string
    rv = client.get('/suggest?gene=')
    json = rv.get_json()
    assert json == []

    # case insensitive
    rv = client.get('/suggest?gene=aA')
    json = rv.get_json().sort()
    assert json == ['AAA','aaa'].sort()

    # no duplicates
    rv = client.get('/suggest?gene=AB')
    json = rv.get_json().sort()
    assert json == ['ABB','ABC'].sort()
