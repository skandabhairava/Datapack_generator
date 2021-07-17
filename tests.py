from src.commandblock_py import Datapack

mypack = Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")
print(mypack)
mypack.register_function(name="load",content="say hi!\nfunction abc:exec")
mypack.register_function(name="tickkk",content="say hi!")
mypack.register_function(name="exec",content="execute as @e[type=minecraft:slime] at @s run say hi!")
mypack.register_function(name="t52est",content="say test")
mypack.register_function(name="test",content="say HAII!!")
mypack.generate(zip=False)