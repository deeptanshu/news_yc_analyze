This is an ongoing personal project to apply basic NLP and ML techniques on datascraped from popular content aggregator/forum news.ycombinator.com aka Hacker News. Requires python and sqlite3.

**NOTE**: At present all of this code is about dataset preparation and presentation. 

Here is brief outline of the files at present and what they do:

* *news_yc.db* A simple database which contains the HN comment id as the database key, the title of the post, and the outgoing target link. The schema is: CREATE TABLE Posts(Id INT, Title TEXT, Target TEXT);

* *rss_link_extractor.py* This grabs the rss feed and stores the id, titles and targets in the database, if they don't already exist. I chose to grab the RSS feed for two reasons: I was only interested on static content of front page posts. Second, HN has a pretty strict policy for scrapers and it is easy to get your IP blocked if you don't respect robots.txt

* *timerscraper* This is a bash script which runs the rss_link_extractor every thirty minutes for 72 hours. I noticed that generally there was a new post popped up to the front page every thirty minutes. There are posts with shorter lifetimed, I have ignored them. 

* *soup/web_content.py* Grabs the content of the front page posts. The primary logic and algorithms will probably live in this directory.  

* *django_awesome/* Contains the standard django MTV workflow. 


* *html/* Contains templates in django templating format. 

Screenshot: 
![screenshot](img/screenshot.png)
   
