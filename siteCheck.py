#!/usr/bin/python
# -*- coding: utf-8 -*-
import time, sys, argparse, re, requests
from bs4 import BeautifulSoup
from datetime import datetime, date

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', default='http://meusite.io')
	parser.add_argument('-t', '--titulo', default='Meu site')
	args = parser.parse_args()

	if args.url == '' or args.titulo == '':
		print('CRITICAL: erro ao executar o script. Execute: siteCheck.py -u <url> -t <titulo> | tempo=0ms')
		sys.exit(2)
	try:
		dataInicio = datetime.now()
		dataFim = datetime.now()
		session = requests.session()
		response = session.get(args.url)
		soup = BeautifulSoup(response.text, 'lxml')
		tituloBusca = soup.title.string
		dataFim = datetime.now() - dataInicio
		if tituloBusca == args.titulo:
			print('OK: acesso ao site: ' + args.url + ' efetuado com sucesso e foi encontrado o título: ' + args.titulo + '. | tempo=' + str(dataFim.microseconds/1000) + 'ms')
			sys.exit(0)
		else:
			print('WARNING: acesso ao site: ' + args.url + ' efetuado com sucesso, porém o título: ' + args.titulo + ' não foi encontrado. | tempo=' + str(dataFim.microseconds/1000) + 'ms')
			sys.exit(1)
	except Exception as exp:
		print('CRITICAL: erro no acesso ao site, tratamento para este erro ainda não foi feito. | tempo=' + str(dataFim.microseconds/1000) + 'ms')
		sys.exit(2)
