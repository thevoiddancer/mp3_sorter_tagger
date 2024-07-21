import pytest

from mp3_sorter_tagger.helpers import check_album_has_year


@pytest.mark.parametrize(
    "test_params",
    [pytest.param({"name": "2002 - Floodland", "expected": True}, id="has year")],
)
def test_check_year(test_params):
    name = test_params["name"]
    expected = test_params["expected"]

    assert check_album_has_year(name) == expected
