"""
A simple program to extract titles and links of the top 30 Hacker News Posts
"""

from urllib import urlopen
import sqlite3 as lite
import sys

con = lite.connect('/home/monadist/news_yc_scraper/news_yc.db')
con.text_factory = str

cur=con.cursor()

seed = "http://news.ycombinator.com/rss"

#seed = open('sample_rss','r').read()
def get_next_title(page):
    start_title = page.find('<title>')
    end_title = page.find('</title>')
    start_url = page.find('<link>')
    end_url =  page.find('</link>')
    if start_title == -1:
	    return None, 0
    title = page[start_title+7:end_title]
    return title, end_title

def get_next_target(page):
    start_url = page.find('<link>')
    end_url =  page.find('</link>')
    if start_url == -1:
	    return None, 0
    target = page[start_url+6:end_url]
    return target, end_url

def get_next_id(page):
    start_id = page.find('<comments>http://news.ycombinator.com/item?id=')
    end_id =  page.find('</comments>')
    if start_id == -1:
	    return None, 0
    id = page[start_id+46:end_id]
    return id, end_id

def get_all_titles(page):
    titles=[]
    while True:
        new_title, endpos = get_next_title(page)
        if new_title:
            titles.append(new_title)
            page = page[endpos+1:]
        else:
            return titles 

def get_all_targets(page):
    targets=[]
    while True:
        new_target, endpos = get_next_target(page)
        if new_target:
            targets.append(new_target)
            page = page[endpos+1:]
        else:
            return targets 
            
def get_all_ids(page):
    ids=[]
    while True:
        new_id, endpos = get_next_id(page)
        if new_id:
            ids.append(new_id)
            page = page[endpos+1:]
        else:
            return ids 


page = urlopen(seed).read()
hn_titles = get_all_titles(page)
del hn_titles[0]
hn_targets = get_all_targets(page)
del hn_targets[0]
hn_ids = get_all_ids(page)
hn_ids = map(int,hn_ids)
zipped = zip( hn_ids, hn_titles, hn_targets)

cur.execute("SELECT Id FROM Posts")
existing_ids = cur.fetchall()

existing_ids_int = [existing_ids[i][0] for i in range(0,len(existing_ids)) ]


for i in range(0,len(zipped)):
    if hn_ids[i] not in existing_ids_int:
        cur.execute("INSERT INTO Posts VALUES(?, ?, ?)", zipped[i])


#print len(zipped)

con.commit()
