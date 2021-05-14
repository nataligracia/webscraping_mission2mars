#Use Jupyter Notebook to scrap information

from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import time
import re
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    
    #Initiatie driver
    browser = Browser("chrome", executable_path=ChromeDriverManager().install(), headless=True)
    nasa_news_title, nasa_story_article = mars_news(browser)

    #Run all scraping
    data = {"nasa_news_title": nasa_news_title,
            "nasa_story_article": nasa_story_article,
            "featured_image": featured_image(browser),
            "facts": mars_facts(),
            "hemispheres": hemispheres(browser),
            "last_modified": dt.datetime.now()}
    
    #Stop webdriver and return scraped data
    browser.quit()
    return data


def mars_news(browser):
    
    url_news = "https://mars.nasa.gov/news/"
    browser.visit(url_news)
    
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=3)
    
    html_news = browser.html
    soup_news = bs(html_news, "html.parser")
    
    try:
        news = soup_news.select_one("ul.item_list li.slide")
        nasa_news_title = news.find('div', class_="content_title").get_text()
        nasa_story_article = news.find('div',class_="article_teaser_body").get_text()
    
    except AttributeError:
        return None, None
    
    
    return nasa_news_title, nasa_story_article
   
    
def featured_image(browser):
    
    url_img = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url_img)
    
    find_image = browser.find_by_css('a[class="showimg fancybox-thumbs"]', wait_time=3)
    html_img= find_image[0]['href']
    
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg'
    
    return featured_image_url


def mars_facts():
    
    df = pd.read_html("https://space-facts.com/mars/")[0]
        
    df.columns=['Description','Value']
    df.set_index('Description',inplace=True)
    
    return df.to_html()


def hemispheres(browser):
    
    url_hem = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hem)
    
    #Loop for hemispheres
    hem_urls = []

    links = browser.find_by_css("a.product-item h3")

    for title in range(len(links)):
        hemisphere ={}

        browser.find_by_css("a.product-item h3")[title].click()

        hem_link = browser.find_link_by_text('Sample').first

        hemisphere['title'] = browser.find_by_css("h2.title").text

        hemisphere['img_url'] = hem_link['href']

        hem_urls.append(hemisphere)

        #Navigate backwards
        browser.back()
    
    return hem_urls


if __name__ == "__main__":
    
    print(scrape())