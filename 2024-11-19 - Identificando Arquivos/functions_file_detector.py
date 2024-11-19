import sys 

from file_type_signatures import *

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
            return strTipoArquivo

      strExtensaoArquivo = '.' + nomeArquivo.split('.')[-1]
      if strExtensaoArquivo in EXTENSOES_LINGUAGENS.keys():
         return EXTENSOES_LINGUAGENS[strExtensaoArquivo]

      return 'Tipo de Arquivo Desconhecido'
