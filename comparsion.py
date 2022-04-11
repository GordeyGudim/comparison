import filecmp, os
def comparsion():
    files = os.listdir('back')
    files2 = os.listdir('back2')
    listFalse = []
    for f1le in files:
        for f2le in files2:
            if filecmp.cmp(f'back/{f1le}', f'back2/{f2le}', shallow = False):
                None
            else:
                listFalse.append(f2le)
    return(set(listFalse))
