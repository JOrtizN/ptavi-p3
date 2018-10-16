#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSmilHandler
import sys

try:

    parser = make_parser()
    Nclase = SmallSmilHandler()
    parser.setContentHandler(Nclase)
    parser.parse(open(sys.argv[1]))

    Nlista = Nclase.get_tags()
    lineaX = ""
    archiv_aux = ""
    for linea in Nlista:
        etiqueta = linea[0]
        atributo = linea[1]

        for valor in atributo:
            if atributo[valor] != '':
               etiqueta +=  "\\t" + valor +"=\"" + atributo[valor] + "\""

        archiv_aux = archiv_aux + etiqueta + "\n"

    print (archiv_aux[:-1])  # para salvar la linea en blanco, mirar como hacerlo mejor



except IndexError:
    sys.exit("sgdvb")
