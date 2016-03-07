#! python3

import requests
import bs4
import praw
from listClean import removeGarbage




def TampaScrape():
    postContent = open('redditPost.txt', 'w')
    print('now do the tampa scrape')

    # Get content from tampabay.com
    tampaThings = requests.get('http://www.tampabay.com/things-to-do/')
    tampaThings.raise_for_status()
    tampaSoup = bs4.BeautifulSoup(tampaThings.text)

    thingNames = tampaSoup.select('#TTD_CALENDAR_UNIT1 h3')
    thingLinks = tampaSoup.select('#TTD_CALENDAR_UNIT1 h3 a')

    postContent.write('# Bored?\n')
    postContent.write('Here\'s some things to do today\n\n')
    for i in range(len(thingNames)):
        eventName = str('##'+thingNames[i].text.strip('\n'))
        eventLink = '[tampabay.com]'+'(http://www.tampabay.com'+str(thingLinks[i].get('href'))+')'
        postContent.write(eventName+' at '+eventLink+'\n')


    postContent.close()

    # Get content from creative loafing
    clThings = requests.get('http://cltampa.com/tampa/EventSearch?feature=CL%20Recommends&narrowByDate=This%20Weekend')
    clThings.raise_for_status()
    clSoup = bs4.BeautifulSoup(clThings.text)

    clNames = clSoup.select('.listing h3 a')
    removeGarbage(clNames)

    postContent = open('redditPost.txt', 'a')
    postContent.write('\n\n\n')
    postContent.write('Here\'s some stuff to do this weekend\n\n')
    for item in clNames:

        eventName = str('## '+item.text.strip())
        print(repr(eventName))
        eventLink = str('[ClTampa]'+'('+item.get('href').strip('\n')+')')
        postContent.write(eventName+' at '+ eventLink +'\n')

    postContent.write('This post was automated by /u/dtzitz')
    postContent.close()






    # user_agent = "Weekend Warrior"
    # reddit = praw.Reddit(user_agent=user_agent)
    # reddit.login('boredbot', 'liHTP02lu3Xx')
    # reddit.submit('reddit_api_test', 'Now do the Tampa Scrape', text=postContent)


TampaScrape()
