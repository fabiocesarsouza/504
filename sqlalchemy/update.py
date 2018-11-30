from sqlalchemy import update
from core import user_table, engine

con = engine.connect()


alt = update(user_table).where(user_table.c.nome == 'teste1')

alt = alt.values(nome='fabio cesar de souza')

print('registro atualizados: ',con.execute(alt).rowcount)

