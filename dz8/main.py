from os.path import exists
from csv import creating
from Writer import write_scv
from Writer import write_txt


path = 'Pbook.csv'
valid = exists(path)
if not valid:
    creating()

write_scv()
write_txt()