from polls.models import Word

def get_word(string,file):
	string_mas = string.split(':') # in future I guess better way its @ symbol
	english_word=string_mas[0]
	try:
		word = Word.objects.get(word_eng=english_word)
		return 1
	except:
		russian_word=unicode(string_mas[1], "CP1251" )
		if russian_word[len(russian_word)-1]=='\n':
			russian_word= russian_word[0:len(russian_word)-1]

	word = Word(word_eng=english_word,word_rus=russian_word)
	word.count = 0
	word.meta = file
	word.coef=100
	if len(string_mas)>2:
	    word.example=string_mas[2]
	return word