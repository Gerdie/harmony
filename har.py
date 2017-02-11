import json
from haralyzer import HarParser, HarPage

ALLOWED_EXTENSIONS = set(['har'])


def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def harmony_open_file(data):
    with open('har_data.har', 'r') as f:
        har_parser = HarParser(json.loads(f.read()))

    print har_parser.browser
    # {u'name': u'Firefox', u'version': u'25.0.1'}

    print har_parser.hostname
    # 'humanssuck.net'

    for page in har_parser.pages:
        assert isinstance(page, HarPage, None)
        # returns True for each
