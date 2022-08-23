from binary import tobin

#file = input('File to convert(incl. extension):\n')
file = 'main.py'

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