import requests
from bs4 import BeautifulSoup
from collections import deque

# In this class, spider can fetch all the link
# of different episode of one specific manga book
class MangaSpider:

    # initial all the preset
    manganame = 'yaren'
    url = 'http://www.dm5.com/manhua-' + manganame
    queue = deque()
    visited = set()
    visitCounter = 0
    queue.append(url)

    filepath = '/Users/bochen/git/Training/python/yaren.text'
    f_obj = open(filepath, 'w')

    # while queue:
    #     # pop deque and add to visited set
    #     url = queue.popleft()
    #     visited |= {url}
    #     visitCounter += 1
    #     print('Fetch Count: ' + str(visitCounter) + '\n -->Fetching: ' + url)
    #
    #     # setting response and cook soup
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, "html.parser")
    #
    #     for link in soup.find_all('a'):
    #         if link.has_attr('href') and link.has_attr('title'):
    #             if '亚人' in link['title']:
    #                 tempurl = 'http://www.dm5.com' + link['href']
    #                 if tempurl not in visited:
    #                     # append a new url to queue
    #                     queue.append(tempurl)
    #                     print('Add new url to set' + tempurl)
    #                 else:
    #                     print('oops... link is visited!')
    #
    # savedata(visited)

    # savedata(link['title'] + ': ' + tempurl)

    # sortFileContent()

    # setting response and cook soup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all('a'):
        if link.has_attr('href') and link.has_attr('title'):
            if '亚人' in link['title']:
                tempurl = 'http://www.dm5.com' + link['href']
                if tempurl not in visited:
                    # append a new url to queue
                    f_obj.write(link['title'] + ': ' + tempurl + '\n')
                    print('Add new url to set' + tempurl + '\n')
                else:
                    print('oops... link is visited!')
    f_obj.close()

    # open the link file and sort all the link
    file = open('/Users/bochen/git/Training/python/' + manganame + '.text', 'r')
    lines = [line for line in file if line.strip()]
    lines.sort()
    file.close()
    file = open('/Users/bochen/git/Training/python/' + manganame + '.text', 'w')
    file.writelines(lines)
    file.close()

    # exit system
    print('Spider is tire... mission complete.')
    exit(0)
