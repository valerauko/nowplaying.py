#coding=utf-8

import yaml

def read():
    with open('config.yaml', 'r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            print("Configuration invalid", e)
