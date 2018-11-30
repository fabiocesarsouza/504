from core import user_table, engine

con = engine.connect()
# ins = user_table.insert()

# new = ins.values(nome='fabio', idade=24, senha='4linuuxx')

con.execute(user_table.insert(), [
    {'nome': 'teste1', 'idade': 18, 'senha': '4linux'},
    {'nome': 'teste2', 'idade': 18, 'senha': '4linux'},
    {'nome': 'teste3', 'idade': 18, 'senha': '4linux'},
    {'nome': 'teste4', 'idade': 18, 'senha': '4linux'},
    {'nome': 'teste5', 'idade': 18, 'senha': '4linux'},
    {'nome': 'teste6', 'idade': 18, 'senha': '4linux'},
])