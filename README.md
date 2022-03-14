# Google_ad_scraper
# Ads_scraping
* Used `request` module to get the response from the website url.
* Then used `Selenium webdriver` to get the page_source.
* By using that `page_source` we created a soup using `BeautifulSoup`.
* Soup contains the page_source and by using that soup we extract the google ads, which contains text, link and img for the ad.
* And save that data in a JSON file.
