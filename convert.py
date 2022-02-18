import os

path = os.getcwd()
fname='SuddenPinBox.py'

os.system('jupyter nbconvert --to script SuddenPinBox.ipynb')

with open(fname, 'r') as f:
    lines = f.readlines()
with open(os.path.join(path, 'problem', fname), 'w') as f:
    for line in lines:
        if "get_ipython()" in line:
            continue
        elif 'nbconvert --to script' in line or "from IPython import display" in line:
            break
        else:
            f.write(line)
os.remove(fname)
