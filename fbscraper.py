from facebook_page_scraper import Facebook_scraper
import json

#setting details for scrape
page = "metaai"
posts_count = 1
browser = "chrome"
timeout = 600
headless = False

scrape = Facebook_scraper(page, posts_count, browser, timeout=timeout, headless=headless)

json_data = scrape.scrap_to_json()
print(json.dumps(json_data, indent="\n"))
