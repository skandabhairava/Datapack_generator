from src.commandblock_py import Datapack
from src.commandblock_py.basic_commands import commands, scoreboard
from src.commandblock_py.basic_commands.selectors import selector
from src.commandblock_py.autofill import *

mypack = Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")
print(mypack)
print(scoreboard.remove_all())
mypack.register_function(name="load",content=[commands.tellraw(selector=selectors.ALL_PLAYERS,nbt={"text":"DATAPACK LOADED!!"}), commands.function("minecraft:uninstall"), scoreboard.declare(objective="abc"), scoreboard.declare(objective="bbc"), scoreboard.set_val(objective="abc", selector=selectors.ALL_PLAYERS, value=5)])
mypack.register_function(name="tickkk",content="")
mypack.register_function(name="uninstall",content=scoreboard.remove_all())
mypack.generate(zip=False)

#with Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk") as mypack:
#    mypack.register_function(name="load",content=["say hi!"])
#    pp = mypack.register_function(name="pp",content="say hi!")
#    mypack.register_function(name="tickkk",content=[commands.kill(selectors.selector(selectors.ALL_ENTITIES, type=entities.CREEPER, etcetera_args="limit=5, sort=nearest"))])
#    mypack.zip = False