class _entities():
    CREEPER = "minecraft:creeper"
    SKELETON = "minecraft:skeleton"
    SPIDER = "minecraft:spider"
    ZOMBIE = "minecraft:zombie"
    GHAST = "minecraft:ghast"
    ENDER_DRAGON = "minecraft:ender_dragon"
    ENDER_PEARL = "minecraft:ender_pearl"

class _selectors():
    NEAREST_PLAYER = "@p"
    ALL_PLAYERS = "@a"
    ALL_ENTITIES = "@e"
    RANDOM_PLAYER = "@r"
    CURRENT_ENTITY = "@s"
    ALL_TARGET_SELECTORS = ["@p", "@a", "@e", "@r", "@s"]

entities_list = _entities()

selectors_list = _selectors()