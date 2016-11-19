import http.client, urllib.request, urllib.parse, urllib.error, base64
class GetImage:

    def __init__(self, key):
        self.key = key

    def getImage(self, keywords):

        search_string = ""
        for x in keywords:
            search_string = search_string + " " + x

        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': self.key,
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'q': search_string,
            'count': '1',
            'offset': '0',
            'mkt': 'en-us',
            'safeSearch': 'Strict',
        })

        try:
            conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
            conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
