from faker import Faker
from con_mongo import connect

fake = Faker('pt-BR')

db = connect('projeto')

for x in range(100):
    data = {
        "nome": fake.name(),
        "email": fake.email(),
        "cpf": fake.cpf(),
        "nascimento": fake.date_of_birth().strftime('%d-%m-%Y')
    }
    db.usuario.insert(data)