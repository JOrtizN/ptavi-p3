#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSmilHandler
import sys
import json
from urllib.request import urlretrieve


class KaraokeLocal():
    def __init__(self, fich):
        parser = make_parser()
        Nclase = SmallSmilHandler()
        parser.setContentHandler(Nclase)
        parser.parse(open(fich))
        self.Nlista = Nclase.get_tags()

    def __str__(self):
        archiv_aux = ""
        for linea in self.Nlista:
            etiqueta = linea[0]
            atributo = linea[1]
            for valor in atributo:
                if atributo[valor] != '':
                    etiqueta += "\\t" + valor + "=\"" + atributo[valor] + "\""
            archiv_aux = archiv_aux + etiqueta + "\n"
        print(archiv_aux, end='')

    def to_json(self, fichero):
        json.dump(self.Nlista, open(fichero, "w"))

    def do_local(self):
        url = ""
        for linea in self.Nlista:
            atributo = linea[1]
            for valor in atributo:
                if valor == 'src'and atributo[valor].startswith('http://'):
                    url = atributo[valor]
                    name = atributo[valor].split("/")[-1]
                    urlretrieve(url, name)
            # print (url) para ver lo que me descarga


if __name__ == "__main__":

    try:
        fich = (sys.argv[1])
        fichjson = (sys.argv[1].replace(".smil", ".json"))
        fich_json = "local.json"
        karaoke = KaraokeLocal(fich)
        karaoke.__str__()
        karaoke.to_json(fichjson)
        karaoke.do_local()
        karaoke.to_json(fich_json)
        karaoke.__str__()
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
