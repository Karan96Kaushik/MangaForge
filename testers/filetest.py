from os import walk, getcwd

mypath = getcwd()

f = []
fol = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    fol.extend(dirnames)
    break

print(f)
print(fol)