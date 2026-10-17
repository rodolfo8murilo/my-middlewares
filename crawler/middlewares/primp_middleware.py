
import random
import primp

from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest


class PrimpMiddleware:

    BROWSERS = [
        "chrome_146",
        "chrome_145",
        "edge_146",
        "safari_26",
    ]

    def process_request(self, request, spider):
        browser = random.choice(self.BROWSERS)

        try:
            client = primp.Client(
                impersonate=browser,
                timeout=30,
                follow_redirects=True,
            )

            headers = dict(request.headers.to_unicode_dict())

            response = client.get(
                request.url,
                headers=headers,
            )

            return HtmlResponse(
                url=str(response.url),
                status=response.status_code,
                headers=dict(response.headers),
                body=response.content,
                encoding="utf-8",
                request=request,
            )

        except Exception as e:
            spider.logger.exception(e)
            raise IgnoreRequest(str(e))