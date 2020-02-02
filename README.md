## Goal
Use BeautifulSoup, Splinter, and Pandas to scrape different webpages related to Mars, and display the results on a webpage using MongoDB and Flask. 
**Scraping Mars Data** 
<img align="right" src="https://github.com/LISASHAH/Mission-to-Mars/blob/master/static/Image_Output.png?raw=true">
For scraping, after importing the necessary dependencies, I connected to the chromedriver and set up my browser to open each webpage I needed to scrape. I first scraped website for the title and text of the most recent article, storing the results in variables to be referenced later. The second page, was the Jet Propulsion Laboratory’s [Mars page](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars), where I would grab the full-sized featured image.Next, was scraping Mars facts from the [Space Facts]( https://space-facts.com/mars/) website.Lastly, I wanted to grab the images and names of all four of Mars’ hemispheres from the [USGS Astrogeology]( https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
) page.

**Flask**
In a separate file, Flask was used to trigger the scrape function, update the Mongo database with the results, and then return that record of data from the database on a webpage. 

**Files**
app.py
index.htm
mission_to_mars.ipynb
scrapping.py
