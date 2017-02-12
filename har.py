# import json
import os
# import base64

from model import Harmony

ALLOWED_EXTENSIONS = set(['har'])


def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def harmony_open_file(data):
    """Takes data as a string; returns json"""

    return Harmony(data)


demo_path = os.getcwd() + '/static/demo/target_web.har'
harmony = harmony_open_file(demo_path)
print harmony.createDoughnut()
# print harmony._creator
# # print harmony._entries[1].request.url
# # print harmony._entries[1].start, harmony._entries[1].timings, harmony._entries[1].time
# print harmony._entries[2].request.url
# # print harmony._entries[2].request.query
# print harmony._entries[2].request.headers
# print harmony._entries[2].response.headers.keys()
# print harmony._entries[2].response.status
# # print harmony._entries[2].response.content
# # print base64.b64decode(harmony._entries[2].response.content['text'])
# print harmony._entries[2].response.body_size
# # print harmony._entries[2].response.body_size
# print harmony._entries[2].response.header_size, "is the header size"
# print harmony._entries[2].response.content['size']
# print harmony._entries[2].start, harmony._entries[2].timings, harmony._entries[2].time
# print harmony._entries[3].request.url
# print harmony._entries[3].start, harmony._entries[3].timings, harmony._entries[3].time
