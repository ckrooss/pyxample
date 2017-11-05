#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from unittest import TestCase, main
from ..lib.common import encode, decode, twice
from hypothesis import given
from hypothesis.strategies import text, integers


class TestEncodeDecode(TestCase):
    @given(text())
    def test_encode_decode(self, s):
        print(s)
        self.assertEqual(decode(encode(s)), s)

    def test_empty_encoding(self):
        self.assertEqual(encode(None), "null")

    @given(integers())
    def test_twice(self, n):
        self.assertEqual(twice(n), 2 * n)


if __name__ == '__main__':
    main()
