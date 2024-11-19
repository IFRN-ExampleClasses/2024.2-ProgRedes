import os, sys

from functions_file_detector import *

strDirArquivo  = os.path.dirname(os.path.realpath(__file__))

strArquivo     = '#01 - EXIF - Tutorial.pdf'

try:
   strTipoArquivo =  getTipoArquivo(f'{strDirArquivo}\\arquivos\\{strArquivo}')
except FileNotFoundError:
   print(f'\nArquivo {strArquivo.upper()} não encontrado...\n')
except:
   print(f'\nERRO: {sys.exc_info()[0]}\n')
else:
   print(f'\nArquivo: {strArquivo}')
   print(f'Tipo...: {strTipoArquivo}\n')