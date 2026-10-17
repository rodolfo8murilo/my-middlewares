
import niquests

from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest


class NiquestsMiddleware:

    def __init__(self):
        self.session = niquests.Session()

    def process_request(self, request, spider):
        try:
            headers = request.headers.to_unicode_dict()
            headers["Accept-Encoding"] = "identity"

            response = self.session.request(
                method=request.method,
                url=request.url,
                headers=headers,
                data=request.body or None,
                timeout=30,
                allow_redirects=True,
            )

            return HtmlResponse(
                url=str(response.url),
                status=response.status_code,
                headers=dict(response.headers),
                body=response.content,
                encoding=response.encoding or "utf-8",
                request=request,
            )

        except Exception as e:
            spider.logger.error(e)
            raise IgnoreRequest(str(e))
