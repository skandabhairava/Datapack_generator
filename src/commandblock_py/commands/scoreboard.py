SCOREBOARDS = []

def declare(objective:str, displayname:str=None, criteria:str="dummy"):
    """
    objective:str -> The id/name given to a scoreboard
    displayname:str -> The name that will be displayed on screen
    criteria:str -> The criteria of the scoreboard
    """

    f = f"scoreboard objectives add {objective} {criteria}"
    global SCOREBOARDS
    SCOREBOARDS.append(objective)

    if displayname == None:
        return f"scoreboard objectives add {objective} {criteria}\n"
    else:
        return f"scoreboard objectives add {objective} {criteria} \"{displayname}\"\n"

def set_val(objective:str, selector:str="@s", value:int=0):
    """
    objective:str -> The id of the scoreboard
    selector:str -> The entity of which scoreboard value needs to be changed
    value:int -> The Value that needs to be set to the specific scoreboard
    """

    return f"scoreboard players set {selector} {objective} {value}\n"

def add_val(objective:str, selector:str="@s", value:int=0):
    """
    objective:str -> The id of the scoreboard
    selector:str -> The entity of which scoreboard value needs to be changed
    value:int -> The Value that needs to be added to the specific scoreboard (ONLY +ve)
    """

    if value < 0:
        return f"scoreboard players add {selector} {objective} 0\n##NEGATIVE INTEGERS ISNT ACCEPTED FOR THIS FUNCTION##\n"
    return f"scoreboard players add {selector} {objective} {value}\n"

def sub_val(objective:str, selector:str="@s", value:int=0):
    """
    objective:str -> The id of the scoreboard
    selector:str -> The entity of which scoreboard value needs to be changed
    value:int -> The Value that needs to be subtracted to the specific scoreboard (ONLY +ve)
    """

    if value < 0:
        return f"scoreboard players add {selector} {objective} 0\n##NEGATIVE INTEGERS ISNT ACCEPTED FOR THIS FUNCTION##\n"
    return f"scoreboard players remove {selector} {objective} {value}\n"

def remove_all():
    """
    Remove all Scoreboards
    """
    global SCOREBOARDS
    syntax = ""
    for score in SCOREBOARDS:
        syntax += f"scoreboard objectives remove {score}\n"

    return syntax