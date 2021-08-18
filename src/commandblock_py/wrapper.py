from functools import wraps
from .datapack import Datapack as DP
from colorama import Fore, Style, init
import inspect
init(convert=True)

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

    def new_function(self, dir:str = "", namespace:str = ''):
        #x = ""
        def inner_function(function):
            file = function.__name__

            dir2 = dir

            if dir != '':
                if dir[-1] != '/' or dir[-1] != "\\":
                    dir2 += '/'

            dir2 += file

            #print(dir2)
            """ frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            filename = frame[0].f_code.co_filename
            print(filename) """

            function.mcfunction = f'{self.namespace_id}:{dir2}'
            @wraps(function)
            def wrapper(*args, **kwargs):
                new_context = _context()
                function(new_context, *args, **kwargs)
                self.data.register_function(name=dir2,content=new_context.contents, namespace=namespace)
            wrapper.mcfunction = f"{self.namespace_id}:{dir2}"
            return wrapper
        #inner_function.__name__ = x
        return inner_function

    def gen(self,zip:bool=True):
        self.data.generate(zip=zip)

    def make_auto_run(self, func):
        #print(f'{Fore.YELLOW}WARNING : The make_auto_run wrapper is deprecated so it may cause some things to be incompatible{Style.RESET_ALL}')
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
