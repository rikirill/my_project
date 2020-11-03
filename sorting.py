import argparse
import os
import sys
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Aaaaaaa tutorial of argparser")
def main(file_path):
    path = [('Документы', 'doc$@$docx$@$pdf$@$exel'), ('Архивы', 'zip$@$rar'), ('Приложения', 'exe$@$php$@$py'),
            ('Изображения', 'png$@$jpg')]

    print(f"the path is '{file_path}'")
    b = {
        "folder": []
    }
    file = os.listdir(file_path)
    for name in file:
        file_name, type = os.path.splitext(name)
        if type == '':
            continue
        else:
            if type in b.keys():
                b[type].append(name)
            else:
                b.update({type: [name]})

    for name in path:
        if name[0] not in file:
            os.mkdir(f'{file_path}\{name[0]}')
    if "Другое" not in  file:
        os.mkdir(f'{file_path}\Другое')

    for type in tqdm(b.keys()):
        for name in path:
            if type[1:] in name[-1].split("$@$"):
                for file_name in b[type]:
                    os.rename(f'{file_path}/{file_name}', f'{file_path}/{name[0]}/{file_name}')
                break
        else:
            for file_name in b[type]:
                os.rename(f'{file_path}/{file_name}', f'{file_path}/Другое/{file_name}')
    pass
    print("\nthe sort is successful\n",)

def enter_path():
    print("\nenter the full path of folder you want to sort\n")
    path = input("the path:")
    if path == "exit":
        exit(0)
    if os.path.exists(path):
        main(path)
    else:
        non_correct_path()


def non_correct_path():
    print(f"\nthe path is not exist, please enter the current path, as like '{sys.argv[0]}'\nif you want to exit enter 'exit'")
    enter_path()


if __name__ =='__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            main(path)
        else:
            non_correct_path()
    else:
        enter_path()