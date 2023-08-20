from models.cliente import Cliente, NCliente

def cliente_listar():
  return NCliente.listar()

def cliente_inserir(nome, email, fone):
  NCliente.inserir(Cliente(nome, email, fone))

def cliente_atualizar(nome, email, fone, id):
  NCliente.atualizar(Cliente(nome, email, fone, id))

def cliente_excluir(id):
  NCliente.excluir(Cliente("", "", "", id))
