owl_pg_count = {}

def update_status(name, state):
    owl_pg_count[name] = state

def get_status():
    return owl_pg_count