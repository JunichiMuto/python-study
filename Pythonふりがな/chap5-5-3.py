# pythonソースからfor/if/elseの出現回数を調べる
from pathlib import Path
terms = {'for':0, 'if':0, 'else':0}
path = Path()
for filepath in path.glob('*.py'):
    rfile = open(filepath, encoding='utf-8')
    text = rfile.read()
    rfile.close()
    for term in terms:
        cnt = text.count(term)
        terms[term] += cnt

print(terms)