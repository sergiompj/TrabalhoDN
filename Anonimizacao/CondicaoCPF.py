class Cpf:
        def __init__(self, documento) :
            if self.cpf_valido(documento):
                self.cpf = documento
                print("CPF Valido!")
            else:
                raise ValueError("CPF Invalido!")
            
        def cpf_valido(self, documento):
             if len(documento) == 11:
                return True
             else:
                return False