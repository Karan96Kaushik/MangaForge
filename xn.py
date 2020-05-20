from xnxx import page as xnxx

count = -1

while(True):
    count = count + 1
    file1 = open('myfile.txt', 'r') 
    Lines = file1.readlines() 
    xnxx(Lines[count], 'XNXX')
