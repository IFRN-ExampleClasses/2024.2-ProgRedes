import sys, zipfile

from file_type_signatures import *

# ----------------------------------------------------------------------
def getTipoArquivoOffice(nomeArquivo: str):
    with zipfile.ZipFile(nomeArquivo, 'r') as zip:
        if 'word/document.xml' in zip.namelist():
            return "Documento Word (.docx)"
        elif 'xl/workbook.xml' in zip.namelist():
            return "Planilha Excel (.xlsx)"
        elif 'ppt/presentation.xml' in zip.namelist():
            return "Apresentação PowerPoint (.pptx)"
        else:
            return "Tipo desconhecido"
        
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
               return getTipoArquivoOffice(nomeArquivo)
            return strTipoArquivo

      strExtensaoArquivo = '.' + nomeArquivo.split('.')[-1]
      if strExtensaoArquivo in EXTENSOES_LINGUAGENS.keys():
         return EXTENSOES_LINGUAGENS[strExtensaoArquivo]

      return 'Tipo de Arquivo Desconhecido'
