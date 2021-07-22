from distutils.dir_util import copy_tree
import re, sys, os, shutil, time
from typing import Union
from colorama import Fore, Style, init
from .bar import printProgressBar

init(convert=True) #for colorama windows

curdir = os.getcwd()

class Datapack:
    def __init__(self, datapack_name :str, namespace_id :str, pack_version :int, loadjson :str, tickjson :str,datapack_description :str = "This datapack was created using commandblock_py") -> None:
        """
        datapack_name:str -> This represents the project name / datapack name
        namespace_id:str -> This represents the id given while making a datapack (usually 2-5 chars). This id is used to call functions and other objects from the datapack
        pack_version:int -> This represents the pack version. Its written in the mcmeta file
        loadjson:str -> This represents the mcfunction that will be run at the start of the datapack
        tickjson:str -> This represents the mcfunction that will be run at each tick, when the datapack is enabled
        datapack_description:str -> This represents the description of the datapack. Its written in the mcmeta file

        example : 
            Datapack("cool_datapack", "abc", 7, "load", "tick", "This is a cool datapack")
        """
        ##############################
        ##  DATAPACK INITIALISATION
        ##############################
        self.datapack_name = datapack_name
        self.datapack_functions = []
        self.function_lock = 0
        self.loadjson = loadjson
        self.tickjson = tickjson
        self.pack_version = pack_version
        self.namespace_id = namespace_id
        self.datapack_description = datapack_description
        if (not bool(re.match('^[a-z_]+$', self.datapack_name))) or (not bool(re.match('^[a-z]+$', self.namespace_id))):
            print(f"{Fore.RED}ERROR : The datapack_name/namespace_id must only contain characters from [a-z]{Style.RESET_ALL}")
            sys.exit(-1)
        if len(self.namespace_id) > 5:
            print(f"{Fore.YELLOW}WARNING : The name space id given (\"{self.namespace_id}\") is longer than 5 characters\n          Datapacks are *usually* made with 2-4 namespace characters\n          Nothing will be changed in the datapack{Style.RESET_ALL}")

        if self.pack_version < 4:
            print(f"{Fore.YELLOW}WARNING : The pack version given (\"{self.pack_version}\") is less than 4. This may cause errors in the datapack{Style.RESET_ALL}")

        try:
            try:
                os.makedirs(f"{curdir}/.temp")
            except Exception:
                shutil.rmtree(f"{curdir}/.temp")
                os.makedirs(f"{curdir}/.temp")
        except Exception as e:
            print(f"{Fore.RED}ERROR : Oh-oh! An Exception occured while generating a temporary folder at dir \"{curdir}\": {e}{Style.RESET_ALL}")

        self.gen_dir = curdir
        self.zip = True
        self.del_scoreboard = False
    def __repr__(self) -> str:
        """
        returns the name of the datapack
        """
        return self.datapack_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.generate(self.gen_dir,self.zip,self.del_scoreboard)
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')

    def register_function(self,name:str,content:Union[list,str]):
        """
        name:str -> Holds the name of the function (without namespace)
        content:str -> Holds the content of the function

        returns True if a function has been generated

        example : 
            register_function(name="load",content="say loaded!")
        """
        ##############################
        ## REGISTERING A DATAPACK FUNCTION
        ##############################
        if (not bool(re.match('^[a-z/]+$', name))):
            print(f"{Fore.RED}ERROR : The function name must only contain characters from [a-z] : {name}{Style.RESET_ALL}")
            self.abort(rem_datapack=False)

        if name == self.loadjson or name == self.tickjson:
            self.function_lock += 1

        if name in self.datapack_functions:
            print(f"{Fore.YELLOW}WARNING : A function with this name (\"{name}\") already exists. Replacing the function with new content{Style.RESET_ALL}")

        try:
            ctx=""
            if isinstance(content, list):
                for element in content:
                    ctx += element if element[-1] == "\n" else element + "\n"
            else:
                ctx += content

            os.makedirs(f"{curdir}/.temp/{os.path.dirname(name)}", exist_ok=True)
            with open(f"{curdir}/.temp/{name}.mcfunction", "w") as func:
                func.write(ctx)
            self.datapack_functions.append(name)
            return f"{self.namespace_id}:{name}"
        except Exception as e:
            print(f"{Fore.RED}ERROR : Oh-oh! An Exception occured while registering function \"{name}\" : {e}{Style.RESET_ALL}")
            self.abort(False)

    def abort(self, rem_datapack:bool, dir:str=curdir):
        """
        dir:str -> This is where the datapack is generated in
        Stops all process and deletes all files related to the datapack
        """
        ##############################
        ##  ABORTING THE DATAPACK GENERATION
        ##############################
        print(f"\n\n{Fore.RED}##############################\nABORTING THE DATAPACK GENERATION\n##############################\n\n\n")
        if rem_datapack and os.path.isdir(f"{dir}/{self.datapack_name}"):
            shutil.rmtree(f"{dir}/{self.datapack_name}")
            print("Removed Main Datapack folder")
        if os.path.isdir(f"{curdir}/.temp"):
            shutil.rmtree(f"{curdir}/.temp")
            print("Removed temp folder")
        print(f"Finished removing datapack related files. Shutting down system{Style.RESET_ALL}")
        sys.exit(-1)

    def private_json_value(self, load:bool) -> str:
        value = """{{
    "values":[
        "{0}:{1}"
    ]
}}"""
        value = value.format(self.namespace_id, self.loadjson) if load else value.format(self.namespace_id, self.tickjson)
        return value

    def generate(self, dir:str=curdir,zip:bool=True,reset_scoreboard:bool=False) -> bool:
        """
        dir:str -> This is where the datapack is generated in
        zip:bool -> If True, it compiles the datapack into a .zip file; If False, the datapack remains as a folder
        reset_scoreboard:bool -> checks the parent folder of dir for a "data" folder, and also checks if a file called "scoreboard.dat" exists in the data folder. If yes, it erases those files.
                                 This can be good while testing your datapacks, if your datapack contains a lot of scoreboards

        returns True if the datapack has generated properly
        """
        ##############################
        ##  GENERATING THE DATAPACK
        ##############################

        ## CHECKING IF {LOAD} AND {TICK} MCFUNCTIONS EXIST

        print(f"{Fore.CYAN}This datapack generator is still in its Beta stages. If You find any bugs, please send a screenshot of the terminal to \"Terroid#0490\" or \"Anthony2be#1900\" on Discord{Style.RESET_ALL}")
        if self.function_lock < 2:
            print(f"{Fore.RED}ERROR : Your Datapack doesn't contain a \"{self.loadjson}\" or a \"{self.tickjson}\" function or both")
            self.abort(rem_datapack=False)

        ## MAKING DATAPACK DIRECTORY

        try:
            try:
                os.makedirs(f"{dir}/{self.datapack_name}")
            except Exception:
                print(f"{Fore.YELLOW}WARNING : A folder with this name already exists. This action is going to replace the old datapack folder{Style.RESET_ALL}")
                shutil.rmtree(f"{dir}/{self.datapack_name}")
                os.makedirs(f"{dir}/{self.datapack_name}")
        except Exception as e:
            print(f"{Fore.RED}ERROR : Oh-oh! An Exception occured while deleting a previous file during generation : {e}{Style.RESET_ALL}")
            self.abort(rem_datapack=False)
        
        ## GENERATING DATAPACK TEMPLATE

        try:
            os.makedirs(f"{dir}/{self.datapack_name}/data/minecraft/tags/functions")
            os.makedirs(f"{dir}/{self.datapack_name}/data/{self.namespace_id}/functions")
            print(f"{Fore.GREEN}SUCCESS : The datapack-template has been generated at \"{dir}\"!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}ERROR : Oh-oh! An Exception occured while generating the template of the datapack : {e}{Style.RESET_ALL}")
            self.abort(rem_datapack=True, dir=dir)

        ## GENERATING MC-FUNCTIONS

        print(f"{Fore.GREEN}Generating function files...{Style.RESET_ALL}")

        try:

            ## LOAD AND TICK JSON AND MCMETA

            with (open(f"{dir}/{self.datapack_name}/data/minecraft/tags/functions/load.json", "w") as load_json,
                  open(f"{dir}/{self.datapack_name}/data/minecraft/tags/functions/tick.json", "w") as tick_json,
                  open(f"{dir}/{self.datapack_name}/pack.mcmeta", "w") as mcmeta):
                load_json.write(self.private_json_value(True))
                tick_json.write(self.private_json_value(False))
                value = f"""{{
    "pack": {{
        "pack_format": {self.pack_version},
        "description": \"{self.datapack_description}\"
    }}
}}"""
                mcmeta.write(value)
            ## MCFUNCTIONS

            #printProgressBar(0, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
            files=os.listdir(f"{curdir}/.temp")
            #for fname in files:
                # copying the files to the 
                # destination directory
                #shutil.copy2(os.path.join(f"{curdir}/.temp",fname), f"{dir}/{self.datapack_name}/data/{self.namespace_id}/functions")
            copy_tree(os.path.join(f"{curdir}/.temp"), f"{dir}/{self.datapack_name}/data/{self.namespace_id}/functions")
            l = len(self.datapack_functions)
            printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            for i in range(l):
                # Do stuff...
                time.sleep(0.1)
                # Update Progress Bar
                printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

            print(f"{Fore.GREEN}SUCCESS : The datapack \"{self.datapack_name}\" has been generated at \"{dir}\"!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}ERROR : Oh-oh! An Exception occured while generating the datapack : {e}{Style.RESET_ALL}")
            self.abort(rem_datapack=True, dir=dir)
        shutil.rmtree(f"{curdir}/.temp")

        ## COMPILING DATAPACK IF NEEDED

        if zip:
            try:
                shutil.make_archive(f"{dir}/{self.datapack_name}", 'zip', f"{dir}/{self.datapack_name}")
                shutil.rmtree(f"{dir}/{self.datapack_name}")
                print(f"\n\n{Fore.GREEN}SUCCESS : The datapack has been compiled to a .zip file. \"{dir}\"{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}ERROR : Oh-oh! An Exception occured while compiling the datapack into a .zip : {e}{Style.RESET_ALL}")
                sys.exit(-1)

        ## REMOVING SCOREBOARD.DAT FILE

        if reset_scoreboard:
            try:
                scoreboard_path = dir[:dir.rfind("\\")] + "/data"
                file_exist = os.path.exists(f"{scoreboard_path}/scoreboard.dat")
                if file_exist:
                    os.remove(f"{scoreboard_path}/scoreboard.dat")
                    print(f"{Fore.GREEN}SUCCESS : scoreboard.dat file has been removed{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}WARNING : A scoreboard.dat file doesnt exist{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}ERROR : Oh-oh! an Exception occured while deleting the scoreboard.dat file : {e}{Style.RESET_ALL}")

        return True