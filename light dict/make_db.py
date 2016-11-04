
create_line = '''
CREATE TABLE `polls_word` (`id`	smallintunsigned NOT NULL, 
	`word_eng`	varchar(100),
	`word_rus`	varchar(100),
	`coef`	integer,
	`count`	integer,
	`meta`	varchar(400),
	`count_right`	integer,
	`count_wrong`	integer,
	`speechClass`	integer,
	`box`	integer,
	PRIMARY KEY(id)
);
'''
import sqlite3
import glob
conn = sqlite3.connect('example.db')
c = conn.cursor()


#c.execute('DELETE FROM  polls_word')



insert_line = '''
INSERT INTO polls_word(id, word_eng, word_rus, count, meta, box) 
VALUES ({0},"{1}","{2}",{3},"{4}",{5})
'''

try:
	c.execute('SELECT max(id) FROM polls_word')
	id =  int(c.fetchall()[0][0])
except:
	id = 0

for file in glob.glob("data/*.txt"):
	f = open(file,'r')
	for line in f:
		eng = line.split(":")[0].lower()
		c.execute('SELECT id FROM polls_word WHERE word_eng="{0}"'.format(eng))
		if len(c.fetchall()):
			continue

		id += 1
		rus = unicode(line.split(":")[1], "CP1251" )

		try:

			execute_line = insert_line.format(id,eng,'@#$',100,file,1)
			c.execute(execute_line.replace('@#$',rus)) # in the other case, this drop error about ascii
			print id, eng, file

		except Exception,e:
			print str(e)
			print file, insert_line.format(id,eng,'so',count,meta,box)
			print rus
			break
		conn.commit()
		#break

c.execute('SELECT max(id) FROM polls_word')
print c.fetchall()
conn.close()