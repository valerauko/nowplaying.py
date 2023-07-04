#coding=utf-8

import yaml

def read_config(path = 'config.yaml'):
    with open(path, 'r') as stream:
        return yaml.safe_load(stream)
