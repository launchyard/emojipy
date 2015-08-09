# -*- coding: utf-8; -*-
import re
from html import escape
from .ruleset import unicode_replace,\
    shortcode_replace


class Emoji(object):

    ascii = False
    unicode_alt = True
    image_type = 'png'
    cache_bust_param = '?v=1.2.5'
    sprites = False
    image_png_path = '//cdn.jsdelivr.net/emojione/assets/png/'
    image_svg_path = '//cdn.jsdelivr.net/emojione/assets/svg/'
    image_path_svg_sprites = './asserts/sprites/emojione.sprites.svg'
    ignored_regexp = '<object[^>]*>.*?<\/object>|<span[^>]*>.*?<\/span>|<(?:object|embed|svg|img|div|span|p|a)[^>]*>'
    unicode_regexp = "(" + '|'.join([x.decode('utf-8') for x in unicode_replace]) + ")"
    shortcode_regexp = ':([-+\\w]+):'
    shortcode_compiled = re.compile(ignored_regexp+"|("+shortcode_regexp+")",
                                    re.IGNORECASE)
    unicode_compiled = re.compile(ignored_regexp+"|("+unicode_regexp+")",
                                  re.UNICODE)

    @classmethod
    def to_image(cls, text):
        text = cls.unicode_to_image(text)
        text = cls.shortname_to_image(text)

        return text

    @classmethod
    def unicode_to_image(cls, text):
        def replace_unicode(match):
            unicode_char = text[match.start():match.end()]
            unicode_encoded = unicode_char.encode('utf-8')
            if not unicode_encoded or unicode_encoded not in unicode_replace:
                return unicode_char  # unsupported unicode char
            shortcode = unicode_replace[unicode_encoded]
            if cls.unicode_alt:
                alt = unicode_char
            else:
                alt = shortcode
            filename = shortcode_replace[shortcode].upper()

            if cls.image_type == 'png':
                if cls.sprites:
                    return '<span class="emojione-%s" title="%s">%s</span>'\
                        % (filename, escape(shortcode), alt)
                else:
                    return '<img class="emojione" alt="%s" src="%s"/>' % (
                        alt,
                        cls.image_png_path+filename+'.png'+cls.cache_bust_param
                    )
            else:
                if cls.sprites:
                    return '<svg class="emojione"><description>%s</description>\
                    <use xlink:href="%s#emoji-%s"</use></svg>' % (
                        alt, cls.image_path_svg_sprites, filename)
                else:
                    return '<object class="emojione" data="%s" \
                    type="image/svg+xml" standby="%s"> %s</object>' % (
                        cls.image_svg_path+filename+'.svg'+cls.cache_bust_param, alt, alt)

        text = re.sub(cls.unicode_compiled, replace_unicode, text)
        return text

    @classmethod
    def shortname_to_image(cls, text):
        pass
