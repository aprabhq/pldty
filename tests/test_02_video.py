#!/usr/bin/env python3

import sys
from os import path, system

sys.path.append(path.abspath(
    path.join(path.dirname(__file__), path.pardir)
))

from ytdl.utils.config import load_config # noqa
from ytdl.main import get_video  # noqa

conf = load_config()
store_dir = conf['store_dir']
video_dir = f'{store_dir}/video'


def test_video_with_id():
    vid = 'AWNI9AN5ZT4'
    system(f'poetry run python ytdl_entrypoint.py v {vid}')

    index_file = f'{video_dir}/ytdl test 1.mp4'
    assert path.exists(index_file)


def test_video_with_url():
    vid = 'AWNI9AN5ZT4'
    url = f'https://www.youtube.com/watch?v={vid}'
    system(f'poetry run python ytdl_entrypoint.py v {url} my_custom_name')

    index_file = f'{video_dir}/my_custom_name.mp4'
    assert path.exists(index_file)


def test_video_with_index_list():
    index_file_path = f'{store_dir}/my_custom_name.json'

    args = [
        'poetry',
        'run',
        'python',
        'ytdl_entrypoint.py',
        'video',
        '--index_file', index_file_path,
        '--since', 'UCeizweRva8',
        '--limit', '3',
        '--prefix_name', '"my test"',
        '--prefix_num', '10'
    ]
    cmd = ' '.join(args)
    system(cmd)

    assert path.exists(f'{video_dir}/my test - 10.mp4')
    assert path.exists(f'{video_dir}/my test - 11.mp4')
    assert path.exists(f'{video_dir}/my test - 12.mp4')
