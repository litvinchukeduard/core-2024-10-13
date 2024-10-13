from pathlib import Path

path = 'folder'

other_folder = path + '/myfolder' + "1"

p = Path(other_folder)
p.mkdir()