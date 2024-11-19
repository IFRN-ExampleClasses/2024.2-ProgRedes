'''
   Este arquivo contém funções para identificar o tipo de arquivo.
'''

import sys, zipfile

from file_type_signatures import *

# ----------------------------------------------------------------------
def getTipoArquivoOffice365(nomeArquivo: str):
   with zipfile.ZipFile(nomeArquivo, 'r') as zip:
      for strAssinatura, strTipoArquivo in ASSINATURAS_OFFICE365.items():
         if strAssinatura in zip.namelist():
            return strTipoArquivo
      return 'Tipo de Arquivo Desconhecido...'
        
# ----------------------------------------------------------------------
def getTipoArquivo(nomeArquivo: str):
   intMaxTamanho = max(len(strAssinatura) for strAssinatura in ASSINATURAS_ARQUIVOS.keys())

   try:
      with open(nomeArquivo, 'rb') as file:
         headerArquivo = file.read(intMaxTamanho)
   except FileNotFoundError:
      raise FileNotFoundError(f'Arquivo {nomeArquivo.upper()} não encontrado...')
   except:
      raise Exception(f'ERRO: {sys.exc_info()[0]}')
   else:
      for strAssinatura, strTipoArquivo in ASSINATURAS_ARQUIVOS.items():
         if headerArquivo.startswith(strAssinatura):
            if strAssinatura == b'\x50\x4B\x03\x04':
               return getTipoArquivoOffice365(nomeArquivo)
            return strTipoArquivo

      strExtensaoArquivo = '.' + nomeArquivo.split('.')[-1]
      if strExtensaoArquivo in EXTENSOES_LINGUAGENS.keys():
         return EXTENSOES_LINGUAGENS[strExtensaoArquivo]

      return 'Tipo de Arquivo Desconhecido...'
