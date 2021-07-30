# Scripting method documentation

## `def __init__(self, datapack_name :str, namespace_id :str, pack_version :int, loadjson :str, tickjson :str,datapack_description :str = "This datapack was created using commandblock_py") -> None`
Takes the values and initializes the scripting method

Example usage:
```py
mypack = Datapack(datapack_name="commandblockpy_tutorial", namespace_id="hw", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tock")
```

## `def register_function(self,name:str,content:Union[list,str])`
Registers a new function

Example usage:
```py
mypack.register_function(name="tock",content=commands.say("hello world"))
```
or
```py
mypack.register_function(name="tock",content=[commands.say("hello world"),commands.say("hello world 2")])
```

## `def abort(self, rem_datapack:bool, dir:str=curdir)`
Aborts the datapack generation

Example usage:
```py
mypack.abort(rem_datapack=True)
```

## `def generate(self, dir:str=curdir,zip:bool=True,reset_scoreboard:bool=False) -> bool`
Generates the datapack

Example usage:
```py
mypack.generate()
```
