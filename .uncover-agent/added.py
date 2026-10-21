        if v.get('visibility', 'default') == 'hidden' \
                and dataset is None:
@pytest.fixture()
def config_exclusively_hidden_resources():
    filename = 'pygeoapi-test-config-exclusively-hidden-resources.yml'
    with open(get_test_file_path(filename)) as fh:
        return yaml_load(fh)


@pytest.fixture()
def api_exclusively_hidden_resources(config_exclusively_hidden_resources, openapi): # noqa
    '''Returns an API instance where all resources are marked as hidden'''
    return API(config_exclusively_hidden_resources, openapi)


def test_describe_collections_with_only_hidden_resources(
    api_exclusively_hidden_resources
):
    '''
    Test an API with only hidden resources to ensure
    there are no indexing errors when no collections are returned
    '''
    req = mock_api_request({})
    _, code, response = describe_collections(api_exclusively_hidden_resources, req)  # noqa
    assert code == HTTPStatus.OK

    collections = json.loads(response)
    assert len(collections['collections']) == 0, \
        'All collections are hidden so there should be none in the response'

    hidden_collection_name = 'objects'
    _, code, response = describe_collections(
        api_exclusively_hidden_resources, req, hidden_collection_name
    )

    assert code == HTTPStatus.OK
    collection = json.loads(response)
    assert collection['title'] == 'GeoJSON objects', \
        'The collection should have its normal title even if hidden'

