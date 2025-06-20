import psycopg2 # type: ignore
from datetime import date
# aqui faz a coneção com o banco
def emitir_mensagens_proximas():
    try: 
        conexao = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="postgres",
            user="postgres",
            password="Anderson@474"
            
        )
        print("Conexão com banco Feita")
        mensagens = []
        cur = conexao.cursor()
        
        # 

        # cur.execute("SELECT paciente, atendimento, medico FROM pacientes;")
        
        #faz uma ponte para executar codigos SQL
        cur = conexao.cursor()
        
        #Faz pegar a data de hoje
        data_hoje = date.today()
        
        cur.execute("""
            SELECT p.nome AS nome_paciente,
                c.data AS data_consulta,
                c.hora AS hora_consulta,
                m.nome AS nome_medico
            FROM consulta c
            JOIN pacientes p ON c.id_paciente = p.id
            JOIN medico m ON c.id_medico = m.id
            WHERE c.data >= %s
            ORDER BY c.data, c.hora
        """, (data_hoje,))
        
        rows = cur.fetchall()

        # print("Toma as tabelas, segura: ")
        # if not rows:
        #     print("⚠️ O Jamal não tem dados no Banco de dado. Ta mais pra banco de nada .")
        
        # else:
        print("Suas consultas proximas: ")
        for row in rows:
            nome = row[0]
            data = row[1].strftime("%d/%m/%Y") #ve se esta certo depois
            hora = row[2].strftime("%H:%M")
            medico = row[3]
                
            mensagem = f"Olá, Sr. {nome}! Informamos que sua consulta será realizada no dia {data} as {hora} com o médico Dr. {medico}."
            mensagens.append(mensagem)

            # print(mensagem)
        
        cur.close()
        conexao.close()
        return mensagens
    except Exception as e:
        print("X Erro em alguma parada ai...")
        print(e)
        return []  # Se ocorrer algum erro ele retorna lista vazia
