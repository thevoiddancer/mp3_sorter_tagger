import re


def check_album_has_year(dirname):
    return dirname[:4].isnumeric() or dirname[1:5].isnumeric()


def check_name_change_safe(old, new):
    for idx, (letter_old, letter_new) in enumerate(zip(old, new)):
        prev_old = old[idx - 1]
        if letter_old != letter_new and prev_old != " " and idx != 0:
            return False
    return True


# TODO: check if year string or int later on
def split_album_year_name(dirname):
    if not check_album_has_year(dirname):
        year, name = None, dirname
    else:
        try:
            year = int(dirname[:4])
            name = dirname[4:].strip(" -_]")
        except Exception:
            year = int(dirname[1:5])
            name = dirname[5:].strip(" -_]")
    return year, name


def split_album_name_type(dirname):
    types = "|".join(["ep", "single", "remixes"])
    pattern = rf"([\(\[^\w]?({types})[\)\]^\w]?)"
    pattern_compiled = re.compile(pattern, re.I)
    res = re.search(pattern_compiled, dirname)
    if res:
        type = res.group(2)
        name = dirname.split(res.group(1))[0].strip()
    else:
        type, name = None, dirname
    name_original = name.rstrip(" -")
    name_title = name_original.title()
    changed = name_original != name_title
    return name_title, type, name_original, changed
