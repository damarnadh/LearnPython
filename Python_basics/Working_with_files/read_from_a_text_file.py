f = open('D:\DE\Python\learn_python_sample_text.txt')
# file_content =f.read()
# print(file_content)
no_of_words =0
for line in f.readlines():
    #print(len(line.split(' ')))
    if 'than' in line.split(' '):
        print(line,line.split(' ').index('than'))
    no_of_words += len(line.split(' '))
print(no_of_words,'words are there in file')
f.close()
