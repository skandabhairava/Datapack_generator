import array, sys, os
from colorama import Fore, Style

curdir = os.getcwd()
def selector(target:str="@s", distance:str=None, scores:dict=None, tags:array=None, team:str=None, type:str=None, nbt:dict=None, etcetera_args:str=None) -> None:

    MAIN_SYNTAX = ""
    _lock = False
    _write_comment = False

    MAIN_SYNTAX += f"{target}["

    if not distance == None:
        MAIN_SYNTAX += f"distance={distance}, "
        _lock = True

    if not scores == None:
        scores_f = "scores={"
        for score_name, score_val in scores.items():
            scores_f += f"{score_name}={score_val},"
        scores_f = scores_f[:-1] + "}"
        MAIN_SYNTAX += scores_f + ", "
        _lock = True

    if not tags == None:
        tag = ""
        for items in tags:
            tag += f"tag={items},"
        tag = tag[:-1]
        MAIN_SYNTAX += tag + ", "
        _lock = True

    if not team == None:
        MAIN_SYNTAX += f"team={team}, "
        _lock = True

    if not type == None:
        if target == "@e" or target == "@s":
            MAIN_SYNTAX += f"type={type}, "
            _lock = True
        else:
            _write_comment = True

    if not nbt == None:
        nbt = str(nbt).replace('\n', '')
        MAIN_SYNTAX += f"nbt={nbt}, "
        _lock = True

    if not etcetera_args == None:
        MAIN_SYNTAX += f"{etcetera_args}, "
        _lock = True

    if _lock == True:
        MAIN_SYNTAX = MAIN_SYNTAX[:-2]

    MAIN_SYNTAX += "]"

    if _write_comment:
        MAIN_SYNTAX += "\n## It seems you have provided a target value of @a / @p / @r and a type value. These target selectors do not take a type arg ##"

    return MAIN_SYNTAX