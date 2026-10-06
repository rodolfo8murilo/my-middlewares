import scrapy


class ExampleSpider(scrapy.Spider):

    custom_settings = {
        "PLAYWRIGHT_BROWSER_TYPE" : "chromium",

        "PLAYWRIGHT_LAUNCH_OPTIONS" : 
        {
            "headless": True,
        },

        "PLAYWRIGHT_MAX_CONTEXTS" : 4,

        "PLAYWRIGHT_MAX_PAGES_PER_CONTEXT" : 8,
        "DOWNLOAD_HANDLERS" : {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "DOWNLOADER_MIDDLEWARES": {
            "crawler.middlewares.playwright_middleware.PlaywrightMiddleware": 900,
        },

    }
    name = "example"
    start_urls = ["https://webscraper.io/test-sites/pagination"]

    def parse(self, response):
        print(response.text)
