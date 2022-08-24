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

temp = 'temp.py'

f = open(temp,'w')
f.write(final)
f.close()


#both of these run the file, up to user which one they use
system('python3 ' + temp)
#import temp 

f = open(temp,'w')
f.write('')
f.close()
