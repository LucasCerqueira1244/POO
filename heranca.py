class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Matrícula: {self.matricula}")


pessoa1 = Pessoa("João", 30)
estudante1 = Estudante("Maria", 20, "2021001")

pessoa1.exibir_informacoes()  # Exibe informações da pessoa1
print()
estudante1.exibir_informacoes()  # Exibe informações do estudante1
