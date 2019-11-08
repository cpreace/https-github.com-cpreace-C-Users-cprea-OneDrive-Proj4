import re
import os

src_d = ''
src_w = ''
pat = re.compile(r"(\w+:\w+:\w+:\w+:\w+:\w+:\w+:\w+)")

src_dir = input("Directory containing Flogi Out: ")	# user input:  directory containing flogi output files
file_list = os.listdir(src_dir)               		# populate 'switch_list' with 'listdir' output.
src_d = src_dir
src_wwns = input("File containing the WWNs to locate: ")


os.chdir(src_d)                               # switch to 'src_dir' directory










