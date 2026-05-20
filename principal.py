import webbrowser

print ("Sistema definição de usuário e senha válidos")
usuario_valido = "Flávio"
senha_valida = "1234"
usuario = input ("Digite o usuario: ")
senha = input ("Digite a senha: ")

if usuario == usuario_valido and senha ==senha_valida:
    print("Login realizado com sucesso!")
    # abre uma página da internet
    webbrowser.open("https:// www.google.com")

else:
    print ("usuário ou senha inválidos.")



