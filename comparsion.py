import filecmp, os
def comparsion():
    files = os.listdir('back')
    files2 = os.listdir('back2')
    listTrue = []
    listFalse = []
    for f1le in files:
        for f2le in files2:
            if filecmp.cmp(f'back/{f1le}', f'back2/{f2le}', shallow = False):
                listTrue.append(f'{f1le}=={f2le}')
            else:
                listFalse.append(f'{f1le}!=={f2le}')
    if len(listTrue) != 0:
        print('True:')
        for truefile in listTrue:
            print(f'\t{truefile}')
    else:
        print('True:\n\tNone')
    if len(listFalse) != 0:
        print('False:')
        for falsefile in listFalse:
            print(f'\t{falsefile}')
    else:
        print('False:\n\tNone')

