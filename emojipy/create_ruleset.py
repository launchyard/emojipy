#!/usr/bin/env python3
# -*- coding: utf-8; -*-
/* [[[cog
import cog
import json

json_package_path = './emoji.json'

data_dict = json.loads(open(json_package_path).read())

unicode_replace = {}
shortcode_replace = {}
ascii_replace = {}

for key, value in data_dict.items():
    unicode_hex = value['unicode']
    ascii_list = value['aliases_ascii']
    shortname = value['shortname']
    for ascii in ascii_list:
        ascii_replace[ascii] = unicode_hex
    shortcode_replace[shortname] = unicode_hex

    if '-' not in unicode_hex:
        unicode_char = chr(int(unicode_hex, 16))
        unicode_replace[unicode_char.encode('utf-8')] = shortname
    else:
        parts = unicode_hex.split('-')
        unicode_char = ''.join(chr(int(part, 16)) for part in parts)
        unicode_replace[unicode_char.encode('utf-8')] = shortname

print(unicode_replace)
print(shortcode_replace)
print(ascii_replace)
cog.out('unicode_replace = %s' % unicode_replace)
]]] */
//[[[end]]]
