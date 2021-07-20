from src.commandblock_py import Datapack
from src.commandblock_py.basic_commands import commands
from src.commandblock_py.basic_commands.selectors import selector
from src.commandblock_py.autofill import *

mypack = Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")
print(mypack)
mypack.register_function(name="load",content=["say hi!"])
pp = mypack.register_function(name="hello/pp",content="say hi!")
mypack.register_function(name="tickkk",content=[commands.kill(selector(selectors.ALL_ENTITIES, type=entities.CREEPER, etcetera_args="limit=5, sort=nearest"))])
mypack.register_function(name="load",content=[commands.schedule('function',pp,'100t')])
mypack.register_function(name="test",content=[commands.function(pp)])
mypack.register_function(name='toopee', content=[commands.stopsound(target=selector(selectors.ALL_ENTITIES,distance="..5"), sound_type="*")])
mypack.generate(zip=False)

#with Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk") as mypack:
#    mypack.register_function(name="load",content=["say hi!"])
#    pp = mypack.register_function(name="pp",content="say hi!")
#    mypack.register_function(name="tickkk",content=[commands.kill(selectors.selector(autofill.selectors.ALL_ENTITIES, type=autofill.entities.CREEPER, etcetera_args="limit=5, sort=nearest"))])
#    mypack.zip = False