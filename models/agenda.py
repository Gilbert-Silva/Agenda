import json
import datetime
from models.modelo import Modelo

class Agenda:
  def __init__(self, _id, _data, _confirmado, _id_cliente, _id_servico):
    self._id = _id
    self._data = _data
    self._confirmado = _confirmado
    self._id_cliente = _id_cliente
    self._id_servico = _id_servico
  def __str__(self):
    return f"{self._id} - {self._data} - {self._confirmado} - {self._id_cliente} - {self._id_servico}"
  def to_json(self):
    return { '_id' : self._id, '_data': self._data.strftime('%d/%m/%Y %H:%M'), '_confirmado': self._confirmado, '_id_cliente' : self._id_cliente, '_id_servico' : self._id_servico }
  def __eq__(self, x):
    if self._id == x._id and self._data == x._data and self._confirmado == x._confirmado and self._id_cliente == x._id_cliente and self._id_servico == x._id_servico:
      return True
    return False  

class NAgenda(Modelo):
  @classmethod
  def listar_nao_confirmados(cls):
    cls.abrir()
    nao_confirmados = []
    aux = datetime.datetime.now()
    hoje = datetime.datetime(aux.year, aux.month, aux.day)
    for aux in cls.agendas:
      if not aux._confirmado and aux._data > hoje: 
        nao_confirmados.append(aux)
    return nao_confirmados

  @classmethod
  def abrir(cls):
    cls.agendas = []
    try: 
      with open("agendas.json", mode="r") as arquivo:
        agendas_json = json.load(arquivo)
        for obj in agendas_json:
          agenda = Agenda(obj["_id"], datetime.datetime.strptime(obj["_data"], "%d/%m/%Y %H:%M"), obj["_confirmado"], obj["_id_cliente"], obj["_id_servico"])
          cls.agendas.append(agenda)
    except (FileNotFoundError):
      pass      

  @classmethod 
  def salvar(cls):
    with open("agendas.json", mode="w") as arquivo:
      json.dump(cls.agendas, arquivo, default = Agenda.to_json)      


class NAgenda2:
  agendas = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.agendas:
      if aux._id > id: id = aux._id
    obj._id = id + 1
    cls.agendas.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.agendas

  @classmethod
  def listar_nao_confirmados(cls):
    cls.abrir()
    nao_confirmados = []
    aux = datetime.datetime.now()
    hoje = datetime.datetime(aux.year, aux.month, aux.day)
    for aux in cls.agendas:
      if not aux._confirmado and aux._data > hoje: 
        nao_confirmados.append(aux)
    return nao_confirmados

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.agendas: 
      if obj._id == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj._id)
    cls.agendas.remove(aux)
    cls.agendas.append(obj)
    cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj._id)
    cls.agendas.remove(aux)
    cls.salvar()

  @classmethod
  def abrir(cls):
    cls.agendas = []
    try: 
      with open("agendas.json", mode="r") as arquivo:
        agendas_json = json.load(arquivo)
        for obj in agendas_json:
          agenda = Agenda(obj["_id"], datetime.datetime.strptime(obj["_data"], "%d/%m/%Y %H:%M"), obj["_confirmado"], obj["_id_cliente"], obj["_id_servico"])
          cls.agendas.append(agenda)
    except (FileNotFoundError):
      pass      

  @classmethod 
  def salvar(cls):
    with open("agendas.json", mode="w") as arquivo:
      json.dump(cls.agendas, arquivo, default = Agenda.to_json)      

