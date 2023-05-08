The access modes available for the open() function are as follows:

r: Opens the file in read-only mode. Starts reading from the beginning of the file and is the default mode for the open() function.
rb: Opens the file as read-only in binary format and starts reading from the beginning of the file. While binary format can be used for different purposes, it is usually used when dealing with things like images, videos, etc.
r+: Opens a file for reading and writing, placing the pointer at the beginning of the file.
w: Opens in write-only mode. The pointer is placed at the beginning of the file and this will overwrite any existing file with the same name. It will create a new file if one with the same name doesn't exist.
wb: Opens a write-only file in binary mode.
w+: Opens a file for writing and reading.
wb+: Opens a file for writing and reading in binary mode.
a: Opens a file for appending new information to it. The pointer is placed at the end of the file. A new file is created if one with the same name doesn't exist.
ab: Opens a file for appending in binary mode.
a+: Opens a file for both appending and reading.
ab+: Opens a file for both appending and reading in binary mode.

# import json
# with open("data/json_example.json") as f:
#      content = f.read()
#      print(content)
#      print(type(content))
#
# print(content["members"])
#
#
# with open("data/json_example.json") as f:
#     content = json.load(f)
#     print(type(content))
#     print(content['members'])
#
# content['members'][0]['name'] = 'ttttttt'
#
# with open("data/json_example_new.json", "w") as f:
#     json.dump(content, f)
#
# with open("data/list_json.json") as f:
#     c = json.load(f)
#     print(type(c))


