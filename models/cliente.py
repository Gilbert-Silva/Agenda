import json
import streamlit as st

class Cliente:
  def __init__(self, _nome, _email, _fone, _id = 0):
    self._nome = _nome
    self._email = _email
    self._fone = _fone
    self._id = _id
  def __str__(self):
    return f"{self._nome} - {self._email} - {self._fone} - {self._id}"
  def __eq__(self, x):
    if self._nome == x._nome and self._email == x._email and self._fone == x._fone and self._id == x._id:
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
    aux._nome = obj._nome
    aux._email = obj._email
    aux._fone = obj._fone
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
          cls.clientes.append(cliente)
    except (FileNotFoundError):
      pass      

  @classmethod 
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls.clientes, arquivo, default=lambda obj: obj.__dict__)      

