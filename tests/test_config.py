#!/usr/bin/env python3

import sys
from os import path, getenv

sys.path.append(path.abspath(
    path.join(path.dirname(__file__), path.pardir)
))

from ytdl.utils.config import get_config, set_config  # noqa


YOUTUBE_API_KEY = getenv('YOUTUBE_API_KEY', '')


def test_config():
    set_config('api_key', YOUTUBE_API_KEY)
    conf = get_config()
    default_config_file = './ptester/.config/ytdl/config.json'
    default_store_dir = './ptester/ytdl_files'

    assert conf['store_dir'] == default_store_dir
    assert path.exists(default_config_file)
    assert path.exists(default_store_dir)

    assert conf['api_key'] == YOUTUBE_API_KEY
