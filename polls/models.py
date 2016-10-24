from django.db import models

class Word(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    word_eng = models.CharField(max_length=100,blank=True, null=True)
    word_rus = models.CharField(max_length=100,blank=True, null=True)
    example = models.CharField(max_length=400,blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    coef= models.IntegerField(blank=True, null=True)
    meta = models.CharField(max_length=400,blank=True, null=True)
    count_right = models.IntegerField(blank=True, null=True)
    count_wrong = models.IntegerField(blank=True, null=True)
    speechClass = models.IntegerField(blank=True, null=True)



    def __unicode__(self):
        string_ans=''
        string_ans+=self.word_eng
        string_ans+=' '
        #string_ans+=unicode(self.word_rus, "CP1251" )
        return (string_ans)

