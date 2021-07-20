from src.commandblock_py.wrapper import *

mypack = Datapack(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")

@mypack.new_function('pp')
def test(ctx):
    ctx.register('say hi')

mypack.gen(zip=False)