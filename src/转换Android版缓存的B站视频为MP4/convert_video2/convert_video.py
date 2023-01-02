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
        return conf.get("title"), conf.get("page_data").get("part"), str(conf.get("type_tag"))


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
        print(f"\t\tMP4视频已存在 -> {output_path}")
        return
    try:
        translator = FFmpeg(
            inputs={
                video_path: None,
                audio_path: None
            },
            outputs={
                output_path: "-c:v copy -strict experimental"
            },
            global_options="-loglevel quiet"
        )
        translator.run()
    except Exception as ex:
        print("\t\t输出MP4视频失败", output_path)
    print(f"\t\t输出MP4视频成功 -> {output_path}")


def run():
    root_dir = r"F:\B站"
    output_base_dir = r"F:\video"
    # 获取该目录下所有视频
    root_dirs = [os.path.join(root_dir, item) for item in os.listdir(root_dir)]
    for root_path in root_dirs:
        print(f"Root path: {root_path}")
        video_paths = [os.path.join(root_path, item) for item in os.listdir(root_path)]
        for i, dir_path in enumerate(video_paths):
            conf_path = os.path.join(dir_path, "entry.json")
            group, video_name, type_tag = get_video_info(conf_path)
            audio_path = os.path.join(dir_path, type_tag, "audio.m4s")
            video_path = os.path.join(dir_path, type_tag, "video.m4s")
            file_name = f"{video_name}.mp4"
            output_dir = os.path.join(output_base_dir, group)
            print(f"\t开始转换 --> {video_name}")
            convert_mp4(output_dir, file_name, audio_path, video_path)
            print(f"\t当前进度： {round((i + 1) * 100 / len(video_paths))}%")


if __name__ == '__main__':
    run()
