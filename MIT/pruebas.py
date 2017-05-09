# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:29:36 2016

@author: Francisco
"""

import string

class Sequencia:
    
    tabla = string.maketrans('ACTG','UGAC')

    def __init__(self, cadena):
        self.cadena = cadena.upper()

    def transcripcion(self):
        tt = string.translate(self.cadena,self.tabla)
        return tt
        
    def restriccion(self,enz):
        if enz in Sequencia.enz_d:
            return self.cadena.count(Sequencia.enz_d[enz])
        else:
            return 0



miseq = Sequencia('ACAGTGTA')
print miseq.transcripcion()
