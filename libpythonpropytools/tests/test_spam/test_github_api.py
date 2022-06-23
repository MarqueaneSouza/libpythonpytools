from libpythonpropytools import github_api


def test_buscar_avatar():
    url = github_api.buscar_avatar('marqueanesouza')
    assert 'https://avatars.githubusercontent.com/u/104281099?v=4' == url
