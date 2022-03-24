#!/usr/bin/env python
"""Hello world multi linguas 

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada:

    export LANG=pt_BR

Execução:
    pyhon3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Diogo Lopes"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World"

if current_language == "pt_BR":
    msg = "Olá, Mundo"
elif current_language =="it_IT":
    msg = "Chiao, Mondo"

print(msg)
