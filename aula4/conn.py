from psycopg2 import connect

try:
    con = connect("host=localhost user=python password=4linux dbname=fundamentals")
    cur = con.cursor()
    # cur.execute("select * from usuario")
    # print(cur.fetchone())
    cur.execute("insert into usuario (nome, email, cpf, nascimento) \
    values ('{}','{}','{}','{}')".format('teste2','teste@teste.com.br','25125225625','17/05/1980'))
    con.commit()
    print(cur.rowncount())

except Exception as e:
    print(e)
    exit()
finally:
    try:
        cur.close()
        con.close()
    except Exception:
        print('Cursor nao definido')
