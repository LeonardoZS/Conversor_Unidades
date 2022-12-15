#Leonardo Zaniboni Silva 11801049

import gi
import pandas as pd
import numpy as np

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from os.path import abspath, dirname, join


class TheApp:
    '''The Application Class.'''

    def __init__(self):
        # Build GUI
        self.builder = Gtk.Builder()
        self.builder.add_from_file('main.glade')
        self.window = self.builder.get_object('window')

        #definindo os liststores
        self.liststore_grandezas = Gtk.ListStore(int, str)
        self.liststore = Gtk.ListStore(int, str)

        #definindo as variaveis que serão utilizadas
        self.qtd_grandeza = 0
        self.lista_aux = []
        self.unidade_entrada = []
        self.unidade_saida = []
        self.output = 0
 
        #lendo o arquivo de configuração
        df =  pd.read_excel("config.xlsx") 
        self.dados = np.asarray(df)

        #definindo a quantidade de grandezas
        self.qtd_grandeza = int(len(self.dados[0])/2)

        #definindo o liststore das grandezas
        for i in range (self.qtd_grandeza):
            self.liststore_grandezas.append([i, self.dados[0][2*i]])

        #inicializando o liststore das unidades
        for k in range (int(len(self.dados[:,0]))) :
            if k == 0:                                  #evitando pegar o termo "Unidade"
                pass
            else:
                if type(self.dados[k,0]) == float:      #evitando o "nan" em células vazias do dataframe do pandas
                    pass
                else:                                   #pegando o nome da grandeza e seu ID
                    self.liststore.append([k, self.dados[k,0]])
                    self.lista_aux.append(self.dados[k,1])

        self.unidade_entrada = 0                        #inicializando a unidade de entrada como primeira da lista
        self.unidade_saida = 0                          #inicializando a unidade de saída como primeira da lista

        #Definindo o combo box das grandezas
        self.combo_grandeza = self.builder.get_object('combo_grandeza')
        self.combo_grandeza.set_model(self.liststore_grandezas)
        renderer_text = Gtk.CellRendererText()
        self.combo_grandeza.pack_start(renderer_text, True)
        self.combo_grandeza.add_attribute(renderer_text, "text", 1)
        self.combo_grandeza.set_active(0)

        #Definindo o combo box das unidades de entrada
        self.combo = self.builder.get_object('combo')
        self.combo.set_model(self.liststore)
        renderer_text = Gtk.CellRendererText()
        self.combo.pack_start(renderer_text, True)
        self.combo.add_attribute(renderer_text, "text", 1)
        self.combo.set_active(0)

        #Definindo o combo box das unidades de saída
        self.combo_saida = self.builder.get_object('combo_saida')
        self.combo_saida.set_model(self.liststore)
        renderer_text = Gtk.CellRendererText()
        self.combo_saida.pack_start(renderer_text, True)
        self.combo_saida.add_attribute(renderer_text, "text", 1)
        self.combo_saida.set_active(0)

        self.builder.connect_signals(self)
        self.window.show()

    def on_window_destroy(self, widget):
        '''Classical window close button.'''
        Gtk.main_quit()


    def on_button_clicked(self, button):
        '''Do something...'''
        self.entry = self.builder.get_object('entry')   #definindo a caixa de entrada
        self.saida = self.builder.get_object('saida')   #definindo a caixa de saída
        input = self.entry.get_text()                   #pegando o dado de entrada
        try:                                            #bloco para tentar realizar a conversão com tratamento de erro
            self.output = float(input) * float(self.lista_aux[self.unidade_entrada]) * 1/float(self.lista_aux[self.unidade_saida])
            self.saida.set_text(str(self.output))
        except:
            print("Entrada em formato errado. Por valor, utilize . como separador decimal")
            self.saida.set_text("Formato errado - utilize . como separador decimal")

    def on_combo_changed(self, widget):
        '''Verify which option is selected'''
        active = widget.get_active()
        self.unidade_entrada = active       #salvando a posição da unidade que o usuário colocou 


    def on_combo_saida_changed(self, widget):
        '''Verify which option is selected'''
        active = widget.get_active()
        self.unidade_saida = active         #salvando a posição da unidade que o usuário colocou      
        

    def on_combo_grandeza_changed(self, widget):
        active = widget.get_active()        #pegando a posição da grandeza que o usuário colocou

        self.liststore.clear()              #método chamado para limpar o liststore das unidades
        self.lista_aux = []                 #limpando a lista auxiliar

        #lógica realizada para pegar o nome da unidade e seu respectivo id
        for k in range (int(len(self.dados[:,2*active]))) :
            if k == 0:                                      #evitando pegar o termo "Unidade"
                pass
            else:
                if type(self.dados[k,2*active]) == float:   #evitando o "nan" em células vazias do dataframe do pandas
                    pass
                else:
                    self.liststore.append([k, self.dados[k,2*active]])
                    self.lista_aux.append(self.dados[k,2*active+1])

        self.combo_saida.set_model(self.liststore)
        self.combo.set_model(self.liststore)
        self.combo_saida.set_active(0)
        self.combo.set_active(0)


if __name__ == '__main__':
    try:
        gui = TheApp()
        Gtk.main()
    except KeyboardInterrupt:
        pass