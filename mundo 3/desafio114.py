'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
# código feito por @Lucas-BRT
import subprocess
import os

try:
    import subprocess; subprocess.run(["ping", "-c", "4", "pudim.com.br"] if subprocess.os.name != "nt" else ["ping", "-n", "4", "pudim.com.br"])
except:
    print(Exception)
else:
    print('Tudo ok')