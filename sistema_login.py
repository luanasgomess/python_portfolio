usuarios = {
    "admin": "1234",
    "Martin": "senha123",
    "Luana": "python123"
}

print("=== Sistema de Login ===")
usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario in usuarios and usuarios[usuario] == senha:
    print("Login bem-sucedido! Bem-vindo,", usuario)
else:
    print("Usuário ou senha incorretos.")