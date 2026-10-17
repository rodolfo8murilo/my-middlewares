
from stealth_requests import StealthSession

from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest


class StealthRequestsMiddleware:

    def __init__(self):
        self.session = StealthSession()

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






            