import re
import os

x = 0
### ??? Uncomment section below: to use this program at a "NON-JOHNS CREEK" bux!!
# s_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\s_file.txt"
# t_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\t_file.txt"
# d_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\YourData2.txt"

### Uncomment section below: to use this program at HOME or the "JOHNS CREEK" bux!!
#s_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\test-data\\switch0.txt"
#t_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\test-data\\switch1.txt"
#d_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\test-data\\result0.txt"

### Uncomment section below: to use this program at the SANDY SPRINGS bux!!
s_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\test-data\\switch0.txt"
t_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\test-data\\switch1.txt"
d_wwn = "C:\\Users\\cprea\\OneDrive\\Proj4\\test-data\\result0.txt"
x = 0

#with open(s_wwn, 'r') as f1, open(t_wwn, 'r') as f2:
#     for line in f1:
#    line=line.strip()
#    print("Searching for: ", line)
#       if line in f2:
#              print(line + " found at" + t_wwn)
with open(s_wwn, 'r') as f1, open(t_wwn, 'r') as f2:
    while True:
        for line in f1:
            line = line.strip()
            for line2 in f2:
                line2 = line2.strip()
                if line2 == line:
                    print("WWN: " + line + " discovered on switch t_wwn")
                    break















