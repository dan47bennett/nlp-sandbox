import urllib2
from bs4 import BeautifulSoup


def writeArrayToFile(fileName, array):
    with open(fileName, 'w') as file:
        for item in array:
            print >> file, item

# data mining to acquire a library of articles
def getAllDoxyDonkeyPosts(url, links):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response)
    for a in soup.findAll('a'):
        try:
            url = a['href']
            title = a['title']
            if title == "Older Posts":
                print title, url
                links.append(url)
                getAllDoxyDonkeyPosts(url, links)
        except:
            title = ""
    return


blogUrl = "http://doxydonkey.blogspot.in"
links = []
getAllDoxyDonkeyPosts(blogUrl, links)
writeArrayToFile('links.txt', links)


def getDoxyDonkeyText(testUrl):
    request = urllib2.Request(testUrl)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response)
    divs = soup.findAll("div", {"class": 'post-body'})

    posts = []
    for div in divs:
        posts += map(lambda p: p.text.encode('ascii', errors='replace').replace("?", " "), div.findAll("li"))
    return posts


doxyDonkeyPosts = []
for link in links:
    doxyDonkeyPosts += getDoxyDonkeyText(link)

writeArrayToFile('posts.txt', doxyDonkeyPosts)
