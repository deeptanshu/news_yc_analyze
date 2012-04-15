import sqlite3 as lite
import sys
import urllib2
from BeautifulSoup import BeautifulSoup,NavigableString

con = lite.connect('news_yc.db')
cur = con.cursor()  
cur.execute("SELECT Target FROM Posts")
rows = cur.fetchall()

def printText(tags):
    for tag in tags:
        if tag.__class__ == NavigableString:
            print tag,
        else:
            printText(tag)
    print ""

def grab_text(row):
    try:
        f = urllib2.urlopen(row)
        data = f.read()
        f.close()
        soup = BeautifulSoup(data)
        #printText(soup.findAll("p"))
        for node in soup.findAll("p"):
            if ("pdf" not in row):
                print ''.join(node.findAll(text=True)).encode('utf-8')
    except urllib2.HTTPError, e:
        print "OSSIFRAGE"

for i in range(100):
    row = rows[i][0]
    grab_text(row) 
    


cur.close()
