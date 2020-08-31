#!/usr/bin/env python3

import sys
from os import path, system

sys.path.append(path.abspath(
    path.join(path.dirname(__file__), path.pardir)
))

from ytdl.utils.config import load_config # noqa
from ytdl.main import get_audio  # noqa

conf = load_config()
store_dir = conf['store_dir']
audio_dir = f'{store_dir}/audio'


def test_audio_with_id():
    vid = 'RESxNFhYReI'
    system(f'poetry run python ytdl_entrypoint.py a {vid}')

    index_file = f'{audio_dir}/ytdl test 5.mp3'
    assert path.exists(index_file)


def test_audio_with_url():
    vid = 'RESxNFhYReI'
    url = f'https://www.youtube.com/watch?v={vid}'
    system(f'poetry run python ytdl_entrypoint.py a {url} my_custom_name')

    index_file = f'{audio_dir}/my_custom_name.mp3'
    assert path.exists(index_file)


def test_audio_with_index_list():
    index_file_path = f'{store_dir}/my_custom_name.json'

    args = [
        'poetry',
        'run',
        'python',
        'ytdl_entrypoint.py',
        'audio',
        '--index_file', index_file_path,
        '--since', 'gDFxjwqF-Uo',
        '--limit', '3',
        '--prefix_name', '"my test"',
        '--prefix_num', '14'
    ]
    cmd = ' '.join(args)
    system(cmd)

    assert path.exists(f'{audio_dir}/my test - 14.mp3')
    assert path.exists(f'{audio_dir}/my test - 15.mp3')
