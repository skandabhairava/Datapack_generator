from mcdppy import functions, commands, loot_table, create_datapack
project_dir = "src"
class cooldatapack:
    def __init__(self) -> None:
        #this part edits load/tick.json
        functions.loadjson("loadmc")
        functions.tickjson("tickmc")
        loottables = ["op.json"]
        loot_table.create(loottables)
        self.scoreboards = {"aaa":"dummy", "bbb":"dummy"}

    @functions(dir="")
    def loadmc(self):
        commands.say("Datapack Loaded!!")
        commands.runfunction("uninstall")
        commands.scoreboard.initialise(self.scoreboards)
        commands.scoreboard["aaa"] = 0
        commands.scoreboard["bbb"] = 0

    @functions(dir="")
    def tickmc(self,dir=""):
        commands.say("TICK!")
        commands.execute(as_f="@e", at_f="@s", if_f=commands.score.if_c(player="@s", objective="aaa", matches=5), run=commands.loot.spawn(pos="~ ~ ~",source=commands.loot.loot("op")))

    @functions(dir="")
    def uninstall(self,dir=""):
        commands.say("UNINSTALLED!")
        commands.scoreboard.delete_all()

if __name__ == "__main__":
    create_datapack(datapack_template=cooldatapack,project_id="ab",workdir=project_dir,isZipped=False)