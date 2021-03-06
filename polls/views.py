from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Word

import random
import os
import time
import sys
import glob

# Create your views here.

def yamap(request):
    answer = 1
    return render(request, 'dict/yamap.html', {'FinalList':answer}) 



def parsing(request):
    Word.objects.all().delete()
    from defs import get_word
    GT=time.time()
    #Word.objects.all().delete()

    file_list=glob.glob('data/*.txt')
    count = 0
    for file in file_list:
        f=open(file,'r')
        for string in f:
            word = get_word(string, file)
            if word == 1:
                continue
            #print word
            try:
                word.save()
                #time.sleep(0.1)
                count+=1
            except:
                time.sleep(1)
                print "ERROR: ",word.word_eng, string
                pass
        print file, count, time.time()-GT
        f.close() 
    #return HttpResponse(str(count)+" words created by "+str(time.time()-GT))
    return HttpResponse(str(count))


def test_parsing(request):
    from defs import test_case, get_count_of_filestrings
    GT=time.time()
    url_parse = 'http://127.0.0.1:8000/polls/parse'
    url_clean = 'http://127.0.0.1:8000/polls/clean'

    if not test_case(url_clean,'Clean'):
        return HttpResponse("ERROR in 1 TestCase")
    print "____________TEST CASE 1 OK_______" 
    count = get_count_of_filestrings()
    print count
    if not test_case(url_parse, str(count)):
        return HttpResponse("ERROR in 2 TestCase")
    print "____________TEST CASE 2 OK_______"

    if not test_case(url_clean,'Clean'):
        return HttpResponse("ERROR in 3 TestCase")
    print "____________TEST CASE 3 OK_______" 
       

    f = open("data/adjective.txt", 'a')
    f.write("covet:domogatsa")
    f.close()
    print count+1

    if not test_case(url_parse,str(count+1)):
            f = open("data/adjective.txt", 'r')
            lines = f.readlines()
            lines = lines[:-1]
            f.close()

            f = open("data/adjective.txt", 'w')
            for line in lines:
                f.write(line)
            f.close()
            return HttpResponse("ERROR in 4 TestCase")
    print "____________TEST CASE 4 OK_______"
    

    f = open("data/adjective.txt", 'r')
    lines = f.readlines()
    lines = lines[:-1]
    f.close()

    f = open("data/adjective.txt", 'w')
    for line in lines:
        f.write(line)
    f.close()
    '''
    if not test_case(url_clean,'Clean'):
        return HttpResponse("ERROR in 5 TestCase")
    print "____________TEST CASE 5 OK_______" 
    '''

    return HttpResponse("Passed. <br> Time: "+str(time.time()-GT))




def index(request):
    from defs import generate_word
    flag="False"
    try:

        word=Word.objects.get(word_rus=request.POST['0'])

        word.count+=1
        print 1
        if request.POST['1']==request.POST['0']:
            word.flag+=1
            word.save()
            flag="True"
        #word.coef=100*word.flag/word.count+1
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
            print key
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
    print answer
    return render(request, 'dict/index.html', {'FinalList':answer})






'''
def req_reboot(request):
    return render(request, 'dict/req_reboot.html')
def req_shutdown(request):
    return render(request, 'dict/req_shutdown.html')
def req_clean(request):
    return render(request, 'dict/req_clean.html')

def reboot(request):
    os.system("shutdown /r")
    return HttpResponse("Reboot system")
def shutdown(request):
    os.system("shutdown /s")
    return HttpResponse("Shutdown system")
'''

def clean(request):
    Word.objects.all().delete()
    return HttpResponse("Clean")

def get_ip(request):


    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse("IP :" + str(ip))


    return HttpResponse(str(count))

 


def quiz(request):
    from defs import generate_list
    #ans1 = Word.objects.all().order_by("id")
    ans1 = generate_list()
    print ans1
    return render(request, 'dict/begin.html', {'FinalList':ans1})

def quiz_con(request):
    print request.POST['q']
    correct_key = int(request.POST['0'])
    key_ans=0
    for key in request.POST:
        if key == 'csrfmiddlewaretoken' or key == '0':
            continue
        key_ans = key
    correct_rus = Word.objects.get(id=request.POST['q']).word_rus
    correct_eng = Word.objects.get(id=request.POST['q']).word_eng
    print correct_rus,request.POST[key_ans],request.POST['q']
    if int(key_ans) == correct_key+1:
        ans1=[]
        word = Word.objects.get(id=request.POST['q'])
        word.coef+=20
        word.count_right+=1
        print word.coef+20,word
        word.save()
    
    else:
        ans1=[correct_rus,request.POST[key_ans],correct_eng]
        word = Word.objects.get(id=request.POST['q'])
        word.coef-=20
        word.count_wrong+=1
        word.save()


    return render(request, 'dict/res.html', {'FinalList':ans1})

def quiz_rus(request):
    from defs import generate_list_rus
    #ans1 = Word.objects.all().order_by("id")
    ans1 = generate_list_rus()
    print ans1[0]
    return render(request, 'dict/begin_rus.html', {'FinalList':ans1})

def quiz_con_rus(request):
    print request.POST['q']
    correct_key = int(request.POST['0'])
    key_ans=0
    for key in request.POST:
        if key == 'csrfmiddlewaretoken' or key == '0':
            continue
        key_ans = key
    correct_rus = Word.objects.get(id=request.POST['q']).word_rus
    correct_eng = Word.objects.get(id=request.POST['q']).word_eng
    print correct_rus,request.POST[key_ans],request.POST['q']
    if int(key_ans) == correct_key+1:
        ans1=[]
        word = Word.objects.get(id=request.POST['q'])
        word.coef+=20
        word.count_right+=1
        print word.coef+20,word
        word.save()
    
    else:
        ans1=[correct_rus,request.POST[key_ans],correct_eng]
        word = Word.objects.get(id=request.POST['q'])
        word.coef-=20
        word.count_wrong+=1
        word.save()


    return render(request, 'dict/res_rus.html', {'FinalList':ans1})