import sys, zipfile

from file_type_signatures import *

# ----------------------------------------------------------------------
def getTipoArquivoOffice365(nomeArquivo: str):
   with zipfile.ZipFile(nomeArquivo, 'r') as zip:
      if 'word/document.xml' in zip.namelist():
         return 'Documento Word (.docx)'
      elif 'xl/workbook.xml' in zip.namelist():
         return 'Planilha Excel (.xlsx)'
      elif 'ppt/presentation.xml' in zip.namelist():
         return 'Apresentação PowerPoint (.pptx)'
      elif 'visio/document.xml' in zip.namelist():
         return 'Desenho Visio (.vsdx)'
      elif 'project/project.xml' in zip.namelist():
         return 'Projeto Project (.mpp)'
      elif 'onenote/document.xml' in zip.namelist():
         return 'Bloco de Notas OneNote (.one)'
      elif 'outlook/item1.xml' in zip.namelist():
         return 'Email Outlook (.msg)'
      elif 'access/document.xml' in zip.namelist():
         return 'Banco de Dados Access (.accdb)'
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
               return getTipoArquivoOffice365(nomeArquivo)
            return strTipoArquivo

      strExtensaoArquivo = '.' + nomeArquivo.split('.')[-1]
      if strExtensaoArquivo in EXTENSOES_LINGUAGENS.keys():
         return EXTENSOES_LINGUAGENS[strExtensaoArquivo]

      return 'Tipo de Arquivo Desconhecido'
