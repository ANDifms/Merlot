from conecaoBD import emitir_mensagens_proximas

mensagens = emitir_mensagens_proximas()

print("Mensagens a serem enviadas: ")
for mensagem in mensagens:
    print(mensagem)
