import Funções
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIntValidator, QDoubleValidator
import uic2


def filtrar():
    # pro.verestoquetabela.
    if pro.cdbradio.isChecked():
        id = str(pro.identificador.text()).strip()
        # QtWidgets.QMessageBox.about(pro, 'Erro', 'Insira um código de barras válido')
        # Transformo todos os números inteiros para str, para facilitar na busca de elementos
        if id == '':
            QtWidgets.QMessageBox.about(pro, 'Erro', 'Digite algo')
        else:
            dados = Funções.pegartodos(cdb=1)
            dados2 = []
            for c in range(0, len(dados)):
                a = str(dados[c])
                if id in a:
                    print(f'Tem aqui no {a} este é o id -> {id}')
                    dados2.append(a)
            print(dados, dados2)
            for c in range(0, len(dados2)):
                Funções.pegartodos()

    elif pro.nomeradio.isChecked():
        id = str(pro.identificador.text())
        print(id)

    else:
        QtWidgets.QMessageBox.about(pro, 'Erro', 'Selecione um filtro')


def excluir():
    from PyQt5.QtWidgets import QMessageBox
    try:
        int(pro.cdb_add.text())
        cdb = int(pro.cdb.text())
    except ValueError:
        QMessageBox.about(pro, 'Erro', 'Insira um código de barras primeiro!')
    else:
        pass
        descricao = pro.descricao.text()
        msg = QMessageBox()
        msg.setWindowTitle('Excluir')
        msg.setText(f'Você tem certeza que deseja excluir "{descricao}"?')
        msg.setIcon(QMessageBox.Question)
        msg.setInformativeText('Yes para confirmar e excluir, Cancel para cancelar')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)

        x = msg.exec_()
        if x == QMessageBox.Yes:
            # Se o usuário pressionar o botão 'Yes'
            if Funções.validacao_cdb(cdb):
                Funções.deletar(cdb)
                QMessageBox.about(pro, 'Sucesso', f'{descricao} Apagado com sucesso!')
                Funções.adicionarhistorico(cdb, descricao, f'{descricao} Excluída', 'Excluiu')
            else:
                QMessageBox.about(pro, 'Ops', 'Tem certeza que existe esse banco de dados?')

        elif x == QMessageBox.Cancel:
            # Se o usuário pressionar o botão 'Cancel'
            print('Cancelado')
        else:
            print('Nenhum dos dois ué')


def habilitar(op):
    """
    Função para habilitar ou desabilitar as lineedit do "janela 2"
    :param op = opção desejada se for 1 ele vai habilitar tudo, se for 0 ele vai desabilitar
    """
    if op == 1:
        pro.cdb.setEnabled(True)
        pro.descricao.setEnabled(True)
        pro.valor.setEnabled(True)
        pro.tipotamanho.setEnabled(True)
        pro.xtamanho1.setEnabled(True)
        pro.xtamanho2.setEnabled(True)
        pro.xtamanho3.setEnabled(True)
        pro.xtamanho4.setEnabled(True)
        pro.xtamanho5.setEnabled(True)
        pro.xtamanho6.setEnabled(True)
    else:
        pro.cdb.setEnabled(False)
        pro.descricao.setEnabled(False)
        pro.valor.setEnabled(False)
        pro.tipotamanho.setEnabled(False)
        pro.xtamanho1.setEnabled(False)
        pro.xtamanho2.setEnabled(False)
        pro.xtamanho3.setEnabled(False)
        pro.xtamanho4.setEnabled(False)
        pro.xtamanho5.setEnabled(False)
        pro.xtamanho6.setEnabled(False)


def limparjanela2():
    """
    Função para limpar todos os dados do frama chamado "janela 2"
    """
    pro.cdb.clear()
    pro.descricao.clear()
    pro.valor.clear()
    pro.xtamanho1.clear()
    pro.xtamanho2.clear()
    pro.xtamanho3.clear()
    pro.xtamanho4.clear()
    pro.xtamanho5.clear()
    pro.xtamanho6.clear()


def novocadastro():
    # Função para habilitar as funções de cadastro

    pro.atualizar.hide()
    pro.cadastrar.show()

    habilitar(1)
    limparjanela2()


