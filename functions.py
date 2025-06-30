def get_todos(filepath):
    with open(filepath,"r") as f:
       todos_local =  f.readlines()
    return todos_local

def write_todos(filepath,todos_local):
    with open(filepath,"w") as f:
        f.writelines(todos_local)


