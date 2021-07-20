from src.commandblock_py.wrapper import *

mypack = Datapack_wrap(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")

@mypack.make_auto_run
@mypack.new_function('load')
def test(ctx):
    ctx.register('say hi')
    #print("hello")

@mypack.make_auto_run
@mypack.new_function('tickkk')
def test2(ctx):
    ctx.register('say hi')

""" test()
test2() """

mypack.gen(zip=False)