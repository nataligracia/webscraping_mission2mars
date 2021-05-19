# webscraping_mission2mars
Web scraping and analysis of NASA Mars News, JPL Images, Facts and Hemispheres

![Alt text](static/Mars-1.png?raw=True "Site Top")
![Alt text](static/Mars-2.png?raw=True "Site Bottom")

## Nasa Mars News:
Using Python and BeautifulSoup, the most recent article title and brief description displayed on the top of the NASA Mars News Site is webscrapped on this page. For reference the link has been embedded into the following image on the site:

<br>
https://mars.nasa.gov/news/

![Alt text](static/mission_to_mars.png?raw=True "Mars Image")


## NASA Featured Mars Image:
The featured JPL Mars Space Image is also brought on to this site and the link has been embedded into the image itself.
<br>
https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html

## Mars Facts:
General Mars Facts is included the site using a pandas dataframe table format. For reference the link has been embedded into the title.
<br>
https://space-facts.com/mars/

## Mars Hemispheres:
In order to view the four hemispheres of Mars, the titles and an image of each with the embedded link is also displayed.
<br>
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

# Deployment Preparation
Using MongoDB and a Flask Application, we imported the scrapped data and images through these tools for deployment.