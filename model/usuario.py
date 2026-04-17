from database.conexao import criar_conexao

class Usuario: 
    def __init__(self, usuario:str, senha:str, nome:str):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome

    def cadastrar (self):
        conexao, cursor = criar_conexao()
        cursor.execute("""
                INSERT INTO usuarios (usuario, senha, nome)
                       VALUES (%s, %s, %s);
                       """, [self.usuario,self.senha, self.nome])
        conexao.commit()
        conexao.close()