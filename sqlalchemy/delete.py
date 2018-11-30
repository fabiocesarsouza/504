from sqlalchemy import delete
from core import user_table, engine

con = engine.connect()


d = delete(user_table).where(user_table.c.nome == 'teste2')


print('registros apagados: ',con.execute(d).rowcount)