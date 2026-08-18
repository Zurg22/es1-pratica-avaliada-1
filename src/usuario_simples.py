import hashlib


class Usuario:
    """Representa um usuário do sistema."""

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)

    def _hash_senha(self, senha: str) -> str:
        """Gera o hash da senha."""
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        """Verifica se a senha informada está correta."""
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    """Gerencia os usuários cadastrados."""

    def __init__(self):
        self.usuarios = []

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """Cadastra um novo usuário."""
        for usuario in self.usuarios:
            if usuario.email == email:
                raise ValueError("Email já cadastrado")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)

        return usuario

    def fazer_login(self, email: str, senha: str):
        """Realiza o login verificando email e senha."""
        for usuario in self.usuarios:
            if usuario.email == email and usuario.validar_senha(senha):
                return usuario

        return None

    def listar_todos(self):
        """Retorna todos os usuários cadastrados."""
        return self.usuarios