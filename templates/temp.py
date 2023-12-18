import json
import datetime

class Agenda:
  def __init__(self, id, data, confirmado, id_cliente, id_servico):
    self.__id = id
    self.__data = data
    self.__confirmado = confirmado
    self.__id_cliente = id_cliente
    self.__id_servico = id_servico
  def get_id(self): return self.__id
  def get_data(self): return self.__data
  def get_confirmado(self): return self.__confirmado
  def get_id_cliente(self): return self.__id_cliente
  def get_id_servico(self): return self.__id_servico
  def set_id(self, id): self.__id = id
  def set_data(self, data): self.__data = data
  def set_confirmado(self, confirmado): self.__confirmado = confirmado
  def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
  def set_id_cliente(self, id_servico): self.__id_servico = id_servico
  def __str__(self):
    return f"{self.__id} - {self.__data} - {self.__confirmado}"
  def to_json(self):
    return { '_Agenda__id' : self._id, '_Agenda__data': self._data.strftime('%d/%m/%Y %H:%M'), '_Agenda__confirmado': self._confirmado, '_Agenda__id_cliente' : self._id_cliente, '_Agenda__id_servico' : self._id_servico }


class NAgenda:
  __agendas = []         # lista de agendas inicia vazia
  @classmethod
  def inserir(cls, obj):
    NAgenda.abrir()
    id = 0 # encontrar o maior id já usado
    for agenda in cls.__agendas:
      if agenda.get_id() > id: id = agenda.get_id()
    obj.set_id(id + 1)
    cls.__agendas.append(obj)  # insere um agenda (obj) na lista
    NAgenda.salvar()
  @classmethod
  def listar(cls):
    NAgenda.abrir()    
    return cls.__agendas       # retorna a lista de agendas
  @classmethod
  def listar_id(cls, id):
    NAgenda.abrir()
    for agenda in cls.__agendas:
      if agenda.get_id() == id: return agenda
    return None
  @classmethod
  def atualizar(cls, obj):
    NAgenda.abrir()
    agenda = cls.listar_id(obj.get_id())
    agenda.set_data(obj.get_data())
    agenda.set_confirmado(obj.get_confirmado())
    agenda.set_id_cliente(obj.get_id_cliente())
    agenda.set_id_servico(obj.get_id_servico())
    NAgenda.salvar()
  @classmethod
  def excluir(cls, obj):
    NAgenda.abrir()
    agenda = cls.listar_id(obj.get_id())
    cls.__agendas.remove(agenda)    
    NAgenda.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__agendas = []
      with open("agendas.json", mode="r") as f:
        s = json.load(f)
        for agenda in s:
          c = Agenda(agenda["_Agenda__id"], datetime.datetime.strptime(agenda["_Agenda__data"], "%d/%m/%Y %H:%M"),
                     agenda["_Agenda__confirmado"], agenda["_Agenda__id_cliente"], agenda["_Agenda__id_servico"])
          cls.__agendas.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("agendas.json", mode="w") as f:
      json.dump(cls.__agendas, f, default = Agenda.to_json)
