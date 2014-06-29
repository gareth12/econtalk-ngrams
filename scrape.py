from bs4 import BeautifulSoup
import urllib
import operator
from random import randint
from time import sleep

# create episodelist from archive page
f = urllib.urlopen("http://www.econtalk.org/archives.html")
soup = BeautifulSoup(f)
tables = soup.find_all("table")
episodetable = tables[5]
episoderows = episodetable.findAll('tr')
episodelist = []
for episoderow in episoderows:
    parts = episoderow.findAll('td')
    if ((len(parts)>0) and (parts[1].a)):
        url = parts[1].a['href']
        title = parts[1].a.string
        date = parts[0].string
        episodelist = episodelist + [[url,title,date]]

# write transcripts
episodelist = list(enumerate(reversed(episodelist),start=1))
for i in episodelist[388:425]:
    print "Saving transcript for episode " , i
    sleep(10)
    u = urllib.urlopen(i[1][0]) 
    soup = BeautifulSoup(u)
    if (soup.find(id="unique")):
        f = open('transcripts/'+str(i[0])+'.txt', 'w')
        description = ' '.join(soup.find(id="unique").stripped_strings)
        f.write(description.encode('utf8'))

# write episode list
f = open('episodelist.txt', 'w')
for i in list(enumerate(reversed(episodelist),start=1)):
    f.write('"'+i[0]+'","'+i[1][0]+'","'+i[1][1]+'","'+i[1][2]+'"\n')



