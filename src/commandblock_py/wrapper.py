from functools import wraps
from typing import Union
from .datapack import Datapack as DP

""" import datapack
DP = datapack.Datapack """

class Datapack:
    def __init__(self, datapack_name :str, namespace_id :str, pack_version :int, loadjson :str, tickjson :str,datapack_description :str = "This datapack was created using commandblock_py") -> None:
        self.datapack_name = datapack_name
        self.datapack_functions = []
        self.function_lock = 0
        self.loadjson = loadjson
        self.tickjson = tickjson
        self.pack_version = pack_version
        self.namespace_id = namespace_id
        self.datapack_description = datapack_description

        DP(self.datapack_name, self.namespace_id, self.pack_version, self.loadjson, self.tickjson, self.datapack_description)

    def new_function(self, file:str):
        def inner_function(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                function(context(dp = DP,filename=file), *args, **kwargs)
            return wrapper
        return inner_function

    def gen(self,zip:bool=True):
        DP.generate(self, zip=zip)


class context:
    def __init__(self, DP, filename:str):
        self.filename = filename
        self.data = DP

    def register(self,content:Union[list,str]):
        self.data.register_function(name = self.filename,content = content)

    


