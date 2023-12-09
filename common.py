file_path = './common.txt'  # Substitua pelo caminho do seu arquivo
common_psw = []
# Abre o arquivo no modo de leitura ('r')
def view_pswd():
 with open(file_path, 'r') as file:
    line = file.readline()
    while line:
        common_psw.append(line.replace('\n',''))
        line = file.readline() 
 return common_psw