
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
       