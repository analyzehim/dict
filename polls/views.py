from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Word
from defs import get_word
import random
import os
import time
import sys
import glob

# Create your views here.



def parsing(request):
    GT=time.time()
    Word.objects.all().delete()
    id_max = 1

    word=Word(id=id_max, word_eng='key',word_rus='key')
    try:
        word.save()
    except:
        print word.id, word_eng
        pass
    file_list=glob.glob('data/*.txt')
    for file in file_list:
            f=open(file,'r')
            print file
            for string in f:
                
                word = get_word(string, file)
                if word == 1:
                    continue
                id_max+=1
                word.id = id_max
                try:
                    word.save()
                except:
                    time.sleep(1)
                    print "ERROR: ",word.word_eng, string
                    pass

            f.close() 
    return HttpResponse(str(id_max)+" "+str(time.time()-GT))
'''
def generate_word(length):
    a=[]

    word = Word.objects.all()
    for i in word:
        if (i.coef>100):
            a.append(i.id)
        if (i.coef==100):
            a.append(i.id)
            a.append(i.id)
            a.append(i.id)
        if (i.coef<100):
            for k in range(5*int(float(100)/float(i.coef)+1)):
                a.append(i.id)


   # word=Word.objects.all().order_by("-coef")[length-1]
    return random.choice(a)

def index(request):
    flag="False"
    try:

        word=Word.objects.get(word_rus=request.POST['0'])

        word.count+=1
        print 1
        if request.POST['1']==request.POST['0']:
            word.flag+=1
            word.save()
            flag="True"
        word.coef=100*word.flag/word.count+1
        word.save()
    except:
        print sys.exc_info()
    id_max=Word.objects.all().order_by("-id")[0]
    answer=[]
    key_mas=set()
    mas=[]
    key=0
    while 1:
        try:
            key=generate_word(id_max.id)

            key_mas.add(key)
            
            answer.append(Word.objects.get(id=key).word_eng)
            answer.append(Word.objects.get(id=key).word_rus)
            mas.append(Word.objects.get(id=key).word_rus)
        except:
            print  sys.exc_info
        break
    
    for i in range(3):
        while 1:
            try:
                key=random.randint(1,id_max.id-1);
                if not key in key_mas:
                    key_mas.add(key)
                    mas.append(Word.objects.get(id=key).word_rus)
                    break
            except:
                print key
                continue
    mas.sort()
    for i in mas:
        answer.append(i)
    answer.append(flag)
    
    return render(request, 'dict/index.html', {'FinalList':answer})







def req_reboot(request):
    return render(request, 'dict/req_reboot.html')
def req_shutdown(request):
    return render(request, 'dict/req_shutdown.html')
def req_clean(request):
    return render(request, 'dict/req_clean.html')
def clean(request):
    Word.objects.all().delete()
    return HttpResponse("Clean")
def reboot(request):
    os.system("shutdown /r")
    return HttpResponse("Reboot system")
def shutdown(request):
    os.system("shutdown /s")
    return HttpResponse("Shutdown system")

def get_ip(request):
    word=Word.objects.all()
    for i in word:
        print i.word_rus
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(ip)
'''