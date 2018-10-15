#!/usr/bin/python3
# -*- coding: utf-8 -*-
#import clases
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSmilHandler(ContentHandler):
    """obtener el valor de los atributos de cada nombre"""
    def __init__(self):
        """hacer un diccionario con atributos"""
        self.etiquetas = ["root-layout", "region", "img", "audio","textstream"]
        self.diccAtributos = {"root-layout":["width","height","background-color"],
                        "region":["id","top","left"],
                        "img":["src","region","begin","dur","end"],
                        "audio":["src","begin"],
                        "textstream":["src","region","fill"]}
        self.lista = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name in self.etiquetas:
            diccAtributos={}
            diccAtributos["etiquetas"] = name
            for atributos in self.diccAtributos[name]:
                diccAtributos[atributos] = attrs.get(atributos,"")
            self.lista.append(diccAtributos)

    def get_tags(self):
        print(self.lista)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    sHandler = SmallSmilHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.get_tags())
