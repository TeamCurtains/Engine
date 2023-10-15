import database
import type_matcher

keys = {
    "(подпись)": ("string", lambda x: x == "электронная подпись", -1),
    "(расшифровка подписи)": ("name", lambda x: x in database.get_data("employees"), -1),
    "(должность)": ("name", lambda x: x.replace("получил ", "") in database.get_data("roles"), 1),
    "организация": ("string", lambda x: True, 1),
    "типовая межотраслевая форма": ("string", lambda x: True, 1),
    "чеерз кого": ("string", lambda x: True, 1),
    "затребовал": ("string", lambda x: True, 1),
    "разрешил": ("string", lambda x: True, 1),
    "структурное": ("string", lambda x: x.replace("подразделение ", "", 1) in database.get_data("sub"), 1),
    "требование-накладная": ("string", lambda x: True, 1)
}


def apply_matcher(str_arr, str_x):
    for x in keys.keys():
        if x in str(str_arr[str_x].lower()):
            str_in = " ".join(str(str_arr[str_x]).replace(x, "").split())

            if not str_in:
                str_in = str_arr[str_x + keys[x][2]].strip()

            if not type_matcher.match_type(keys[x][0], str_in):
                return False

            return x, keys[x][1](str_in), str_in

    return True

