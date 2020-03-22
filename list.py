from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('Comix/') if isfile(join('Comix/', f))]

print(onlyfiles)