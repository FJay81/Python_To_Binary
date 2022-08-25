
def tobin(string):

    strarr = []

    for char in string:
        strarr.append(char)

    asciistrarr = []

    for char in string:
        asciistrarr.append(ord(char))
        
    binstrarr = []

    for num in asciistrarr:
        binstrarr.append(bin(num))
    
    return binstrarr


def tostr(binlist):
    
    asciistrarr = []
    
    for num in binlist:
        asciistrarr.append(int(num,2))
    
    strarr = []
    
    for char in asciistrarr:
        strarr.append(chr(char))
        
    string = str()
    
    for char in strarr:
        string += char
        
    return string
       

def FileToBin():
    file = input('File to convert(incl. extension):\n')

    f = open(file,'r')

    content = f.read()
    f.close()
    del f


    binary_file_data = tobin(content)

    to_print = [binary_file_data]


    new_file = open(file+'.binstr','w')
    new_file.write('')

    new_file = open(file+'.binstr','a')

    for obj in to_print[0]:
        
        new_file.write(''+obj+',')

    new_file.close()
    
    
    
    
def Transpiler():
    file = input('File to run(Ends in \'.binstr\'):\n')


    f = open(file,'r')
    content = f.read()
    f.close()




    newlist = []
    content_list = [content]


    content_list = content_list[0].split(',')

    content_list.remove('')

    final = tostr(content_list)

    file = input('newfile name(incl. extension):\n')

    f = open(file,'w')
    f.write(final)
    f.close()

def Translator():
    
    file = input('File to run(Ends in \'.binstr\'):\n')



    f = open(file,'r')
    content = f.read()
    f.close()




    newlist = []
    content_list = [content]


    content_list = content_list[0].split(',')

    content_list.remove('')

    final = tostr(content_list)

    tempy = 'temp.py'

    f = open(tempy,'w')
    f.write(final)
    f.close()

    import temp
    
    f = open(tempy,'w')
    f.write('')
    f.close()


def main():
    choice = int(input('1 - File to binary file\n2 - Transpiler of binary file\n3 - Translator of Binary file\n'))
    if choice == 1:
        FileToBin()
    elif choice == 2:
        Transpiler()
    elif choice == 3:
        Translator()
    else: exit()
    
    
main()