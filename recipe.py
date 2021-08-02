from commandblock_py import autofill
from src.commandblock_py.wrapper import *
from src.commandblock_py.basic_commands import commands
from src.commandblock_py.autofill import *
from src.commandblock_py.basic_commands.selectors import selector

from typing import List, Dict, Pattern, Union, Tuple
import json

def create(name:str, layout:Union[Tuple,List], result:str, shaped:bool = True, group:str = ""):
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

""" create('test', [
    ('','u','y'),
    ('pp','i','tt'),
    ('u','i','p')
],'h' ) """
create('test', ['g','y','uuuu'], 'x', shaped=False)