import glob
from os import path

from xlsx2html import xlsx2html

excels = glob.glob("/Users/veneet/Desktop/testing/run/**/*.xlsx")

for excel in excels:
    file_name_without_ext = path.splitext(path.basename(excel))[0]
    parent_dir = path.dirname(excel)
    # parent_dir = "."
    html_path = path.join(parent_dir, f"{file_name_without_ext}.html")
    xlsx2html(excel, html_path)


