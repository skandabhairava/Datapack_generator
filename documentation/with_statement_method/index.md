# "With" method getting started

First lets import the Scripting/With method and the basic commands
```py
from commandblock_py import Datapack
from commandblock_py.basic_commands import commands
```

Next lets initialize the with method
```py
with Datapack(datapack_name="cool_datapack", namespace_id="with", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tick") as mypack:
```
Lets break this down

- `with Datapack` uses a with statement (which is why its called the with method) and initializes the method

- `datapack_name="cool_datapack"` sets the datapack name to `cool_datapack`

- `namespace_id="with"` sets the namespace to `with`

- `pack_version=7` sets pack format to `7`

- `datapack_description="My brand new datapack"` sets the description to `My brand new datapack`

- `loadjson="load"` sets the load function name to `load`

- `tickjson="tick"` sets the tick function name to `tick`


Next lets actually register a function by putting the following inside the with statement
```py
mypack.register_function(name="load",content=commands.say('hi'))
mypack.register_function(name="tick",content=commands.say('loaded'))
```
Now lets quickly break with down

- `mypack.register_function(name="load",content=commands.say('hi'))` registers a new function with the name load (what we set as our load function) and it says `hi`

- `mypack.register_function(name="tick",content=commands.say('loaded'))` registers a new function with the name tick (what we said as our tick function) and it says `loaded`

Now if you wanted to generate the datapack as a folder instead of a zip add this like to the end of the with statement
```py
mypack.zip = False
```

The code should look something like
```py
from commandblock_py import Datapack
from commandblock_py.basic_commands import commands

with Datapack(datapack_name="cool_datapack", namespace_id="with", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tick") as mypack:
  mypack.register_function(name="load",content=commands.say('hi'))
  mypack.register_function(name="tick",content=commands.say('loaded'))
  mypack.zip = False
```

Now you can run the file and the datapack should generate!
