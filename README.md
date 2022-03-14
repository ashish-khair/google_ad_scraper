# Google_ad_scraper
# Ads_scraping
* Used `request` module to get the response from the website url.
* Url contains the user input and search that input on the `http://google.com/`
* Then used `Selenium webdriver` to get the page_source.
* By using that `page_source` we created a soup using `BeautifulSoup`.
* Soup contains the page_source and by using that soup we extract the google ads, which contains text, links and image of that advertisement.
* And saved that data in a JSON file.
