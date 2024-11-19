import os, sys

from functions_file_detector import *

strDirArquivo  = f'{os.path.dirname(os.path.realpath(__file__))}\\arquivos'

lstArquivos = [f for f in os.listdir(strDirArquivo) if os.path.isfile(os.path.join(strDirArquivo, f))]

for strArquivo in lstArquivos:
   try:
      strTipoArquivo = getTipoArquivo(f'{strDirArquivo}\\{strArquivo}')
   except FileNotFoundError:
      print(f'\nArquivo {strArquivo.upper()} não encontrado...\n')
   except:
      print(f'\nERRO: {sys.exc_info()[0]}\n')
   else:
      print(f'\nArquivo: {strArquivo}')
      print(f'Tipo...: {strTipoArquivo}\n')