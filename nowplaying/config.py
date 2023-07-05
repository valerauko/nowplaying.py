#coding=utf-8

import os
import yaml

def read_config(path = 'config.yaml'):
    file_path = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__), '..', path))
    with open(file_path, 'r') as stream:
        return yaml.safe_load(stream)
