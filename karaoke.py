#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSmilHandler
import sys
import json
from urllib.request import urlretrieve


def printlines(Nlista):
    archiv_aux = ""
    for linea in Nlista:
        etiqueta = linea[0]
        atributo = linea[1]
        for valor in atributo:
            if atributo[valor] != '':
               etiqueta +=  "\\t" + valor +"=\"" + atributo[valor] + "\""
        archiv_aux = archiv_aux + etiqueta + "\n"
    print (archiv_aux,end='')  # para salvar la linea en blanco, mirar como hacerlo mejor

def makejson(Nlista,fichero):
    json.dump(Nlista, open(fichero, "w"))

def dowloand(Nlista):
    url=""
    for linea in Nlista:
        atributo = linea[1]
        for valor in atributo:
            if valor == 'src'and atributo[valor].startswith('http://'):
                url= atributo[valor]
                name=atributo[valor].split("/")[-1]
                urlretrieve(url,name)
        #print (url) para ver lo que me descarga

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
        dowloand(Nclase.get_tags())

    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
