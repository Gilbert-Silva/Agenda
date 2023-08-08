import json

class Cliente:
    def __init__(self, _nome, _email, _fone):
        self._nome = _nome
        self._email = _email
        self._fone = _fone
    def __str__(self):
       return f"{self._nome} - {self._email}"
       
class NCliente:
    clientes = []
    @classmethod
    def Inserir(cls, c):
        cls.Abrir()
        cls.clientes.append(c)
        cls.Salvar()
    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.clientes
    @classmethod 
    def Salvar(cls):
      with open("clientes.json", mode="w") as arquivo:
        json.dump(cls.clientes, arquivo, default=lambda obj: obj.__dict__)      
    @classmethod
    def Abrir(cls):
      cls.clientes = []
      try: 
        with open("clientes.json", mode="r") as arquivo:
          clientes_json = json.load(arquivo)
          for obj in clientes_json:
            cliente = Cliente(**obj)
            cls.clientes.append(cliente)
      except (FileNotFoundError):
         pass      