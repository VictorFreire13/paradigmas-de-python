class Aluno:
    def __init__ (self, nome="", nota1=0.0, nota2=0.0):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def get_nome(self):
        self.__nome = nome
        
    def set_nota1(self, nota):
        self.__nota1 = nota

    def get_nota1(self):
        return self.__nota1

    def set_nota2(self, nota):
        self.__nota2 = nota

    def get_nota2(self):
        return self.__nota2

    
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

    
    def exibir_informacoes(self):
        media = self.calcular_media()
        print(f"Aluno: {self.__nome}")
        print(f"Média: {media:.2f}")



aluno1 = Aluno("Victor", 3.5, 7.0)
aluno1.exibir_informacoes()

aluno2 = Aluno()
aluno2.set_nome("Ana")
aluno2.set_nota1(9)
aluno2.set_nota2(5.5)
aluno2.exibir_informacoes() 