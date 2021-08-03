if_unless_list = ["if", "unless"]

def align(axes:str):
    """
    axes:str -> Updates the command's execution position, aligning to its current block position
    "x", "xz", "xyz", "yz", "y", "z", "xy"
    """
    if not isinstance(axes, str):
        return ""

    h = ["x", "y", "z"]
    b = []

    for i in axes:
        if (not i in h) or i in b:
            return ""
        b.append(i)

    return f"align {axes}"

def anchor(anchor_at:str):
    """
    anchor_at:str -> Sets the execution anchor to the eyes or feet. Defaults to feet.
    "eyes", "feet"
    """

    if not isinstance(anchor_at, str):
        return ""

    a = ["eyes", "feet"]

    if not anchor_at in a:
        return ""

    return f"anchored {anchor_at}"

def as_cmd(selector:str):
    """
    selector:str -> Sets the command's executor to target entity, without changing execution position, rotation, dimension, or anchor
    """

    if not isinstance(selector, str):
        return ""
    
    return f"as {selector}"

def at(selector:str):
    """
    selector:str -> Sets the command's executor to target entity, without changing execution position, rotation, dimension, or anchor
    """

    if not isinstance(selector, str):
        return ""
    
    return f"at {selector}"

def facing(position:tuple=None, selector:str=None, anchor:str=None):
    """
    Sets the execution rotation to face a given point, as viewed from its anchor
    position:tuple(str) -> should contain a 3d vector ("~", "~", "~") | Independent arg.
    selector:str -> The entity the command should run facing towards | Independent arg.
    anchor:str -> "eyes", "feet" | Dependent on selector
    """
    if isinstance(position, tuple) and len(position) == 3:
        return f"facing {position[0]} {position[1]} {position[2]}"

    if isinstance(selector, str) and not selector == "":
        fina = selector
        anc = ["feet", "eyes"]
        if isinstance(anchor, str) and (not anchor == "") and anchor in anc:
            fina += " " + anchor
        else: return ""
    else: return ""

    return f"facing entity {fina}"

def in_dim(dimension:str=None):
    """
    Sets the execution dimension and position
    It respects dimension scaling for relative and local coordinates. Applies to custom dimensions as well.
    dimension:str -> contains the whole dimension id.
    "minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"
    """

    if isinstance(dimension, str) and dimension != "":
        return f"in {dimension}"

    return ""

def positioned(position:tuple=None, selector:str=None):
    """
    Sets the execution position , without changing execution rotation or dimension; can match an entity's position
    postion:tuple(str) -> should contain a 3d vector ("~", "~", "~") | Independent arg.
    selector:str -> The entity the command should run facing towards | Independent arg.
    """

    if isinstance(position, tuple) and len(position) == 3:
        return f"positioned {position[0]} {position[1]} {position[2]}"

    if isinstance(selector, str) and selector != "":
        return f"positioned as {selector}"

    return ""

def rotated(rotation:tuple=None, selector:str=None):
    """
    Sets the execution position , without changing execution rotation or dimension; can match an entity's position
    rotation:tuple(float) -> should contain a 2d vector (149.0, 152.5) | Independent arg.
    selector:str -> The entity the command should run facing towards | Independent arg.
    """

    if isinstance(rotation, tuple) and len(rotation) == 2:
        if (isinstance(rotation[0], int) or isinstance(rotation[0], float)) and (isinstance(rotation[1], int) or isinstance(rotation[1], float)):
            return f"rotated {float(rotation[0])} {float(rotation[1])}"

    if isinstance(selector, str) and selector != "":
        return f"rotated as {selector}"

    return ""

def if_unless_block(if_unless:str=None, position:tuple=None, block:str=None):
    """
    Compares the block at a given position to a given block ID or block tag
    if_unless:str -> either should be "if" or "unless" | *important
    position:tuple(str) -> Position of a target block to test, a 3d vector ("~", "~", "~")
    block:str -> the block id, minecraft:stone
    """

    if isinstance(if_unless, str) and if_unless in if_unless_list:

        if (not (isinstance(position, tuple) and isinstance(block, str))):
            return ""
        if len(position) == 3:
            main = f"block {position[0]} {position[1]} {position[2]} {block}"
            main = "if " + main if if_unless == "if" else "unless " + main
            return main

    return ""
