
import httpx

from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest


class HttpxMiddleware:

    def __init__(self):
        self.client = httpx.Client(
            timeout=30.0,
            follow_redirects=True,
            http2=True,
        )

    def process_request(self, request, spider):
        try:
 
            headers = request.headers.to_unicode_dict()
            headers["Accept-Encoding"] = "identity"

            response = self.client.request(
                method=request.method,
                url=request.url,
                headers=headers,
                content=request.body or None,
            )

            response_headers = dict(response.headers)
            

            return HtmlResponse(
                url=str(response.url),
                status=response.status_code,
                headers=response_headers,
                body=response.content,
                encoding=response.encoding or "utf-8",
                request=request,
            )

        except Exception as e:
            spider.logger.error(e)
            raise IgnoreRequest(str(e))
