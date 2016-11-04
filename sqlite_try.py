import sqlite3
from math import sqrt
import glob
import time

con = sqlite3.connect('stocks.db')
cur = con.cursor()

cur.execute('SELECT day_return FROM ba ')

def E(mas):
        return reduce(lambda x, y: x + y, mas) / len(mas)

def cov(x,y):

        E1 = E(x)
        E2 = E(y)
        new_mas = []
        size = min(len(x),len(y))
        for i in range(size):
                new_mas.append( (x[i] - E1)*(y[i]-E2) )
        
        return E(new_mas)

cur.execute('SELECT day_return FROM yndx ')
list_returns_yndx = [i[0] for i in cur.fetchall()]
cur.execute('SELECT day_return FROM goog ')
list_returns_goog = [i[0] for i in cur.fetchall()]
cur.execute('SELECT day_return FROM msft ')
list_returns_msft = [i[0] for i in cur.fetchall()]
print len(  list_returns_msft)  
'''
5cur.execute('SELECT ba.day_return,goog.day_return,mrk.day_return,yahoo.day_return FROM ba,goog,mrk,yahoo WHERE (ba.id = yahoo.id) AND(ba.id = goog.id) AND (ba.id = mrk.id)')
f = open("returns.txt","w")
for i in cur.fetchall():
		st =  str(i)[1:-1]+'\n'
		st = st.replace(',','')
		f.write(st)
f.close()

for file in glob.glob("stocks/*.txt"):
	table =  file.split('/')[1].split('.')[1].split('_')[0]

	for id in range(495):
		cur.execute('SELECT price from {0} where id={1}'.format(table, id+2))
		price_today =  cur.fetchall()[0][0]
		cur.execute('SELECT price from {0} where id={1}'.format(table,id+1))
		price_yesterday=  cur.fetchall()[0][0]
		day_return = float(price_today - price_yesterday)/ float(price_yesterday)
		print id, price_yesterday,price_today,day_return
		insert_str = 'UPDATE {0} SET day_return = {1} WHERE id = {2}'.format(table,day_return, id+2)
		cur.execute(insert_str)
		con.commit()


insert_str = 'UPDATE yndx SET day_return = 1'
cur.execute(insert_str)
con.commit()
cur.execute('SELECT * FROM stocks WHERE stocks.name = "US1.YNDX" AND (SELECT COUNT(*) stocks.date  IN (SELECT date FROM stocks WHERE stocks.name = "US1.T")')
print cur.fetchall()

cur.execute('CREATE TABLE stocks (id INTEGER PRIMARY KEY, name VARCHAR(100), date INTEGER, price REAL, day_return REAL)')

#cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, firstName VARCHAR(100), secondName VARCHAR(30))')
#con.commit()


#cur.execute('SELECT * FROM users')
#print cur.fetchall()
#con.close()
#cur.execute('SELECT * FROM stocks WHERE stocks.date = 20140409 AND stocks.name = "US1.YNDX"')
#print cur.fetchall()
time_stamp = time.time()
#cur.execute('DELETE FROM stocks')
for file in glob.glob("stocks/*.txt"):
	f = open(file, "r")

	table =  file.split('/')[1].split('.')[1].split('_')[0]
	print table
	cur.execute('CREATE TABLE {0} (id INTEGER PRIMARY KEY, name VARCHAR(100), date INTEGER, price REAL, day_return REAL)'.format(table))
	con.commit()
	flag = 0
	for i in f:
		if flag ==0:
			flag = 1
			continue
		new_name = i.split(',')[0]
		new_date = i.split(',')[2]
		new_price = i.split(',')[4]
		cur.execute('SELECT * FROM {2} WHERE {2}.date = {0} AND {2}.name = "{1}"'.format(new_date,new_name,table))
		if cur.fetchall()!=[]:
			continue
		insert_str = 'INSERT INTO {3} (id, name, date, price, day_return) VALUES(NULL, "{0}", {1}, {2}, 0)'.format(new_name, new_date, new_price,table)
		cur.execute(insert_str)
		con.commit()
print "Done", time.time()-time_stamp
con.commit()
'''
