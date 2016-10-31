import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

def game_step(word):
        rus = word[2]
        eng = word[1]
        print word[0], eng
        inp = raw_input()
        if inp == "":
                print rus
                return True
        else:
                print rus
                return False
        
        

def set_box(id,box_number):
        cur.execute('UPDATE polls_word SET box = {0} WHERE id = {1}'.format(box_number, id))
        con.commit()
        return 0
        

def game():
        cur.execute('SELECT * FROM polls_word WHERE box is NULL ')
        print "Enter - go to 2 box, any key - go to 1 box"
        print "{0} new words".format(len(cur.fetchall()))
        for word in cur.fetchall():

                flag = game_step(word)
                if flag:
                        set_box(word[0],2)
                else:
                        set_box(word[0],1)

game()
print "Exit"


                

