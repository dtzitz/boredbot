#! python3

import requests
import bs4
# import praw
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
    eventName = []
    eventLink = []

    '''
    for item in thingNames:
        eventName.append( str('##'+item.text.strip('\n')) )
        # postContent.write(eventName+' at ''\n')
    '''

    eventName = [str('##'+item.text.strip('\n')) for item in thingNames]

    '''
    for item in thingLinks:
        eventLink.append( '[tampabay.com]'+'(http://www.tampabay.com'+str(item.get('href'))+')')
        # postContent.write(eventLink)
    '''

    eventLink = ['[tampabay.com]'+'(http://www.tampabay.com'+str(item.get('href'))+')' for item in thingLinks]

    for i in range(len(eventName)):
        print(eventName[i])
        print(eventLink[i])
        postContent.write(eventName[i]+' at ''\n')
        postContent.write(eventLink[i])




    postContent.close()

    # Get content from creative loafing
    clThings = requests.get('http://cltampa.com/tampa/EventSearch?feature=CL%20Recommends&narrowByDate=This%20Weekend')
    creative_success = True
    try:
        clThings.raise_for_status()
        print "Tried"
    except requests.exceptions.HTTPError as e:
        creative_success = False
        print
        print "##### HANDLED EXCEPTION #####"
        print "cltampa.com error = ", e


    if creative_success:
        clSoup = bs4.BeautifulSoup(clThings.text)

        clNames = clSoup.select('.listing h3 a')
        removeGarbage(clNames)

        postContent = open('redditPost.txt', 'a')
        postContent.write('\n\n\n')
        postContent.write('Here\'s some stuff to do this weekend\n\n')
        for item in clNames:

            eventName = str('## '+item.text.strip())
            eventLink = str('[ClTampa]'+'('+item.get('href').strip('\n')+')')
            postContent.write(eventName+' at '+ eventLink +'\n')

        postContent.write('This post was automated by /u/dtzitz')
        postContent.close()






    # user_agent = "Weekend Warrior"
    # reddit = praw.Reddit(user_agent=user_agent)
    # reddit.login('boredbot', 'liHTP02lu3Xx')
    # reddit.submit('reddit_api_test', 'Now do the Tampa Scrape', text=postContent)


TampaScrape()
