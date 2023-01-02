#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# ======================================================
# @File:  : chinese_to_pinyin
# @Author : forward_huan
# @Date   : 2023/1/2 18:32
# @Desc   :
# ======================================================

from pypinyin import pinyin, lazy_pinyin, Style

string = "朝阳"

print(pinyin(string, style=Style.NORMAL))
print(pinyin(string, style=Style.TONE))
print(pinyin(string, style=Style.TONE2))
print(pinyin(string, style=Style.TONE3))

print(pinyin(string, style=Style.NORMAL, heteronym=True))
print(pinyin(string, style=Style.TONE, heteronym=True))
print(pinyin(string, style=Style.TONE2, heteronym=True))
print(pinyin(string, style=Style.TONE3, heteronym=True))

print(lazy_pinyin(string, style=Style.NORMAL))
print(lazy_pinyin(string, style=Style.TONE))
print(lazy_pinyin(string, style=Style.TONE2))
print(lazy_pinyin(string, style=Style.TONE3))

