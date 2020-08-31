#!/usr/bin/env python3

import sys
from os import path, system

sys.path.append(path.abspath(
    path.join(path.dirname(__file__), path.pardir)
))

from ytdl.utils.config import load_config # noqa
from ytdl.main import get_playlist  # noqa


def test_playlist_with_id():
    conf = load_config()
    store_dir = conf['store_dir']

    plid = 'PL6UpWSERHPIK3wMVXqotpjOA3G6ulEkv2'
    system(f'poetry run python ytdl_entrypoint.py p {plid}')

    index_file = f'{store_dir}/ytdl testing.json'
    assert path.exists(index_file)


def test_playlist_with_url():
    conf = load_config()
    store_dir = conf['store_dir']

    plid = 'PL6UpWSERHPIK3wMVXqotpjOA3G6ulEkv2'
    url = f'https://www.youtube.com/playlist?list={plid}'
    system(f'poetry run python ytdl_entrypoint.py p {url} my_custom_name')

    index_file = f'{store_dir}/my_custom_name.json'
    assert path.exists(index_file)