def cadastrar():
    # Função para cadastrar novos produtos
    try:
        cdb = int(pro.cdb.text())
    except ValueError:
        QtWidgets.QMessageBox.about(pro, 'Erro', 'Insira um código de barras primeiro')
    else:
        pass

        x = Funções.validacao_cdb(cdb)
        if x:
            QtWidgets.QMessageBox.about(pro, 'Algo deu errado', 'Este código de barras já existe')

        else:
            descricao = pro.descricao.text()
            valor = float(pro.valor.text())
            op = pro.tipotamanho.currentIndex()
            q_1 = int(pro.xtamanho1.text())
            q_2 = int(pro.xtamanho2.text())
            q_3 = int(pro.xtamanho3.text())
            q_4 = int(pro.xtamanho4.text())
            q_5 = int(pro.xtamanho5.text())
            if op == 0:
                q_t = q_1 + q_2 + q_3 + q_4 + q_5
                Funções.cadastrar(cdb, descricao, valor, q_t, q_1, q_2, q_3, q_4, q_5, op)
                Funções.adicionarhistorico(cdb, descricao,
                                           f'{q_1} Tamanhos U, {q_2} Tamanhos P, {q_3} Tamanhos M, {q_4} Tamanhos G, '
                                           f'{q_5} Tamanhos GG', 'Novo Cadastro', 0)
            else:
                q_6 = int(pro.xtamanho6.text())
                q_t = q_1 + q_2 + q_3 + q_4 + q_5 + q_6
                Funções.adicionarhistorico(cdb, descricao, f'{q_1} Tamanhos 36, {q_2} Tamanhos 38, {q_3} Tamanhos 40, '
                                                           f'{q_4} Tamanhos 42, {q_5} Tamanhos 44, {q_6} Tamanhos 46',
                                           'Novo Cadastro', 0)
                Funções.cadastrar(cdb, descricao, valor, q_t, q_1, q_2, q_3, q_4, q_5, op, q_6)
            # Mensagem que deu tudo certo
            QtWidgets.QMessageBox.about(pro, 'Sucesso', f'A peça {descricao} foi cadastrada com sucesso!')


def editar():
    # Função para habilitar as edições de peças
    try:
        int(pro.cdb_add.text())
        int(pro.cdb.text())
    except ValueError:
        QtWidgets.QMessageBox.about(pro, 'Erro', 'Insira um código de barras primeiro!')
    else:
        pass
        pro.cadastrar.hide()
        pro.atualizar.show()
        habilitar(1)
        pro.cdb.setEnabled(False)
        pro.tipotamanho.setEnabled(False)


def atualizar():
    """ Função para atualizar dados no banco de dados
    Os dados editáveis são os -> Descrição, Valor, Quantidade total e Todos os xtamanhos
    Os dados não editáveis são os -> Código de barras e Tipo de Tamanho"""
    cdb = int(pro.cdb.text())
    descricao = pro.descricao.text()
    valor = float(pro.valor.text())
    q_1 = int(pro.xtamanho1.text())
    q_2 = int(pro.xtamanho2.text())
    q_3 = int(pro.xtamanho3.text())
    q_4 = int(pro.xtamanho4.text())
    q_5 = int(pro.xtamanho5.text())
    try:
        q_6 = int(pro.xtamanho6.text())
    except ValueError:
        q_6 = 0
    q_t = q_1 + q_2 + q_3 + q_4 + q_5 + q_6
    op = Funções.pegarvalor(cdb, op=1)
    # ou -> op = pro.tipotamanho.currentIndex()
    antigo = Funções.pegarvalor(cdb, todos=1)
    if antigo[-1] == 1:
        del antigo[3:8]
        novo = [descricao, valor, q_t, q_1, q_2, q_3, q_4, q_5, q_6, op[0]]
        dic = ['Descrição', 'Valor', 'Quantidade total', 'Tamanhos 36', 'Tamanhos 38', 'Tamanhos 40', 'Tamanhos 42',
               'Tamanhos 44', 'Tamanhos 46']
    else:
        # op = 0
        # ['Vestido Drills ', 49.9, 16, 3, 3, 3, 2, 5, 0, 0, 0, 0, 0, 0, 0]
        # 8:14
        # ['Vestido Drills ', 49.9, 16, 3, 3, 3, 2, 5, 0]
        del antigo[8:14]
        novo = [descricao, valor, q_t, q_1, q_2, q_3, q_4, q_5, op[0]]
        dic = ['Descrição', 'Valor', 'Quantidade total', 'Tamanhos U', 'Tamanhos P', 'Tamanhos M', 'Tamanhos G',
               'Tamanhos GG']

    # situacao vai ser o valor passado ao adicionarhistorico() e nele irá conter o dic (Para especificar qual o objeto
    # está sendo mudado) e os valores antigos para os novos
    situacao = []
    # Detecção de mudanças
    for x in range(0, 9):
        if novo[x] != antigo[x]:
            situacao.append(f'{dic[x]} mudou de {antigo[x]} para {novo[x]}')

    # Irá criar a frase para o adicionarhistorico()
    frase = ''
    for c in range(0, len(situacao)):
        if c == 0:
            frase = situacao[c]
        else:
            frase = frase + ' , ' + situacao[c]

    if not situacao:
        QtWidgets.QMessageBox.about(pro, 'Erro', 'Não houve mudança, tente novamente.')
    else:
        Funções.remocaoeadicao(cdb, op, q_t, q_1, q_2, q_3, q_4, q_5, q_6, descricao, valor)
        if op[0] == 0:
            Funções.adicionarhistorico(cdb, descricao, frase, 'Mudança')
        else:
            Funções.adicionarhistorico(cdb, descricao, frase, 'Mudança')
        QtWidgets.QMessageBox.about(pro, 'Sucesso', 'Peça editada com sucesso')


