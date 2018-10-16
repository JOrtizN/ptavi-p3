#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSmilHandler
import sys
import json


def printlines(Nlista):
    archiv_aux = ""
    for linea in Nlista:
        etiqueta = linea[0]
        atributo = linea[1]
        for valor in atributo:
            if atributo[valor] != '':
               etiqueta +=  "\\t" + valor +"=\"" + atributo[valor] + "\""
        archiv_aux = archiv_aux + etiqueta + "\n"
    print (archiv_aux[:-1])  # para salvar la linea en blanco, mirar como hacerlo mejor

def makejson(Nlista,fichero):
    json.dump(Nlista, open(fichero, "w"))


if __name__ == "__main__":

    try:
        fich = (sys.argv[1])
        fichjson = (sys.argv[1].replace(".smil", ".json"))
        parser = make_parser()
        Nclase = SmallSmilHandler()
        parser.setContentHandler(Nclase)
        parser.parse(open(fich))
        printlines(Nclase.get_tags())
        makejson(Nclase.get_tags(),fichjson)

    except IndexError:
        sys.exit("sgdvb")
