import re
import os

src_d = ''
src_w = ''
pat = re.compile(r"(\w+:\w+:\w+:\w+:\w+:\w+:\w+:\w+)")

src_dir = input("Directory containing Flogi output files: ")   # user input:  directory containing flogi output files
file_list = os.listdir(src_dir)                                 # populate 'switch_list' with 'listdir' output.
print(file_list)
print(src_dir)
#src_d = src_dir
src_wwns = input("Full Path to the file containing the WWNs to locate: ")



os.chdir(src_dir)                               # switch to 'src_dir' directory










