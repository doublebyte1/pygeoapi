        f = str(int(nbytes))
@pytest.mark.parametrize('nbytes,expected', [
    (500, 500),
    (1024, '1K'),
    (1536, '1K'),
    (10240, '10K'),
    (102400, '100K'),
    (1048576, '1M'),
    (1572864, '1.5M'),
    (10485760, '10M'),
    (1073741824, '1G'),
])
def test_human_size(nbytes, expected):
    assert util.human_size(nbytes) == expected

