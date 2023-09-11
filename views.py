from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico

def cliente_listar():
  return NCliente.listar()

def cliente_inserir(nome, email, fone):
  NCliente.inserir(Cliente(0, nome, email, fone))

def cliente_atualizar(id, nome, email, fone):
  NCliente.atualizar(Cliente(id, nome, email, fone))

def cliente_excluir(id):
  NCliente.excluir(Cliente(id, "", "", ""))

def servico_listar():
  return NServico.listar()

def servico_inserir(descricao, valor, duracao):
  NServico.inserir(Servico(0, descricao, valor, duracao))

def servico_atualizar(id, descricao, valor, duracao):
  NServico.atualizar(Servico(id, descricao, valor, duracao))

def servico_excluir(id):
  NServico.excluir(Servico(id, "", "", ""))
