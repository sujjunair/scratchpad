import feedparser
import time

url = "http://www.nytimes.com/pages/technology/index.html?partner=rssnyt"
url = "http://www.washingtonpost.com/wp-dyn/rss/technology/index.xml"
url = "https://www.cnet.com/rss/news/"
url = "http://makezine.com/tag/makerfaire/feed/"
url = "http://www.pmmag.com/rss/topic/2655-bath-kitchen"
url = "http://feeds.feedburner.com/houserepairtalk"
url = "http://knowyourmeme.com/photos.rss"
url = "https://onsizzle.com/rss/donald-trump"
url = "http://www.pctechbytes.com/feed/"
url = "http://www.iicrc.org/article_rss.php"
url = "http://feeds.feedburner.com/meme-meme"
url = "https://www.youtube.com/feeds/videos.xml?channel_id=UCtAGzm9e_liY7ko1PBhzTHA"
url = "http://rss.thisoldhouse.com/web/toh/rss/latestnews/index.xml"
url = "http://feeds.wsjonline.com/wsj/video/most-popular/feed"
url = "http://feeds.thisoldhouse.com/ThisOldHouseHow-toAndRepair?format=xml"
url = "https://thecraftsmanblog.com/feed/"
url = "http://prettyfluffy.com/feed/"
url = "http://www.espn.com/espn/rss/news"

feed = feedparser.parse(url)
for post in feed.entries:
    print (post.title)
    print (post.published)
    print (post.link)
    print (post.summary)
    print ("===========")
#print (feed)
#print (feed.entries[0])
