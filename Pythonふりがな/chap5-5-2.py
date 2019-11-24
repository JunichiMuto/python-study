# pythonソースからforの出現回数を調べる
from pathlib import Path
path = Path()
for filepath in path.glob('*.py'):
    rfile = open(filepath, encoding='utf-8')
    text = rfile.read()
    rfile.close()
    cnt = text.count('for')
    print(filepath, cnt)
