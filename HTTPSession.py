import requests

class HTTPSession(object):
    """
    Class that holds the requests session for all api calls.
    """

    def __init__(self):
        requests.packages.urllib3.disable_warnings()
        self.rs = requests.Session()
        self.baseurl = 'http://127.0.0.1:8088'

    def print_resp_info(self, resp):
        """
        Function to print useful info when something goes wrong.
        Prints:
            -URL that was hit.
            -Response body.
            -HTTP response code.
        Args:
            resp (obj): Response object from a request.
        Returns:
        """
        print('INFO: USED URL: {url}'.format(url=resp.url))
        print('INFO: RESPONSE BODY: {resp_body}'.format(resp_body=resp.text))
        print('INFO: RESPONSE STATUS: {status_code}'.format(status_code=resp.status_code))
