import pytest

from mp3_sorter_tagger.helpers import extract_year


@pytest.mark.parametrize(
    "folder_name, year, name",
    [
        ("2002 - Virgin Mary", "2002", "Virgin Mary"),
        ("2005 Close to human", "2005", "Close to human"),
        (
            "Diary Of Dreams - 2002 - Freak Perfume (Ltd.Ed)",
            "2002",
            "Diary Of Dreams -  - Freak Perfume (Ltd.Ed)",
        ),
        ("Faderhead (2010) - Black Friday", "2010", "Faderhead () - Black Friday"),
        (
            "Faderhead-Atoms_and_Emptiness-2014-FWYH",
            "2014",
            "Faderhead-Atoms_and_Emptiness--FWYH",
        ),
        ("(2005) Flesh Field - Inferior", "2005", "Flesh Field - Inferior"),
        (
            "VA - Im Rhythmus Bleiben - A Tribute To Front 242 - Vol. 1 (2015)",
            "2015",
            "VA - Im Rhythmus Bleiben - A Tribute To Front 242 - Vol. 1",
        ),
        ("1994 -Afterglow", "1994", "Afterglow"),
        ("_2013 - Goetia V", "2013", "Goetia V"),
        ("1985 - Laibach (re issue 1999)", None, "1985 - Laibach (re issue 1999)"),
        ("March Violets - Natural History", None, "March Violets - Natural History"),
    ],
)
def test_extract_year(folder_name, year, name):
    res_year, res_name = extract_year(folder_name)

    assert res_year == year
    assert res_name == name
