import random
import glob
import math
count=0
file_all=open('all.txt','w')
for txt_file_name in glob.glob("*.txt"):
        if txt_file_name=="all.txt":
            continue
        txt_file = open(txt_file_name,"r")
        for words in txt_file:
            file_all.write(words)
            count+=1
        txt_file.close()
file_all.close()
file_all = open('all.txt', 'r+')
pos = 0
line = file_all.readlines()
file_all.seek(pos)
sort_text = sorted(line)
for new_line in sort_text:
        file_all.write(new_line)
        pos = file_all.tell()
file_all.close()

print str(count)+" strings created"+'\n'

while True:
    try:
        list_of_files = []
        count = 0
        for i in glob.glob("*.txt"):
            list_of_files.append(i)
            print str(count)+": "+i.decode('cp1251')
            count += 1
        inp = raw_input()
        if inp=="exit":
            break
        if len(inp) == 2:
            mode = 2
            k = int(inp[1])
        else:
            mode = 1
            k = int(inp[0])
            
        f = open(list_of_files[int(math.fmod(k, len(list_of_files)))],"r")
        en = []
        ru = []
        for words in f:
            en.append(words.split(":")[0])
            ru.append(words.split(":")[1][0:-1])
        f.close()
        flag = [1 for i in range(len(en))]
        count = 0
        while True:
            if flag == [0 for i in range(len(en))]:
                print "All"
                break
            key = random.randint(0, len(en)-1)
            if flag[key] == 0:
                continue
            flag[key] = 0
            count += 1
            if mode == 1:
                raw_input(en[key].decode('cp1251')+" | " + str(count)+"/"+str(len(en)))
                print ru[key].decode('cp1251')
            if mode == 2:
                str1=ru[key].decode('cp1251')+" | " + str(count)+"/"+str(len(en))
                print str1
                raw_input()
                print en[key].decode('cp1251')
            print "___________"
            print
    except:
      
        continue

