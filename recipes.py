from commandblock_py import autofill
from src.commandblock_py.wrapper import *
from src.commandblock_py.commands import basic_commands
from src.commandblock_py.utils.autofill import *
from src.commandblock_py.utils.selectors import selector

from typing import List, Dict, Pattern, Union, Tuple
from colorama import Fore, Style, init
import json, os
init(convert=True) #for colorama windows

curdir = os.getcwd()

def crafting(name:str, layout:Union[Tuple,List], result:str, count:int=1, shaped:bool = True, group:str = ""):
    #print(layout)
    #print(layout[0])
    #print(layout[1])
    #print(layout[2])
    keys = ['#', '@', 'X', 'O', 'Q', 'P', 'J', '%', '$']
    data = {}
    assigned_keys = {}

    if shaped:
        data['type'] = 'minecraft:crafting_shaped'
        on_key = 0
        for i in layout:
            for x in i:
                try:
                    assigned_keys[x]
                except:
                    if x == '' or x == ' ':
                        x = ' '
                        assigned_keys[x] = x
                        on_key += 1
                    else:    
                        assigned_keys[x] = keys[on_key]
                        on_key += 1
                #print(x)
        """print(assigned_keys)
        for h in assigned_keys:
            print(assigned_keys[h]) """
        final_layout = []
        row = 0
        row1 = ""
        row2 = ""
        row3 = ""
        for h in layout:
            row += 1
            for j in h:
                if j == '' or j == ' ':
                    j = ' '

                if row == 1:
                    row1 += assigned_keys[j]

                elif row == 2:
                    row2 += assigned_keys[j]

                elif row == 3:
                    row3 += assigned_keys[j]

        if row1 != '':
            final_layout.append(row1)

        if row2 != '':
            final_layout.append(row2)

        if row3 != '':
            final_layout.append(row3)

        #print(final_layout)

        data['pattern'] = final_layout
        data['key'] = {}

        if ' ' in assigned_keys:
            assigned_keys.pop(' ')
        
        for m in assigned_keys:
            data['key'][assigned_keys[m]] = {}
            data['key'][assigned_keys[m]]['item'] = m

        data['result'] = {}
        data['result']['item'] = result
        data['result']['count'] = count

        if group != '':
            data['group'] = group

        #print(assigned_keys)

    elif shaped == False:
        data['type'] = 'minecraft:crafting_shapeless'

        data['ingredients'] = []
        for i in layout:
            item = {}
            item['item'] = i
            data['ingredients'].append(item)

        data['result'] = result

        if group != '':
            data['group'] = group

    else:
        pass

    with open(f'{name}.json','w') as f:
        json.dump(data, f, indent=4)

def furnace(name:str, input:str, output:str, xp:Union[int,str] = 0.1, time:Union[int,float] = 200, group:str=''):
    data = {}
    data['type'] = 'minecraft:smelting'
    data['ingredient'] = {}
    data['ingredient']['item'] = input
    data['result'] = output
    data['experience'] = xp
    data['cookingtime'] = time
    if group != '':
        data['group'] = group

    with open(f'{name}.json','w') as f:
        json.dump(data, f, indent=4)

def blast_furnace(name:str, input:str, output:str, xp:Union[int,str] = 0.1, time:Union[int,float] = 200, group:str=''):
    data = {}
    data['type'] = 'minecraft:blasting'
    data['ingredient'] = {}
    data['ingredient']['item'] = input
    data['result'] = output
    data['experience'] = xp
    data['cookingtime'] = time
    if group != '':
        data['group'] = group

    with open(f'{name}.json','w') as f:
        json.dump(data, f, indent=4)

def smoker(name:str, input:str, output:str, xp:Union[int,str] = 0.1, time:Union[int,float] = 200, group:str=''):
    data = {}
    data['type'] = 'minecraft:smoking'
    data['ingredient'] = {}
    data['ingredient']['item'] = input
    data['result'] = output
    data['experience'] = xp
    data['cookingtime'] = time
    if group != '':
        data['group'] = group

    with open(f'{name}.json','w') as f:
        json.dump(data, f, indent=4)

def campfire(name:str, input:str, output:str, xp:Union[int,str] = 0.1, time:Union[int,float] = 200, group:str=''):
    data = {}
    data['type'] = 'minecraft:campfire_cooking'
    data['ingredient'] = {}
    data['ingredient']['item'] = input
    data['result'] = output
    data['experience'] = xp
    data['cookingtime'] = time
    if group != '':
        data['group'] = group

    with open(f'{name}.json','w') as f:
        json.dump(data, f, indent=4)
    
def stone_cutter(name:str, input:str, output:str, count:int = 1, group:str=''):
    data = {}
    data['type'] = 'minecraft:campfire_cooking'
    data['ingredient'] = {}
    data['ingredient']['item'] = input
    data['ingredient']['count'] = count
    data['result'] = output
    if group != '':
        data['group'] = group

    with open(f'{name}.json','w') as f:
        json.dump(data, f, indent=4)

def smithing(name:str, base:str, addition:str, output:str, group:str=''):
    data = {}
    data['type'] = 'minecraft:smithing'
    data['base'] = {}
    data['base']['item'] = base
    data['addition'] = {}
    data['addition']['item'] = addition
    data['result'] = {}
    data['result']['item'] = output
    if group != '':
        data['group'] = group

    with open(f'{name}.json','w') as f:
        json.dump(data, f, indent=4)
