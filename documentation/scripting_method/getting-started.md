# Scripting method getting started

First you should import the Scripting/With method and the basic commands
```py
from commandblock_py import Datapack
from commandblock_py.basic_commands import commands
```
Next you should initialize the Scripting Method

```py
mypack = Datapack(datapack_name="commandblockpy_tutorial", namespace_id="hw", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tock")
```
Lets break down what this all means
- `datapack_name="commandblockpy_tutorial"` sets the zip/folder name to `commandblockpy_tutorial`

- `namespace_id="hw"` sets the namespace to `hw`

- `pack_version=7` sets the pack_format to `7`

- `datapack_description="My brand new datapack"` sets the description to `My brand new datapack`

- `loadjson="load"` sets the load function name to `load`

- `tickjson="tock"` sets the tick function name to `tock`

Now lets create a function

First lets make a tick function
```py
mypack.register_function(name="tock",content=commands.say("hello world"))
```
lets see what we just did

`mypack.register_function` is the function to make a new function
it takes
- `name` which we set to `tock` (what we said our tick function name was)

- `content` which we just told it to say `hello world`

Now lets repeat the same but for our load function and change what it says to `new datapack`
```py
mypack.register_function(name="load",content=commands.say("new datapack"))
```

Now that we've registered our tick and load functions we can generate our datapack

We do this by adding these few lines to the end of our file
```py
if __name__ == "__main__":
    mypack.generate(zip=False)
```
If you wanted to generate it as a zip you could remove the `zip=False`

Now when you run the file it should generate a new datapack!
