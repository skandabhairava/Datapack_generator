from src.commandblock_py.wrapper import *
from src.commandblock_py.basic_commands import commands

mypack = Datapack_wrap(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")

#@mypack.make_auto_run
@mypack.new_function('load')
def test(ctx):
    ctx.register('say hi')
    #print("hello")


#@mypack.make_auto_run
@mypack.new_function('tickkk')
def test2(ctx):
    ctx.register('say hi')

@mypack.new_function('p')
def test3(ctx):
    ctx.register(commands.function(test2))

@mypack.new_function('h')
def test4(ctx):
    ctx.register(commands.function('h:h'))

print(test)
print(test2)

test.__name__ ='pp'
print(test.__name__)
print(test.mcfunction)
print(test2.mcfunction)

print(callable(test))
print(callable(test()))

if __name__ == "__main__":
    test()
    test2()
    test3()
    test4()
    mypack.gen(zip=False)