def mudoucombobox():
    op = pro.tipotamanho.currentIndex()
    # Tamanho bermuda o index é 1 e o tamanho normal é 0
    # tamanho1 -> tamanho6 label // xtamanho1 -> xtamanho6 spinbox
    if op == 0:
        pro.tamanho6.hide()
        pro.xtamanho6.hide()
        pro.tamanho1.setText('Tamanho U')
        pro.tamanho2.setText('Tamanho P')
        pro.tamanho3.setText('Tamanho M')
        pro.tamanho4.setText('Tamanho G')
        pro.tamanho5.setText('Tamanho GG')
    else:
        pro.tamanho1.setText('Tamanho 36')
        pro.tamanho2.setText('Tamanho 38')
        pro.tamanho3.setText('Tamanho 40')
        pro.tamanho4.setText('Tamanho 42')
        pro.tamanho5.setText('Tamanho 44')
        pro.tamanho6.show()
        pro.xtamanho6.show()


def pesquisar():
    try:
        cdb = int(pro.cdb_add.text())
    except ValueError:
        QtWidgets.QMessageBox.about(pro, 'Erro', 'Insira um código de barras válido')
        return 'a'
    else:
        pass

    validacao = Funções.validacao_cdb(cdb)
    if validacao:
        dados = Funções.pegarvalor(cdb, todos=1)
        dados.insert(0, cdb)

        for y in range(0, 16):
            pro.verestoquetabela_2.setItem(0, y, QtWidgets.QTableWidgetItem(str(dados[y])))

        # Limpa todos os dados passados antes
        # pro.cdb.clear()
        # pro.descricao.clear()
        # pro.valor.clear()
        limparjanela2()
        pro.tipotamanho.setCurrentIndex(0)
        mudoucombobox()
        habilitar(0)

        # Inserindo os dados na janela
        pro.cdb.insert(str(dados[0]))
        pro.descricao.insert(dados[1])
        pro.valor.insert(f'{float(dados[2]+0):.2f}')
        pro.tipotamanho.setCurrentIndex(dados[15])

        # mudoucombobox()
        if dados[15] == 1:
            pro.xtamanho1.setValue(dados[9])
            pro.xtamanho2.setValue(dados[10])
            pro.xtamanho3.setValue(dados[11])
            pro.xtamanho4.setValue(dados[12])
            pro.xtamanho5.setValue(dados[13])
            pro.xtamanho6.setValue(dados[14])
        else:
            pro.xtamanho1.setValue(dados[4])
            pro.xtamanho2.setValue(dados[5])
            pro.xtamanho3.setValue(dados[6])
            pro.xtamanho4.setValue(dados[7])
            pro.xtamanho5.setValue(dados[8])

    else:
        QtWidgets.QMessageBox.about(pro, 'Dados inválidos', 'Os dados inseridos estão incorretos')


def atualizarhistorico():
    # Lê os dados do historico e mostra na tela
    dados = Funções.verhistorico()
    pro.verhistoricotabela.setRowCount(len(dados))

    for m in range(0, len(dados)):
        for b in range(0, 6):
            pro.verhistoricotabela.setItem(m, b, QtWidgets.QTableWidgetItem(str(dados[m][b])))


def atualizarestoque():
    # Lê os dados do banco de dados e mostra no "Ver Estoque"
    dados = Funções.verlista()
    pro.verestoquetabela.setRowCount(len(dados))

    for m in range(0, len(dados)):
        for b in range(0, 16):
            pro.verestoquetabela.setItem(m, b, QtWidgets.QTableWidgetItem(str(dados[m][b])))


