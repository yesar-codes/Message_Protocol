import json

def parse_code(command):
    return json.dumps(command).encode('utf-8')

def unparse_code(command):
    return json.loads(command.decode('utf-8'))