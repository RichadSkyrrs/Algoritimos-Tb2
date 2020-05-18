import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from controle_compras import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnAdicionar.clicked.connect(self.adicionar)
        self.ui.btnSoma.clicked.connect(self.calcular_soma)
        
        
    def adicionar(self):
        produto = self.ui.edtProduto.text()    
        preco = self.ui.edtPreco.text()    
        
        if not produto or not preco:
            msg = QMessageBox()
            msg.setWindowTitle('Atenção!')
            msg.setText('Preencha o Item e o Preço')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()            
            self.ui.edtProduto.setFocus()
            return
            
        self.ui.lstItens.addItem(produto)
        self.ui.lstPrecos.addItem(preco)
        
        self.ui.edtNome.setText('')
        self.ui.edtNota.setText('')
        self.ui.edtNome.setFocus()

    def calcular_soma(self):

       
        num = self.ui.lstItens.count()
        
        if num == 0:
            msg = QMessageBox()
            msg.setWindowTitle('Atenção!')
            msg.setText('Não há itens para calcular a soma')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()            
            self.ui.edtProduto.setFocus()
            return
            
        soma = 0
        
        for i in range(num):
            soma += float(self.ui.lstPrecos.item(i).text())
            
        media = soma 
        
        msg = QMessageBox()
        msg.setWindowTitle('Resultado')
        msg.setText(f'Soma dos Itens')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())