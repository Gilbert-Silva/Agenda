import json

class Cliente:
  def __init__(self, _id, _nome, _email, _fone):
    self._id = _id
    self._nome = _nome
    self._email = _email
    self._fone = _fone
  def __str__(self):
    return f"{self._id} - {self._nome} - {self._email} - {self._fone}"
  def __eq__(self, x):
    if self._id == x._id and self._nome == x._nome and self._email == x._email and self._fone == x._fone:
      return True
    return False  
       
class NCliente:
  clientes = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.clientes:
      if aux._id > id: id = aux._id
    obj._id = id + 1
    cls.clientes.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.clientes

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.clientes: 
      if obj._id == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj._id)
    cls.clientes.remove(aux)
    cls.clientes.append(obj)
    cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj._id)
    cls.clientes.remove(aux)
    cls.salvar()

  @classmethod
  def abrir(cls):
    cls.clientes = []
    try: 
      with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          cliente = Cliente(**obj)
          cliente = Cliente(obj["_id"], obj["_nome"], obj["_email"], obj["_fone"])
          cls.clientes.append(cliente)
    except (FileNotFoundError):
      pass      

  @classmethod 
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls.clientes, arquivo, default=lambda obj: obj.__dict__)      

