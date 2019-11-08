x = 0

with open('s_file.txt', 'r') as f1, open('t_file.txt', 'r') as f2:
    for line in f1:
        #print("Source Line: " + str(line).strip())
        if line in f2:
            print("Line: " + line + " from \'Source File was located in " + 'Target')
        else:
            print(">> " + line + "   ....NOT FOUND")
