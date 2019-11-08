import re
import os

##################################################
xx = """guru99
careerguru99
selenium
zone name tfbosnb1_HBA2_p1  vsan77
21:01:00:1b:32:34:15:51
zone_tfbosnb1_01_HBA3_p1
21:01:00:1b:32:34:15:55
21:01:00:1b:32:34:15:50
21:01:00:1b:32:34:15:59
zone name tfbosnb1_HBA2_p1  vsan77
21:01:00:1b:32:34:15:61
21:01:00:1b:32:34:15:60
2101001b32341560
zone name nbmap1_HBA1_p1  vsan77
10:01:00:1b:32:34:10:25
zone name nbmap1_HBA2_p1  vsan77
10:01:00:1b:33:34:15:25
"""

k2 = re.findall(r"(\w+:\w+:\w+:\w+:\w+:\w+:\w+:\w+)", xx, re.MULTILINE)


i = 0
size = len(k2)
while i < size:
    print(k2[i])
    i += 1
print("\n\n", str(i))



if "10:01:00:1b:33:34:15:25" in k2:
    print("She is zhere!")
else:
    print("She has left you...")



