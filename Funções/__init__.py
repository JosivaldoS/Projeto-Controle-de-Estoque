import sqlite3


class Roupa:

    def __init__(self, nome, preco, codigo_de_barra, q_t, q_p, q_m, q_g, q_gg):
        """ Essa classe foi criada no intuito de cadastrar novas roupas e também pq eu tava aprendendo classes
        :param nome: Nome da roupa
        :param preco: Preço da roupa
        :param codigo_de_barra: Código de barras
        :param q_t: Quantidade total
        :param q_p: Quantitade de Tamanhos P
        :param q_m: Quantitade de Tamanhos M
        :param q_g: Quantitade de Tamanhos G
        :param q_gg: Quantitade de Tamanhos GG
        """
        self.nome = nome
        self.preco = preco
        self.barra = codigo_de_barra
        self.q_t = q_t
        self.q_p = q_p
        self.q_m = q_m
        self.q_g = q_g
        self.q_gg = q_gg

    def cadastrar(self):
        """ Cadastra novas peças de roupas no banco de dados
        """
        con = sqlite3.connect("dados.db")
        c = con.cursor()

        c.execute("INSERT INTO produtos VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (self.barra, self.nome, self.preco, self.q_t, self.q_p, self.q_m, self.q_g, self.q_gg))

        con.commit()
        con.close()


def remocaoeadicao(barra, tamanho, quantidade):
    """ Função para remover peças de roupa
    :param barra: Código de barras
    :param quantidade: quantidade a ser retirada/adicionada
    :param tamanho: tamanho da roupa a ser retirada/adicionada
    """

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    if tamanho == 4:
        c.execute(f"UPDATE produtos SET quantidade_p = ? WHERE codigo_de_barra = ?", (quantidade, barra))
    elif tamanho == 5:
        c.execute(f"UPDATE produtos SET quantidade_m = ? WHERE codigo_de_barra = ?", (quantidade, barra))
    elif tamanho == 6:
        c.execute(f"UPDATE produtos SET quantidade_g = ? WHERE codigo_de_barra = ?", (quantidade, barra))
    else:
        c.execute(f"UPDATE produtos SET quantidade_gg = ? WHERE codigo_de_barra = ?", (quantidade, barra))

    con.commit()
    con.close()


def verlista():
    """ Função para ver a lista de produtos
    """
    con = sqlite3.connect("dados.db")
    c = con.cursor()

    print('-'*113)
    print(f'|{"Código de barra":^16}|{"Nome da roupa":^20}|{"Valor":^7}|{"Quantidade Total":^17}|'
          f'{"Tamanhos P":^11}|{"Tamanhos M":^11}|{"Tamanhos G":^11}|{"Tamanhos GG":^11}|')
    # 7
    print('-'*113)

    for lista in c.execute('SELECT * FROM produtos'):
        print(f'|{lista[0]:^16}|{lista[1]:^20}|{lista[2]:^7.2f}|{lista[3]:^17}|{lista[4]:^11}|'
              f'{lista[5]:^11}|{lista[6]:^11}|{lista[7]:^11}|')

    print('-'*113)

    con.close()


def validacao_cdb(codigo):
    """ Função para Validação de código de barras e de quantidade
    :param codigo: Código de barras
    :return: Se achar o código de barras o valor retornado vai ser True
    Se não, o valor retornado vai ser False"""

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    for linha in c.execute("SELECT * FROM produtos"):
        if codigo == linha[0]:
            con.close()
            return True
    con.close()
    return False


def validacao_tr(cb, tam, qp=1, op=1):
    """ Validação da função: tirar roupa. Tem o próposito de validação da quantiade de roupas do tamanho x
    :param tam: Tamanho da roupa
    :param qp: Quantidade de roupas a ser retirado. Como foi adicionado a "op" coloquei o qp também como =1
    :param cb: Código de barras
    :param op: Apenas uma forma que achei para incluir a função na funcionalidade: adicionar quantidade de roupa
    :return: Return True se possuir, False se não possuir.
    """

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    for linha in c.execute("SELECT * FROM produtos"):
        if cb == linha[0]:
            if op == 2:
                con.close()
                return linha[tam]
            if qp <= linha[tam]:
                con.close()
                return True and linha[tam]
    con.close()
    return False
