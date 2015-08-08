# -*- coding: utf-8; -*-


class Emoji(object):

    @staticmethod
    def to_image(cls, _str):
        _str = cls.unicode_to_image(_str)
        _str = cls.shortname_to_image(_str)

        return _str

    @staticmethod
    def unicode_to_image(cls, _str):
        pass

    @staticmethod
    def shortname_to_image(cls, _str):
        pass
