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