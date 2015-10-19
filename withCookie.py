import http.cookiejar
import urllib
import urllib.request
import re
import gzip
__author__ = 'bochen'



def makeMyOpener(head):
    header = []
    cookieJar = http.cookiejar.CookieJar()
    processor = urllib.request.HTTPCookieProcessor(cookieJar)
    opener = urllib.request.build_opener(processor)

    for key, value in head.items():
        e = (key, value)
        header.append(e)

    opener.addheaders = header

    return opener

def saveData(data):
    save_path = '/Users/bochen/git/Training/python/temp.html'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

def getXSRF(data):
    xsrfRe = re.compile('name="\_xsrf\" value=\"(.*)\"', flags=0)
    xsrfStr = xsrfRe.findall(data)
    return xsrfStr[0]

def ungzip(data):
    try:
        print('正在解压...')
        data = gzip.decompress(data)
        print('完成解压！')
    except:
        print('未经压缩，无需解压')

    return data

header = {
    'Collection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,*/*',
    'Accept-Language': 'en-US,en;q=0.8,ja;q=0.6,zh-CN;q=0.4,zh;q=0.2,it;q=0.2',
    'User-Agent': 'Chrome/45.0.2454.101'

}

url = 'http://www.zhihu.com/'
opener = makeMyOpener(header)
urlopen = opener.open(url)
data = urlopen.read()
unzipData = ungzip(data)
_xsrf = getXSRF(unzipData.decode())
print('_xsrf: ', _xsrf)

url += 'login'
loginEmail = 'bochentheone@hotmail.com'
password = 'BOboris8878'
postDict = {
    '_xsrf': _xsrf,
    'email': loginEmail,
    'password': password,
    'rememberme': 'y'
}

postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode())