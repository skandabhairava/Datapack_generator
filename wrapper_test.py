from src.commandblock_py.wrapper import *

mypack = Datapack_wrap(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")

@mypack.new_function('load')
def test(ctx):
    ctx.register('say hi')
    #print("hello")

@mypack.new_function('tickkk')
def well(ctx):
    ctx.register('say hi')
    ctx.register('say well hello there')
    #print("there")

test()
well()
mypack.gen(zip=False)