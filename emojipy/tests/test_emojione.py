# -*- coding: utf-8; -*-

from unittest import TestCase
from emojipy import Emoji


class EmojipyTest(TestCase):
    def setUp(self):
        pass

    def test_unicode_to_image(self):
        txt = 'Hello world! 😄 :smile:'
        expected = """Hello world! <img class="emojione" alt="😄" src="//cdn.jsdelivr.net/emojione/assets/png/1F604.png%s"/> :smile:""" %\
                   Emoji.cache_bust_param

        self.assertEqual(Emoji.unicode_to_image(txt), expected)
