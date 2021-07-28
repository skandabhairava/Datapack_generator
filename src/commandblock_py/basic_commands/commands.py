from typing import List, Dict, Union, Tuple
import json
from colorama import Fore, Style, init
init(convert=True)

def say(content:str="") -> str :
    """
    context:str -> The text to be printed in chat
    """
    return f"say {content}\n"

#def op(player:str="") -> str:
    """
    player:str -> Ops the player given
    """
    #return f"op {player}\n"

#def deop(player:str="") -> str:
    """
    player:str -> Deops the player given
    """
    #return f"deop {player}\n"

def kill(selector:str="@s") -> str:
    """
    selector:str -> All the entities that must be killed
    """

    return f"kill {selector}\n"

def tellraw(selector:str="@s", nbt:Dict={"text":"foo"}):
    """
    selector:str -> The thing to say the tellraw to
    nbt:dict -> the json/nbt needed for the tellraw, might add ez nbt later
    """
    if "@e" in selector:
        return f"tellraw @a {json.dumps(nbt)}\n## @e IS NOT ACCEPTED BY THIS FUNCTION ##"
    return f"tellraw {selector} {json.dumps(nbt)}\n"

def schedule(option:str, function:str, time:str = ""):
    """
    option:str -> The option to schedule (clear or function)
    function:str -> The function to be scheduled/cleared
    time:str -> The time to be scheduled ( d = day, s = seconds, and t = ticks) (only if option is "function")
    """

    if option == "function":
        return f"schedule {option} {function} {time}\n"
    
    elif option == "clear":
        return f"schedule {option} {function}\n"
    
    else:
        return ""

def tp(selector:Union[str, tuple]="@s", selector2:Union[str, tuple]=("~", "~", "~")):
    """
    selector:Union[str, tuple] -> The position to be moved from
    selector2:Union[str, tuple] -> The position to be moved to
    """

    if isinstance(selector, tuple):
        if len(selector) < 3:
            selector = ("~", "~", "~")

        return f"tp {selector[0]} {selector[1]} {selector[2]}\n"

    else:
        if isinstance(selector2, tuple):
            if len(selector2) < 3:
                selector2 = ("~", "~", "~")
            return f"tp {selector} {selector2[0]} {selector2[1]} {selector2[2]}\n"
        
        else:
            return f"tp {selector} {selector2}\n"


def playsound(sound:str="minecraft:ui.button.click", target:str="@s", block_pos:tuple=("~", "~", "~"), sound_type:str="master", volume:float=None, pitch:float=None, min_vol:float=None):
    """
    sound:str -> The minecraft sound file name
    target:str -> The entity to which the sound must be played
    block_pos:tuple -> The position at which the sound must be played
    sound_type:str -> The type of sound that must be played (default : master)
    volume:float -> The volume of the sound that will be played [Optional]
    pitch:float -> The pitch of the sound that will be played [Optional]
    min_volume:float -> The minimum volume of the sound that will be played [Optional]
    """

    if len(block_pos) < 3:
        block_pos = ("~", "~", "~")

    if not "@e" in target:
        syntax = f"playsound {sound} {sound_type} {target} {block_pos[0]} {block_pos[1]} {block_pos[2]}"
        write_at_end = False
    else:
        syntax = f"playsound {sound} {sound_type} @s {block_pos[0]} {block_pos[1]} {block_pos[2]}"
        write_at_end = True

    if volume != None:
        syntax += f" {volume}"
        if pitch != None:
            syntax += f" {pitch}"
            if min_vol != None:
                syntax += f" {min_vol}"

    if write_at_end:
        syntax = f"{syntax}\n## @e CANNOT BE USED IN STOPSOUND COMMAND, AND HENCE TARGET BEEN REVERTED TO @s##"

    return f"{syntax}\n"

def stopsound(target:str="@s", sound_type:str=None, sound:str=None):
    """
    target:str -> The entity to which the playing sound must be stopped
    sound_type:str -> The type of sound that must be stopped playing
    sound:str -> The minecraft sound file name
    """

    if not "@e" in target:
        syntax = f"stopsound {target}"
        write_at_end = False
    else:
        syntax = "stopsound @s"
        write_at_end = True

    if sound_type != None:
        syntax += f" {sound_type}"
        if sound != None:
            syntax += f" {sound}"

    if write_at_end:
        syntax = f"{syntax}\n## @e CANNOT BE USED IN STOPSOUND COMMAND, AND HENCE TARGET BEEN REVERTED TO @s##"

    return f"{syntax}\n"

def function(function:Union[str, object]=""):
    """
    function:str -> The function to be run
    """

    #print(function)

    if function == None:
        print(f'{Fore.YELLOW}WARNING : Detected that you passed None instead of a string or function into the basic_commands.commands.function, will continue but it may cause your datapack to not work{Style.RESET_ALL}')

    if callable(function):
        return f"function {function.mcfunction}\n"

    else:
        if function != "":
            return f"function {function}\n"
        else:
            return ""
