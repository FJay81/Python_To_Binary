from os import system

from binary import tostr

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

