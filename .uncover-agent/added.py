    if '@' not in u.netloc:
        return url
    return u._replace(netloc=u.netloc.rpartition('@')[2]).geturl()
@pytest.mark.parametrize('url,expected', [
    ['https://user:pw@example.org/x', 'https://example.org/x'],
    ['https://token@example.org/x', 'https://example.org/x'],
    ['mqtt://user:@broker:1883', 'mqtt://broker:1883'],
    ['postgresql://u:p@ss@db:5432/x?a=b', 'postgresql://db:5432/x?a=b'],
    ['https://example.org/x?email=a@b.c', 'https://example.org/x?email=a@b.c'],
    ['https://example.org/x', 'https://example.org/x'],
])
def test_remove_url_auth(url, expected):
    assert util.remove_url_auth(url) == expected

