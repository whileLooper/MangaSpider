import requests
import os
from bs4 import BeautifulSoup
from collections import deque

__author__ = 'bochen'
# Using the Link form MangaSpider to
# fetching the manga image, is called ImageSpider
class ImageSpider:

    # Download the image from links, and save them into files
    def save_Image(src, epNum, pgNum):
        savePath = '/Users/bochen/Documents/Manga/yaren/' + str(epNum) + '/'
        saveName = str(pgNum)

        # checking the path exist, if not create new path
        if not os.path.exists(savePath):
            os.makedirs(savePath, exist_ok=True)
        with open(savePath+saveName, 'wb') as handle:
            response = requests.get(src, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

    # open the episode link file
    file_path = '/Users/bochen/git/MangaSpider/yaren.text'
    episode_file = open(file_path, 'r')

    # create a deque to contain link
    queue = deque()

    # read the each episode link from text file
    # add link to the deque
    for line in episode_file.readlines():
        line = line.split(': ', 1)[1]
        queue.append(line)

    response = requests.get('http://www.ishuhui.net/ReadComicBooks/3813')
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())
    # for link in soup('img'):
    #     if link.has_attr('data-original'):
    #         imageSrc = link['data-original']
    #         print(link['data-original'])
    #         episodeNum = imageSrc.split('/')[4]
    #         pageNum = imageSrc.split('/')[5]
    #         # print(episodeNum + ': ' + pageNum)
    #         # save_Image(imageSrc, episodeNum, pageNum)
    #         print(episodeNum + ': ' + pageNum + 'page is saved successfully...')

    for links in soup('div', {'class': 'mangaContentMainImg'}):
        if 'data-original' in links('img')[0].attrs:
            print(links('img')['src'])
    exit(0)