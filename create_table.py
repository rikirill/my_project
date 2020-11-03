from easygui import fileopenbox
import random
import math
from graphviz import Digraph as di
from graphviz import nohtml
import numpy as np
import pandas as pn
import time
from tqdm import tqdm



def take_array(table):
    a = pn.read_excel(table)
    team = np.asarray(a)
    team = list(team)
    for i in range(len(team)):
        a = team[i][0].split(' ')
        b = team[i][1].split(' ')
        team[i][0] = ''.join(fr'{x}\n' for x in a)
        team[i][1] = ''.join(fr'{x}\n' for x in b)
    return team

def create_arrays(array):
    Time = len(array)//10
    team = array[:]
    free = True
    circls = []
    first_circle = []
    log = int(math.log(len(team), 2))
    circle = (len(team) - 2 ** log)
    if circle == 0:
        circle = len(team) // 2
        free = False
    while circle != 0:
        first = random.randint(0, len(team) - 1)
        second = random.randint(0, len(team) - 1)
        if team[first][1] != team[second][1]:
            first_circle.append([team[first], team[second]])
            team.pop(first)
            team.pop(second - 1)
            circle -= 1
    circls.append(first_circle)

    if free and len(team) > circle:
        circle = len(first_circle)
        second_circle = []
        while circle != 0:
            third = random.randint(0, len(team) - 1)
            second_circle.append(team[third])
            circle -= 1
            team.pop(third)
    else:
        second_circle = team
        free = False
    circls.append(second_circle)
    if free:
        third_circle = []
        circle = len(team) // 2
        start = time.time()
        end = start + Time
        while circle != 0 and time.time() < end:
            first = random.randint(0, len(team) - 1)
            second = random.randint(0, len(team) - 1)
            if team[first][1] != team[second][1]:
                third_circle.append([team[first], team[second]])
                if first > second:
                    team.pop(second)
                    team.pop(first - 1)
                else:
                    team.pop(first)
                    team.pop(second - 1)
                circle -= 1
        if circle != 0:
            return None
        third_circle += [[x] for x in second_circle]
        circls.append(third_circle)
        return circls

def create_graph (log : int, first_circle: list, second_circle, third_circle = None):
    dot = di('structs', filename='tournament_table',
             node_attr={'shape': 'record'})
    dot.attr(rankdir='LR')

    for i in range(len(first_circle)):
        nd = first_circle[i]
        dot.node(f'0{i}1', nohtml(fr"{{ {str(nd[0][0])} | {str(nd[0][1])} }}"))
        dot.node(f'0{i}2', nohtml(fr'{{ {str(nd[1][0])} | {str(nd[1][1])} }}'))

    if third_circle:
        itt = third_circle
    else:
        itt = second_circle

    c = 0
    for i in range(len(itt)):
        nd = itt[i]
        dot.node(f'1{i}1', nohtml(f'{{ {str(nd[0][0])} | {str(nd[0][1])} }}'))
        if len(nd) > 1:
            dot.node(f'1{i}2', nohtml(f'{{ {str(nd[1][0])} | {str(nd[1][1])} }}'))
        else:
            dot.node(f'1{i}2', nohtml('{ | }'))
            dot.edge(f'0{c}1', f'1{i}2')
            dot.edge(f'0{c}2', f'1{i}2')
            c += 1

    for i in range(len(itt)):
        dot.node(f'2{i}', nohtml('{ | }'))
        dot.edge(f'1{i}1', f'2{i}')
        dot.edge(f'1{i}2', f'2{i}')

    count = len(itt)
    for i in range(log - 1):
        c = 0
        for j in range(count // 2):
            dot.node(f'{i + 3}{j}', nohtml('{ | }'))
            dot.edge(f'{i + 2}{c}', f'{i + 3}{j}')
            dot.edge(f'{i + 2}{c + 1}', f'{i + 3}{j}')
            c += 2
        count = count // 2
    dot.edge_attr.update(arrowsize='0')
    dot.attr(overlap='false')
    dot.view()


def open_table():
    return fileopenbox(filetypes=["*.excel", "*xlsx"])


if __name__ =='__main__':
    print('\nВыберите .excel  файл, для создания турнирной таблицы\n')
    time.sleep(3.2)
    input_f = open_table()
    with tqdm(total= 100) as pbar:
        print('\ncollecting data\n')
        array = take_array(input_f)
        pbar.update(30)
        log = int(math.log(len(array), 2))
        circls = None
        print('\nexpress data\n')
        while not circls:
            circls = create_arrays(array)
        pbar.update(35)
        print('\ncreate tournament table\n')
        if len(circls) == 3:
            create_graph(log= log, first_circle=circls[0], second_circle=circls[1], third_circle=circls[2])
        else:
            create_graph(log, circls[0], circls[1])
        pbar.update(35)
        print('\nsucessful\n')
