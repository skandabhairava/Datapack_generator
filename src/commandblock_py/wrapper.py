from .datapack import DataPack as DP

class DataPack:
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

    def run_every_tick():
        pass