# Google_ad_scraper
# Ads_scraping
* Used `request` module to get the response from the website URL.
* Url contains the user input and searched that input on the `http://google.com/`
* Then used `Selenium webdriver` to get the page_source.
* By using that `page_source`, we created a soup using `BeautifulSoup`.
* Soup contains the page_source, and by using that soup, we extract the google ads, which includes text, links, and images of that advertisement.
* And saved that data in a JSON file.
