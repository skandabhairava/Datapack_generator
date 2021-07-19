from src.commandblock_py import Datapack
from src.commandblock_py.basic_commands import commands, selectors, autofill

mypack = Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")
print(mypack)
mypack.register_function(name="load",content=["say hi!"])
mypack.register_function(name="tickkk",content="say hi!")
mypack.register_function(name="tickkk",content=[commands.kill(selectors.selector(autofill.ALL_ENTITIES, type=autofill.CREEPER, etcetera_args="limit=5, sort=nearest"))])
mypack.generate(zip=False)
