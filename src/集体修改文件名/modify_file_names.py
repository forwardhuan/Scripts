#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# ======================================================
# @File:  : 集体修改文件名
# @Author : forward_huan
# @Date   : 2023/1/2 9:29
# @Desc   :
# ======================================================
import os


def rename(old_name, new_name):
    """
    重命名

    :param old_name:
    :param new_name:
    :return:
    """
    print(f"{old_name} --> {new_name}")
    try:
        os.rename(old_name, new_name)
        pass
    except Exception as ex:
        print("\t", ex)


def get_name_info(root_path: str, file_name: str):
    """
    返回文件名称信息

    :param root_path:
    :param file_name:
    :return:
    """
    new_name = file_name
    return os.path.join(root_path, file_name), os.path.join(root_path, new_name)


def run():
    root_path = r"F:\video\Python从入门到精通教程-黑马程序员"
    for file in os.listdir(root_path):
        old_name, new_name = get_name_info(root_path, file)
        rename(old_name, new_name)


if __name__ == '__main__':
    run()
