import re

#parsea file
def parseFile(file):
    with open(file, 'r') as f:
        return f.readlines()
#teste parseFile
#print parseFile('./docs/skype range.txt')

#preenche arquivo com lista
def fillFile(file_target, flag, content):
    conteudo = content

    with open(file_target, 'r') as f:
        texto_alvo = f.read()

    with open(file_target, 'w') as f:
        #print conteudo

        texto_flag = texto_alvo.replace(flag, flag + ' FLAG')

        result = texto_flag

        for element in content:
            if (len(content) > 0):
                result = result.replace(flag + ' FLAG', flag + ' ' + element, 1)

        result = result.replace(flag + ' FLAG', flag)

        f.write(result)


content = parseFile('./docs/skype range.txt')
fillFile('./docs/fg_skype_objects_script.txt', 'next', content)
