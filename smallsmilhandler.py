#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSmilHandler(ContentHandler):
    """obtener el valor de los atributos de cada nombre"""
    def __init__(self):
        """hacer un diccionario con etiquetas y atributos """
        self.diccAtributos = {"root-layout":["width","height","background-color"],
                        "region":["id","top","left"],
                        "img":["src","region","begin","dur","end"],
                        "audio":["src","begin"],
                        "textstream":["src","region","fill"]}
        self.lista = []

    def startElement(self, name, attrs):

        if name in self.diccAtributos:
            diccAtributos={}
            for atributos in self.diccAtributos[name]:
                diccAtributos[atributos] = attrs.get(atributos,"")
            self.lista.append([name,diccAtributos])

    def get_tags(self):
        return self.lista

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSmilHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.get_tags())
