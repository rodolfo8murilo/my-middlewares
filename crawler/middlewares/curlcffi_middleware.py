import random

from curl_cffi import requests
from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest


class CurlCffiMiddleware:
    
    BROWSERS = [
        "chrome136",
        "chrome124",
        "edge136",
        "safari184",
    ]

   
    def process_request(self, request, spider):

       
        browser = random.choice(self.BROWSERS)

        session = requests.Session(
            impersonate=browser
        )


        try:

            response = session.get(
                request.url,
                headers=request.headers.to_unicode_dict(),
                timeout=30,
                allow_redirects=True,
            )

            return HtmlResponse(
                url=response.url,
                status=response.status_code,
                body=response.content,
                encoding=response.encoding or "utf-8",
                request=request,
            )

        except Exception as e:
            spider.logger.error(e)
            raise IgnoreRequest(str(e))