from polls.models import Word

def get_count_of_filestrings():
    import glob
    file_list=glob.glob('data/*.txt')
    count = 0
    for file in file_list:
        f = open(file,"r")
        for line in f:
            count+=1
        f.close()
    return count

def get_word(string, file):
	string_mas = string.split(':') # in future I guess better way its @ symbol
	english_word=string_mas[0]
	'''
	THIS BELOW WAS FOR CHECK TO DUBLICATE

	try:
		word = Word.objects.get(word_eng=english_word)
		return 1 #already has
	except:
		russian_word = unicode(string_mas[1], "CP1251" )
		if russian_word[-1] == '\n':
			russian_word= russian_word[0:len(russian_word)-1]
	'''
	russian_word = unicode(string_mas[1], "CP1251" )
	if russian_word[-1] == '\n':
		russian_word= russian_word[0:len(russian_word)-1]


	word = Word(word_eng=english_word,word_rus=russian_word)
	word.count = 0
	#print file
	try:
		file_meta = file.split('\\')[1].split('.')[0]
	except:
		file_meta = file.split('/')[1].split('.')[0]
	
	word.isNoun=False
	word.isVerb=False
	word.isAdjective=False
	word.isAdverb=False
	word.coef = 100

	if file_meta=="adjective":
		word.isAdjective=True

	if file_meta=="adverb_preposition":
		word.isAdverb=True

	if file_meta=="noun":
		word.isNoun=True

	if file_meta=="verb":
		word.isVerb=True


	word.meta = file_meta
	word.coef=100
	if len(string_mas)>2:
	    word.example=string_mas[2]
	try:
		id_max = Word.objects.all().latest('id').id
	except:
		id_max = -1
	word.id = id_max + 1



	return word



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


def test_case(url, text):
	import requests
	r = requests.get(url)
	if r.text != text:
		print "Real: ", r.text, "\nExpected: ", text
		return False
	return True
