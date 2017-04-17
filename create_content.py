import feedparser
import time
import random
import csv
import datetime

NO_OF_MONTHS = 5

def get_articles_from_feeds():
    url_feeds = ["http://feeds2.feedburner.com/redfin_corporate?format=xml",
            "http://rss.cnn.com/rss/money_realestate.rss",
            "http://feeds.feedburner.com/ZillowBlog",
            "http://rss.topix.net/rss/business/real-estate.xml",
            "http://www.realtor.com/news/feed/",
            "http://feeds.feedburner.com/DailyRealEstateNews",
            "http://feeds.bizjournals.com/industry_20",
            "http://feeds.feedburner.com/RealEstateNewsForReal",
            "http://www.costar.com/News/RSS/RSS.aspx",
            "http://feeds.feedburner.com/Rismedia",
            "http://feeds.feedburner.com/realtytimes/TLGO",
            "http://www.biggerpockets.com/renewsblog/feed/",
            "http://realestateinyourtwenties.com/blog/feed/",
            "http://lightersideofrealestate.com/feed",
            "http://www.houzz.com/getGalleries/featured/out-rss",
            "http://feeds.feedburner.com/curbed/BHBe",
            "http://homeguides.sfgate.com/rss/root.xml"]

    articles = []
    count = 0
    for url in url_feeds:
        feed = feedparser.parse(url)
        for post in feed.entries:
            count += 1
            articles.append((post.title, post.link))
            print (post.title)
            print (post.link)
            #print (post.summary)
            print ("===========")
    print ("extracted articles: ", count)
    random.shuffle(articles)
    return articles


def get_schedule(weekday):
    date_today = datetime.date.today()
    days_ahead = weekday - date_today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return date_today + datetime.timedelta(days_ahead)


def write_to_csv(schedule_dates):
    articles = get_articles_from_feeds()
    with open('real_estate_lib.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["date", "message", "url"])
        for article, d in zip(articles, schedule_dates):
            csvwriter.writerow([d.strftime('%Y-%m-%d') + ", 10:00 a.m.", article[0] + " #RealEstate", article[1]])


def main():
    # for tuesday and thursday
    days = [1,3]
    schedule_days = []
    for day in days:
        next_date = get_schedule(day)
        for i in range(15):
            schedule_days.append(next_date + datetime.timedelta(i*7))
    schedule_days.sort()
    write_to_csv(schedule_days)


if __name__=="__main__":
    main()

