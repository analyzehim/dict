import glob
import webbrowser
import time
new = 2
url = "https://translate.google.ru/#en/ru/{0}"
for name in glob.glob("*.txt"):
    f = open(name,"r")
    for line in f:
        
        try:
            if line.split(':')[1]!='\n':
                continue
            else:
                time.sleep(0.1)
                print name, line[:-2]
                webbrowser.open(url.format(line[:-2]), new=new)
        except:
            time.sleep(0.1)
            print name, line[:-1]
            webbrowser.open(url.format(line[:-1]), new=new)
    f.close()
            
