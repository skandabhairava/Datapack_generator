from src.commandblock_py import Datapack
from src.commandblock_py.commands import scoreboard
from src.commandblock_py.commands import basic_commands as commands
from src.commandblock_py.utils.selectors import selector
from src.commandblock_py.utils import exec_commands
from src.commandblock_py.utils.autofill import *

mypack = Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")
print(mypack)
print(scoreboard.remove_all())
mypack.register_function(name="load",content=[commands.tellraw(selector=selectors_list.ALL_PLAYERS,nbt={"text":"DATAPACK LOADED!!"}), commands.function("minecraft:uninstall"), scoreboard.declare(objective="abc"), scoreboard.declare(objective="bbc"), scoreboard.set_val(objective="abc", selector=selectors_list.ALL_PLAYERS, value=5)])
mypack.register_function(name="tickkk",content=commands.execute(check=[exec_commands.as_cmd(selector("@e", type=entities_list.SHEEP)), exec_commands.align("xy"), exec_commands.facing(("~", "~", "~")), exec_commands.in_dim("minecraft:overworld"), exec_commands.positioned(selector="@s"), exec_commands.rotated((14.5, 2)), exec_commands.if_unless_block("if", (5, 6, 8), blocks_list.STONE)], run=commands.say("hello!")))
#mypack.register_function(name="stuff",content=[commands.execute(check=[cmd.align("xz"), cmd.anchored("feet"), cmd.as(selector="@e"), cmd.at(selector="@s"), cmd.facing(pos=("1", "2", "3")), cmd.facing(entity="minecraft:creeper",anchor="feet"), cmd.in(dimension="minecraft:overworld"), cmd.positioned(pos=("1", "2", "3")), cmd.positioned(as_selector="@s"), cmd.rotated("""SAME AS POSITIONED""")], run=commands.say("hi!"))])
mypack.register_function(name="uninstall",content=scoreboard.remove_all())
mypack.generate(zip=False)

#with Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk") as mypack:
#    mypack.register_function(name="load",content=["say hi!"])
#    pp = mypack.register_function(name="pp",content="say hi!")
#    mypack.register_function(name="tickkk",content=[commands.kill(selectors.selector(selectors_list.ALL_ENTITIES, type=entities_list.CREEPER, etcetera_args="limit=5, sort=nearest"))])
#    mypack.zip = False