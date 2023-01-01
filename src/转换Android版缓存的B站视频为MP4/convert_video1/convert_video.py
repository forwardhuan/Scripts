#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# ======================================================
# @File:  : merge_video
# @Author : forward_huan
# @Date   : 2022/12/31 10:48
# @Desc   : 合并Android版B站
# ======================================================
import json
import os

from ffmpy import FFmpeg


def get_video_info(conf_path):
    """
    获取视频名称

    :param conf_path:
    :return:
    """
    with open(conf_path, "r", encoding="utf8") as f:
        conf = json.load(f)
        return conf.get("title"), conf.get("type_tag")


def convert_mp4(output_dir, file_name, audio_path, video_path):
    """
    转换成mp4

    :param output_dir:
    :param file_name:
    :param audio_path:
    :param video_path:
    :return:
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, file_name)
    if os.path.exists(output_path):
        print(f"MP4视频已存在 -> {output_path}")
        return
    try:
        translator = FFmpeg(
            inputs={
                video_path: None,
                audio_path: None
            },
            outputs={
                output_path: "-c:v copy -strict experimental"
            }
        )
        translator.run()
    except Exception as ex:
        print("输出MP4视频失败", ex)
    print(f"输出MP4视频成功 -> {output_path}")


def run():
    root_path = r"F:\硬件安全"
    output_dir = r"F:\纽创信安-硬件安全系列课程"
    # 获取该目录下所有视频
    video_paths = [os.path.join(root_path, item) for item in os.listdir(root_path)]
    for i, dir_path in enumerate(video_paths):
        base_dir = os.path.join(dir_path, os.listdir(dir_path)[0])
        conf_path = os.path.join(base_dir, "entry.json")
        video_name, type_tag = get_video_info(conf_path)
        audio_path = os.path.join(base_dir, type_tag, "audio.m4s")
        video_path = os.path.join(base_dir, type_tag, "video.m4s")
        if video_name:
            video_name = str(video_name).replace(os.path.basename(output_dir) + "-", "")
        file_name = f"{video_name}.mp4"
        print(f"开始转换 --> {video_name}")
        convert_mp4(output_dir, file_name, audio_path, video_path)
        print(f"当前进度： {round((i + 1) * 100 / len(video_paths))}%")


if __name__ == '__main__':
    run()
