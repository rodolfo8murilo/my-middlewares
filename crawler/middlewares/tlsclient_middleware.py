import random
import gzip


import tls_client
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse


class TLSClientMiddleware:

    CLIENT_IDENTIFIERS = [
        "chrome_120",
        "chrome_124",
        "chrome_131",
        "firefox_120",
        "safari_16_0",
    ]

    def process_request(self, request, spider):

        client = tls_client.Session(
            client_identifier=random.choice(self.CLIENT_IDENTIFIERS),
            random_tls_extension_order=True,
        )

        headers = request.headers.to_unicode_dict()
        headers["Accept-Encoding"] = "identity"

        try:
            response = client.get(
                request.url,
                headers=headers,
                timeout_seconds=30,
                allow_redirects=True,
            )
            
            content = response.text.encode("utf-8")
               

            return HtmlResponse(
                url=response.url,
                status=response.status_code,
                headers=response.headers,
                body=content,
                encoding="utf-8",
                request=request,
            )

        except Exception as e:
            spider.logger.exception(e)
            raise IgnoreRequest(str(e))