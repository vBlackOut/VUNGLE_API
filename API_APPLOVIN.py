import requests

class API_APPLOVIN():

    def __init__(self):
        self.URL = "https://r.applovin.com/report"
        self.API = requests.Session()
        self.API.keep_alive = False

    def generate_url(self, elements):
        generate_url = ""
        disable_options = ["_print"]
        for key, value in elements.items():
            for a in disable_options:
                if a != key:
                    if type(value) == list:
                        generate_url += "&" + key + "=" + ','.join(value)
                    else:
                        generate_url += "&" + key + "=" + value
                else:
                    print(" NOTICE: Disable options '{}' API for python".format(a))

        return generate_url

    def get(self, **kwargs):
        generate_url = self.generate_url(kwargs)
        resultAPI = self.API.get('{0}?api_key={1}{2}'.format(self.URL, 
                                                             self.api_key, 
                                                             generate_url))
        self.Close()
        if kwargs["_print"] == True:
            print(resultAPI.headers, resultAPI.text)
        return resultAPI.text

    def Close(self):
        self.API.close()