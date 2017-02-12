import urllib.request
import json
import pprint

import bibtrak import handler

class ADS(handler.Handler):
    def fetch(self,id):
        auth_token = self
        bibcode = id

        #request access to the file
        url = (
            "https://api.adsabs.harvard.edu/v1/search/query?q=" +
            bibcode + 
            "&fl=" +
            ",".join([
                "author",
                "title",
                "id",
                "keyword",
                "pubdate",
                "year",
            ])
        )
        req = urllib.request.Request(url)
        req.add_header("Authorization", "Bearer " + auth_token)

        #open page and store info
        response = urllib.request.urlopen(req)
        res = response.read()

        #creating and setting the dictionary
        paper = json.loads(res.decode())
        bib_info = paper['response']['docs'][0]

        #modifying dict
        bib_info["bibcode"] = bibcode
        bib_info["adsurl"] = "http://adsabs.harvard.edu/abs/" + bibcode

        return bib_info

    def authenticate(self, id):
        raise NotImplementedError
