import psycopg2

# aqui faz a coneção com o banco
try: 
    conexao = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Anderson@474"
    )
    print("Conexão com banco Feita")

    cur = conexao.cursor()
    cur.execute("SELECT * FROM pacientes;")
    rows = cur.fetchall()

    print("Toma as tabelas, segura: ")
    for row in rows:
        print(row)
    
    cur.close()
    conexao.close()
    
except Exception as e:
    print("X Erro em alguma parada ai...")
    print(e)

