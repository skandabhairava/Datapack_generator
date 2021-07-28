from functools import wraps
from .datapack import Datapack as DP

""" import datapack
DP = datapack.Datapack """

class Datapack_wrap:
    def __init__(self, datapack_name :str, namespace_id :str, pack_version :int, loadjson :str, tickjson :str,datapack_description :str = "This datapack was created using commandblock_py") -> None:
        self.datapack_name = datapack_name
        self.datapack_functions = []
        self.function_lock = 0
        self.loadjson = loadjson
        self.tickjson = tickjson
        self.pack_version = pack_version
        self.namespace_id = namespace_id
        self.datapack_description = datapack_description

        self.data = DP(datapack_name=self.datapack_name,namespace_id=self.namespace_id,pack_version=self.pack_version,loadjson=self.loadjson,tickjson=self.tickjson,datapack_description=self.datapack_description)
        #self.data.gen_dir = os.getcwd()

    def new_function(self, file:str):
        #x = ""
        def inner_function(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                new_context = _context()
                function(new_context, *args, **kwargs)
                #print(function)
                #function.mcfunction = f"{self.namespace_id}:{file}"
                #setattr(function, "__mcfunction__", f"{self.namespace_id}:{file}")
                self.data.register_function(name=file,content=new_context.contents)
                #return function(new_context, *args, **kwargs)
            #print(wrapper)
            wrapper.mcfunction = f"{self.namespace_id}:{file}"
            return wrapper
        #inner_function.__name__ = x
        return inner_function

    def gen(self,zip:bool=True):
        self.data.generate(zip=zip)

    def make_auto_run(self, func):
        func()
        return func


class _context:
    def __init__(self):
        self.contents = ""

    def register(self,content:str):
        #print("hello")
        self.contents += content if content[:-1] == "\n" else content + "\n"
        #self.data.register_function(name = self.filename,content = content)
        #print(self.data.datapack_functions)
