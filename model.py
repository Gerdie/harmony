import json


class HAR_Request(object):
    """Response captured in HAR entry"""

    def __init__(self, req_dict):
        self.cookies = req_dict.get('cookies')
        self.url = req_dict.get('url')
        self.query = req_dict.get('queryString')
        self.headers = req_dict.get('headers')
        self.method = req_dict.get('method')


class HAR_Response(object):
    """Response captured in HAR entry"""

    def __init__(self, res_dict):
        self.status = res_dict.get('status')
        self.status_text = res_dict.get('statusText')
        self.comment = res_dict.get('comment')
        self.cookies = res_dict.get('cookies')
        self.content = res_dict.get('content')


class Entry(object):
    """An entry in an HAR log"""

    def __init__(self, entrydict):
        self.server_ip = entrydict.get('serverIPAddress')
        self.start = entrydict.get('startedDateTime')
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