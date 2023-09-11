import json

class Servico:
  def __init__(self, _id, _descricao, _valor, _duracao):
    self._id = _id
    self._descricao = _descricao
    self._valor = _valor
    self._duracao = _duracao
  def __str__(self):
    return f"{self._id} - {self._descricao} - {self._valor:.2f} - {self._duracao} min"
  def __eq__(self, x):
    if self._id == x._id and self._descricao == x._descricao and self._valor == x._valor and self._duracao == x._duracao:
      return True
    return False
  
class NServico:
  servicos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.servicos:
      if aux._id > id: id = aux._id
    obj._id = id + 1
    cls.servicos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.servicos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.servicos: 
      if obj._id == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj._id)
    cls.servicos.remove(aux)
    cls.servicos.append(obj)
    cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj._id)
    cls.servicos.remove(aux)
    cls.salvar()

  @classmethod
  def abrir(cls):
    cls.servicos = []
    try: 
      with open("servicos.json", mode="r") as arquivo:
        servicos_json = json.load(arquivo)
        for obj in servicos_json:
          servico = Servico(**obj)
          cls.servicos.append(servico)
    except (FileNotFoundError):
      pass      

  @classmethod 
  def salvar(cls):
    with open("servicos.json", mode="w") as arquivo:
      json.dump(cls.servicos, arquivo, default=lambda obj: obj.__dict__)      

