import urllib.request
import re

class Search:
    def __init__(self):
        pass

    def search(self, title):
        title = title.replace(" ","+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + title)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        return video_ids[0]



if __name__ == '__main__':
    search = Search()
    sid = search.search("House of memories")