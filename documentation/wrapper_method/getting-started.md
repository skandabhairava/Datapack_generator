# Getting Started

First you need to import the wrapper and commands, add this to the top of your file
```py
from commandblock_py.wrapper import Datapack_wrap
from commandblock_py.basic_commands import commands
```

Next you need to initialize it, add this line of code (you can change some stuff like the name or namespace)

```py
mypack = Datapack_wrap(datapack_name="my_cool_datapack", namespace_id="dp", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tock")
```
Lets first break it down
- `datapack_name` is the datapack name
- `namespace_id` is the namespace
- `pack_version` is the pack format
- `datapack_description` is the datapack description
- `loadjson` and `tickjson` are what the names of the load and tick function should be

Now that we broke it down we can continue to the next part, actually making the functions
Add this to your file
```py
@mypack.new_function('load')
def test(ctx):
    ctx.register(commands.say(content='hi'))
```
Now you could also do
```py
@mypack.new_function('load')
def test(ctx):
    ctx.register('say hi')
```
But for now we are gonna stick to the first one
And repeat the same for the tick file but instead of `load` in `@mypack.new_function('load')` change it with what you put down as your tick file

Lets break this down
- `@mypack.new_function('load')` makes a new function with the name load (which is what we made our load function in the initialization)

- `def test(ctx):` makes a new python function with the context

- and finally `ctx.register(commands.say(content='hi'))` registers a new command, say, with the content `hi`

Now lets add a new function that runs every minecraft tick
```py
@mypack.new_function('tock')
def test2(ctx):
    ctx.register('say hi!')
    ctx.register(commands.say(content='tick tock'))
```

Now that we broke it down, add this to the very end to generate the datapack
```py
if __name__ == "__main__":
    mypack.gen(zip=False)
```
and run it

Now if you did everything correctly you might notice theres an error that says `ERROR : Your Datapack doesn't contain a "load" or a "tock" function or both`, if you have another error check if you did everything correctly

This is because we haven't actually called our python functions, you can call them by adding them above `mypack.gen(zip=False)`

The final code should look something like this
```py
from commandblock_py.wrapper import Datapack_wrap
from commandblock_py.basic_commands import commands

mypack = Datapack_wrap(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tock")

@mypack.new_function('load')
def test(ctx):
    ctx.register(commands.say(content='hi'))

@mypack.new_function('tock')
def test2(ctx):
    ctx.register('say hi!')
    ctx.register(commands.say(content='tick tock'))

if __name__ == "__main__":
    test()
    test2()
    mypack.gen(zip=False)```
