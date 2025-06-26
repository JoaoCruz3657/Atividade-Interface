from abc import ABC
from abc import abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, email, endereco, telefone):
        self.email = email
        self.endereco = endereco
        self.telefone = telefone
        
    @abstractmethod
    def apresentar(self):
        ...

    @abstractmethod
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, profissao, email, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        super().__init__(email=email, endereco=endereco, telefone=telefone)

    def apresentar(self):
        return f"Olá, eu sou {self.nome}!"
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Profissão: {self.profissao}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):
    def __init__(self, razao_social, nome_fantasia, cnpj, email, endereco, telefone):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, endereco=endereco, telefone=telefone)

    def apresentar(self):
        return f"Olá, somos a empresa {self.nome_fantasia}."
    
    def exibir_dados(self):
        print(f"Razão Social: {self.razao_social}")
        print(f"Nome Fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()
