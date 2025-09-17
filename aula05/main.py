class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus


class Vendedor(Empregado):
    def __init__(self, nome, salario_base, vendas, percentual_comissao):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.percentual_comissao = percentual_comissao  

    def calcular_salario(self):
        comissao = self.vendas * self.percentual_comissao
        return self.salario_base + comissao

gerente = Gerente("Alice", 5000, 1500) 
vendedor = Vendedor("Bob", 3000, 30000, 0.05)  


print(f"Salário do gerente {gerente.nome}: R$ {gerente.calcular_salario()}")
print(f"Salário do vendedor {vendedor.nome}: R$ {vendedor.calcular_salario()}")
