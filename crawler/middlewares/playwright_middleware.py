from scrapy import Request


class PlaywrightMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request: Request, spider):
        request.meta["playwright"] = True

        return None