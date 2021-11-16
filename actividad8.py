import json

def store(var, filename):
    json.dump(json.dumps(var), open(filename, 'w')) #json sirve para no tener que ir linea a linea y escribe en disco

def retrieve(filename):
    var = json.loads(json.load(open(filename,'r')))
    return var