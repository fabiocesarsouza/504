from sqlalchemy import select
from core import user_table

sel = select([user_table]).where(user_table.c.nome == 'fabio')
#c  = coluna

print(list(sel.execute()))

registros = [x for x in sel.execute()]
print(registros)