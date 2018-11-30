from psycopg2 import connect
from faker import Faker

fake = Faker('pt-BR')

con = connect("host=localhost user=python password=4linux dbname=fundamentals")
cur = con.cursor()

for x in range(100):
    cur.execute("insert into usuario (nome, email, cpf, nascimento) \
    values ('{}','{}','{}','{}')".format(fake.name(),fake.email(),fake.cpf(),fake.date_of_birth().strftime('%d-%m-%Y')))
    con.commit()

try:
    cur.close()
    con.close()
except Exception:
    print('Cursor nao definido')
