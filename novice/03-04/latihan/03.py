def test_empty_db(client):
    """start with a blank database"""

    rv = client.get('/')
    assert b'No entries here do far' in rv.data