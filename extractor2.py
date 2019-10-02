import glob
import os
import shutil
import win32api

path = input('Digite o caminho da pasta de onde copiar os arquivos: ')
diretorio_destino = input('Diga o nome da diretório de destino: ')
extensao = input('Diga a extensão que você deseja mover ex (.pdf): ')
indice_pai = input('Índice da pasta com o nome da cidade: ')
indice_filho = input('Índice da pasta com o nome da pessoa: ')

os.mkdir(diretorio_destino)

lol_path = "%s\\" % path
files = [f for f in glob.glob(lol_path + "**/*.%s" % (extensao), recursive=True)]
for file in files:
    vish = os.path.join(diretorio_destino, file.split('\\')[int(indice_pai)], file.split('\\')[int(indice_filho)])
    if not os.path.exists(vish):
        os.makedirs(vish)
    try:
        print('OKAAY!!')
        shutil.copy2(file, "%s\\" % vish)
    except:
        print("%s - WRONG!!!!!" % file)
        dirname = os.path.dirname(file)
        basename = os.path.basename(file)
        short_dirname = win32api.GetShortPathName(dirname)
        rum = win32api.GetShortPathName(os.path.join(short_dirname, basename))
        try:
            shutil.copy2(rum, "%s\\" % vish)
        except:
            import pdb; pdb.set_trace()
        else:
            print('MAS DEU CERTO!!')
 