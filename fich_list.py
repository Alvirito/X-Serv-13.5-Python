#!/usr/bin/python
# -*- coding: utf-8 -*-

fich=open("/etc/passwd","r")
lista=fich.readlines()
print "Tenemos" + str(len(lista))+ "usuarios"
fich.close()

dicc={}

fich=open("/etc/passwd","r")



for linea in lista:
	conf=linea.split(":")
	username=conf[0]
	shell=conf[-1][:-1]
	print "USUARIO    " + username + "  shell:  " + shell
	dicc[username]= shell
	

print "root", dicc["root"]
try:
   print "imaginario", dicc["imaginario"]
#miramos si hay error
except KeyError:
   print ("No existe clave") 
fich.close()