def abrirestoque():
    pro.framecompras.close()
    pro.frameverhistorico.close()
    pro.frameadicionarpecas.close()
    pro.frameclientes.close()
    pro.frameverestoque.show()


def abrirhistorico():
    pro.framecompras.close()
    pro.frameadicionarpecas.close()
    pro.frameclientes.close()
    pro.frameverestoque.close()
    pro.frameverhistorico.show()


def abriradicionarpecas():
    pro.framecompras.close()
    pro.frameclientes.close()
    pro.frameverestoque.close()
    pro.frameverhistorico.close()
    pro.frameadicionarpecas.show()


def abrirclientes():
    pro.framecompras.close()
    pro.frameverestoque.close()
    pro.frameverhistorico.close()
    pro.frameadicionarpecas.close()
    pro.frameclientes.show()


def abrircompras():
    pro.frameverestoque.close()
    pro.frameverhistorico.close()
    pro.frameadicionarpecas.close()
    pro.frameclientes.close()
    pro.framecompras.show()


app = QtWidgets.QApplication([])
pro = uic2.loadUi('app.ui')

# Isso são valores padrões
pro.cdb_add.setValidator(QIntValidator())
pro.cdb.setValidator(QIntValidator())
pro.valor.setValidator(QDoubleValidator())
pro.tipotamanho.currentIndexChanged.connect(mudoucombobox)
pro.tamanho6.hide()
pro.xtamanho6.hide()
pro.atualizar.hide()
pro.cadastrar.hide()
# pro.excluir.setEnabled(False)
# pro.comboBox.setCurrentIndex(1)

# Colunas
# Tabela do histórico
pro.verhistoricotabela.setColumnWidth(0, 100)
pro.verhistoricotabela.setColumnWidth(1, 100)
pro.verhistoricotabela.setColumnWidth(2, 360)
pro.verhistoricotabela.setColumnWidth(3, 100)
pro.verhistoricotabela.setColumnWidth(4, 530)
pro.verhistoricotabela.setColumnWidth(5, 100)
# Tabela de estoque
pro.verestoquetabela.setColumnWidth(0, 100)
pro.verestoquetabela.setColumnWidth(1, 250)
pro.verestoquetabela.setColumnWidth(2, 30)
pro.verestoquetabela.setColumnWidth(4, 75)
pro.verestoquetabela.setColumnWidth(5, 75)
pro.verestoquetabela.setColumnWidth(6, 75)
pro.verestoquetabela.setColumnWidth(7, 75)
pro.verestoquetabela.setColumnWidth(8, 75)
pro.verestoquetabela.setColumnWidth(9, 75)
pro.verestoquetabela.setColumnWidth(10, 75)
pro.verestoquetabela.setColumnWidth(11, 75)
pro.verestoquetabela.setColumnWidth(12, 75)
pro.verestoquetabela.setColumnWidth(13, 75)
pro.verestoquetabela.setColumnWidth(14, 75)
pro.verestoquetabela.setColumnWidth(15, 50)


# Botões
pro.atualizarestoque.clicked.connect(atualizarestoque)
pro.atualizarhistorico.clicked.connect(atualizarhistorico)
pro.pesquisar.clicked.connect(pesquisar)
pro.editar.clicked.connect(editar)
pro.cadastrarnovo.clicked.connect(novocadastro)
pro.cadastrar.clicked.connect(cadastrar)
pro.atualizar.clicked.connect(atualizar)
pro.excluir.clicked.connect(excluir)
pro.buscar.clicked.connect(filtrar)

# Icones
pro.pesquisar.setIcon(QtGui.QIcon('icons/dsds.png'))
pro.buscar.setIcon(QtGui.QIcon('icons/dsds.png'))
pro.abahistorico.setIcon(QtGui.QIcon('icons/history.png'))
pro.abaadicionar.setIcon(QtGui.QIcon('icons/add.png'))
pro.abaestoque.setIcon(QtGui.QIcon('icons/stock.png'))
pro.abaclientes.setIcon(QtGui.QIcon('icons/user.png'))
pro.abacompras.setIcon(QtGui.QIcon('icons/cart.png'))

# Abas
pro.abaestoque.clicked.connect(abrirestoque)
pro.abahistorico.clicked.connect(abrirhistorico)
pro.abaadicionar.clicked.connect(abriradicionarpecas)
pro.abaclientes.clicked.connect(abrirclientes)
pro.abacompras.clicked.connect(abrircompras)

pro.show()
app.exec()
