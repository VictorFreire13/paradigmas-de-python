class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome (self):
        return self.nome
    
    def get_idade (self):
        return self.idade
    
    def set_nome (self, novo_nome):
        self.nome = novo_nome
        
    def set_idade (self, nova_idade):
        self.idade = nova_idade 
    
pessoa = Pessoa("Victor",18)
print(pessoa.set_nome('Victor'))
print(pessoa.get_nome())