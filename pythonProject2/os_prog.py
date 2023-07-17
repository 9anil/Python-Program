import os
print(os.getcwd())
help(os.listdir)
print(os.listdir('.'))
print(os.listdir('/'))
os.makedirs('./data',exist_ok=True)
print('data' in os.listdir('.'))
print(os.listdir('./data'))
# file1=open('./data/loan1.txt',mode='r')
# file1_read=file1.read()
# print(file1_read)
with open('./data/loan1.txt') as file2:
    file2_read=file2.read()
    print(file2_read)