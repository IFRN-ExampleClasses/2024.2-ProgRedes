'''
   Este arquivo contém as assinaturas de arquivos e extensões de linguagens de programação e 
   de arquivos do Office 365.
'''

# ----------------------------------------------------------------------
ASSINATURAS_ARQUIVOS = {
    b'\xFF\xD8': 'Imagem JPEG',
    b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'Imagem PNG',
    b'\x47\x49\x46\x38\x37\x61': 'Imagem GIF (87a)',
    b'\x47\x49\x46\x38\x39\x61': 'Imagem GIF (89a)',
    b'\x25\x50\x44\x46': 'Documebnto PDF',
    b'\x50\x4B\x03\x04': 'Arquivo ZIP',
    b'\x52\x61\x72\x21\x1A\x07\x00': 'Arquivo RAR',
    b'\x3C\x21\x44\x4F\x43\x54\x59\x50\x45': 'Documento HTML',
    b'\x4D\x5A': 'Executável Windows (EXE)',
    b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1': 'Documento Microsoft Office (DOC, XLS, PPT)',
    b'\x50\x4B\x03\x04': 'Documento Microsoft Office (DOCX, XLSX, PPTX)',
    b'\x49\x44\x33': 'Arquivo MP3',
    b'\x42\x4D': 'Imagem BMP',
    b'\x49\x49\x2A\x00': 'Imagem TIFF (little-endian)',
    b'\x4D\x4D\x00\x2A': 'Imagem TIFF (big-endian)',
    b'\x00\x00\x01\xBA': 'Vídeo MPEG',
    b'\x00\x00\x01\xB3': 'Vídeo MPEG',
    b'\x66\x4C\x61\x43': 'Áudio FLAC',
    b'\x1F\x8B': 'Arquivo GZIP',
    b'\x37\x7A\xBC\xAF\x27\x1C': 'Arquivo 7-Zip',
    b'\x25\x21\x50\x53': 'Documento PostScript',
    b'\x2E\x52\x4D\x46': 'Arquivo RealMedia',
    b'\x46\x4C\x56': 'Vídeo FLV',
    b'\x4F\x67\x67\x53': 'Arquivo Multimidia OGG',
    b'\x00\x01\x00\x00': 'Imagem ICO',
    b'\x00\x00\x00\x18\x66\x74\x79\x70\x33\x67\x70\x35': 'Vídeo MP4',
    b'\x1A\x45\xDF\xA3': 'Vídeo MKV',
    b'\x52\x49\x46\x46': 'Arquivo CorelDRAW (CDR)'
}

# ----------------------------------------------------------------------
EXTENSOES_LINGUAGENS = {
   '.c'   : 'Código-Fonte em Linguagem C',
   '.cpp' : 'Código-Fonte em Linguagem C++',
   '.cs'  : 'Código-Fonte em Linguagem C#',
   '.java': 'Código-Fonte em Linguagem Java',
   '.py'  : 'Código-Fonte em Linguagem Python',
   '.rb'  : 'Código-Fonte em Linguagem Ruby',
   '.js'  : 'Código-Fonte em Linguagem JavaScript',
   '.php' : 'Código-Fonte em Linguagem PHP',
   '.html': 'Código-Fonte em Linguagem HTML',
   '.css' : 'Folha de Estilo CSS',
   '.xml' : 'Documento XML',
   '.sh'  : 'Shell Script',
   '.bat' : 'Arquivo Batch',
   '.pl'  : 'Script Perl',
   '.rs'  : 'Código-Fonte em Linguagem Rust',
   '.go'  : 'Código-Fonte em Linguagem GO'
}

# ----------------------------------------------------------------------
ASSINATURAS_OFFICE365 = {
   'word/document.xml': 'Documento Word (.docx)',
   'xl/workbook.xml': 'Planilha Excel (.xlsx)',
   'ppt/presentation.xml': 'Apresentação PowerPoint (.pptx)',
   'visio/document.xml': 'Desenho Visio (.vsdx)',
   'project/project.xml': 'Projeto Project (.mpp)',
   'onenote/document.xml': 'Bloco de Notas OneNote (.one)',
   'outlook/item1.xml': 'Email Outlook (.msg)',
   'access/document.xml': 'Banco de Dados Access (.accdb)'
}