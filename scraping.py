#%%
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import requests

#%%
def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver")
    news_title, news_paragraph = mars_news(browser)
    
    # Run all scraping functions and store results in dictionary
    data={}
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "Cerberus_Hemisphere":Cerberus_Hem(browser),
        "Schiaparelli_Hemisphere":Schiaparelli_Hem(browser),
        "Syrtis_Hemisphere":Syrtis_Hem(browser),
        "Valles_Marineris_Hemisphere":Valles_Hem(browser),
        "last_modified": dt.datetime.now()
            }
    
    return data

#%%
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None
    # Assign columns and set index of dataframe
    df.columns=['Description','Value']
    df.set_index('Description',inplace=True)
    mars_html_table = df.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    # Convert dataframe into HTML format, add bootstrap
    return mars_html_table
#%%
def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    try:
         slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
         news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
         news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None
    return news_title, news_p
#%%
def featured_image(browser):
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    try:
        # find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    except AttributeError:
        return None
    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    return img_url
#%%
def Cerberus_Hem(browser):
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        cerberus_img = soup.find('div', class_="wide-image-wrapper")
        pic = cerberus_img.find('li')
        full_img = pic.find('a')['href']
        cerberus_title = soup.find('h2', class_='title').text
        cerberus_heme = {"title": cerberus_title, "img_url": full_img}
    except AttributeError:
        return None    
    return(cerberus_heme)

#%%
def Schiaparelli_Hem(browser):
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        schiaparelli_img = soup.find('div', class_="wide-image-wrapper")
        pic = schiaparelli_img.find('li')
        full_img = pic.find('a')['href']
        schiaparelli_title = soup.find('h2', class_='title').text
        schiaparelli_heme = {"title": schiaparelli_title, "img_url": full_img}
    except AttributeError:
        return None    
    return(schiaparelli_heme)
#%%
def Syrtis_Hem(browser):
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        syrtis_img = soup.find('div', class_="wide-image-wrapper")
        pic = syrtis_img.find('li')
        full_img = pic.find('a')['href']
        syrtis_title = soup.find('h2', class_='title').text
        syrtis_heme = {"title": syrtis_title, "img_url": full_img}
    except AttributeError:
        return None    
    return(syrtis_heme)

#%%
def Valles_Hem(browser):
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        vallesMarineris_img = soup.find('div', class_="wide-image-wrapper")
        pic = vallesMarineris_img.find('li')
        full_img = pic.find('a')['href']
        vallesMarineris_title = soup.find('h2', class_='title').text
        vallesMarineris_hem = {"title": vallesMarineris_title, "img_url": full_img}
    except AttributeError:
        return None    
    return(vallesMarineris_hem)
    
#%%    
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
   

# %%
