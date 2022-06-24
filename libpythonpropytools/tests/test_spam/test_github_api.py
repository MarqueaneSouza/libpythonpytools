from unittest.mock import Mock

import pytest

from libpythonpropytools import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/104281099?v=4'
    resp_mock.json.return_value = {
        'login': 'MarqueaneSouza', 'id': 104281099,
        'avatar_url': url,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('marqueanesouza')
    assert avatar_url


def test_buscar_avatar_integração():
    url = github_api.buscar_avatar('marqueanesouza')
    assert 'https://avatars.githubusercontent.com/u/104281099?v=4' == url
