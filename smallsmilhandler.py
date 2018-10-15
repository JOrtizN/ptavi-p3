#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class smallsmilhandler(ContentHandler):
    """encontrar los atributos """
    def __init__(self):
        self.rlwidth = ""
        self.rlheight = ""
        self.rlbackgroundcolor = ""
        self.isrc = ""

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.rlwidth = attrs.get('width', "")
            self.rlheight = attrs.get('height', "")
            self.rlbackgroundcolor= attrs.get('background-color',"")
            print(self.rlwidth)

        elif name == 'img':
            self.isrc = attrs.get('src',"")
            print (self.isrc)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = smallsmilhandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
