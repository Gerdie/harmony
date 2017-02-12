import json
import random


def generate_random_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


class HAR_Header(object):
    """Header in a Resp/Req"""

    def __init__(self, header):
        self.name = header.get('name')
        self.value = header.get('value')

    @classmethod
    def from_request(cls, header):
        new_header = HAR_Header(header)
        return (new_header.name, new_header.value)


class HAR_Request(object):
    """Response captured in HAR entry"""

    def __init__(self, req_dict):
        self.cookies = req_dict.get('cookies')
        self.url = req_dict.get('url')
        self.query = req_dict.get('queryString')
        self.headers = {k: v for (k, v) in map(HAR_Header.from_request, req_dict.get('headers'))}
        self.method = req_dict.get('method')


class HAR_Response(object):
    """Response captured in HAR entry"""

    def __init__(self, res_dict):
        self.status = res_dict.get('status')
        self.status_text = res_dict.get('statusText')
        # self.headers = res_dict.get('headers')
        self.headers = {k: v for (k, v) in map(HAR_Header.from_request, res_dict.get('headers'))}
        self.comment = res_dict.get('comment')
        self.cookies = res_dict.get('cookies')
        self.content = res_dict.get('content')
        self.body_size = res_dict.get('bodySize', 0)
        self.header_size = res_dict.get('headersSize')


class Entry(object):
    """An entry in an HAR log"""

    def __init__(self, entrydict):
        self.server_ip = entrydict.get('serverIPAddress')
        self.start = entrydict.get('startedDateTime')
        self.timings = entrydict.get('timings')
        self.time = entrydict.get('time')
        self.cache = entrydict.get('cache')
        self.request = HAR_Request(entrydict.get('request', {}))
        self.response = HAR_Response(entrydict.get('response', {}))

    @classmethod
    def from_har(cls, entry):
        return Entry(entry)


class Harmony(object):
    """An HAR file object"""

    def __init__(self, harfile):
        with open(harfile) as f:
            self._har = json.loads(f.read())
        self._log = self._har.get('log', {})
        self._entries = map(Entry.from_har, self._log.get('entries', []))
        self._version = self._log.get('version', '')
        self._creator = self._log.get('creator', {})

    def createDoughnut(self):
        """Create doughnut chart of content types"""

        data = {"labels": [],
                "datasets": [{
                    "data": [],
                    "backgroundColor":[],
                    "hoverBackgroundColor": []
                    }]
                }
        for entry in self._entries:
            if "Content-Type" in entry.response.headers:
                desired = entry.response.headers["Content-Type"].split(";")[0].split("/")[-1].split("+")[0].split("-")[-1]
                if desired not in data["labels"]:
                    data["labels"].append(desired)
                    data["datasets"][0]["data"].append(1)
                    random_color = generate_random_color()
                    data["datasets"][0]["backgroundColor"].append(random_color)
                    data["datasets"][0]["hoverBackgroundColor"].append(random_color)
                else:
                    existing_i = data["labels"].index(desired)
                    data["datasets"][0]["data"][existing_i] += 1
        return data

    def createBar(self):
        """Create bar chart of requests"""

        data = {"labels": [],
                "datasets": [{
                    # "label": "Requests by size in uncompressed bytes",
                    "data": [],
                    "backgroundColor":[],
                    "borderColor": [],
                    "borderWidth": 1,
                    }]
                }
        for entry in self._entries:
            if entry.request.url and entry.response.body_size > 5000:
                print "found entry.request.url"
                print entry.response.body_size
                data["labels"].append(entry.request.url[7:18])
                data["datasets"][0]["data"].append(entry.response.body_size)
        print data
        return data

