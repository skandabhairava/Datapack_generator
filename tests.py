from src.commandblock_py import Datapack
from src.commandblock_py.commands import commands

mypack = Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")
print(mypack)
mypack.register_function(name="load",content=["say hi!"])
mypack.register_function(name="tickkk",content="say hi!")
mypack.register_function(name="test",content=[commands.say("hello"), commands.say("ad")])
mypack.generate(zip=False)
