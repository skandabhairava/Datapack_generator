from typing import List, Dict
import json

def say(context:str="") -> str :
    """
    context:str -> The text to be printed in chat
    """
    return f"say {context}\n"

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

def kill(selector:str="") -> str:
    """
    selector:str -> All the entities that must be killed
    """
    return f"kill {selector}\n"

def tellraw(selector:str, nbt:Dict):
    """
    selector:str -> The thing to say the tellraw to
    nbt:dict -> the json/nbt needed for the tellraw, might add ez nbt later
    """
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
