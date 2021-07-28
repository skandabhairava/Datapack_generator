# Datapack_wrap documentation

## `def __init__(self, datapack_name:str, namespace_id:str, pack_version:int, loadjson:str, tickjson:str, datapack_description:str = "This datapack was created using commandblock_py") -> None`
Takes the values and initializes the wrapper

Example Usage:
```py
mypack = Datapack_wrap(datapack_name="my_cool_datapack", namespace_id="dp", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tock")
```

## `def new_function(self, file:str)`
Registers a new function

Example usage:
```py
@mypack.new_function('load')
```

## `def gen(self, zip:bool=True)`
Generates the datapack

Example usage:
```py
mypack.gen(zip=False)
```

## `def make_auto_run(self, func)`
Makes the fuction automatically at runtime

Example usage:
```py
@mypack.make_auto_run
``` 
