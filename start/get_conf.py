# coding:utf-8
import yaml
import os
import glob

def get_project_root() -> str:
    """ return project root """
    dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    print(dir_path)
    return dir_path

project_path = get_project_root()
conf_file_list = glob.glob(f"{project_path}/conf/*.yaml")
conf = {}
for file_path in conf_file_list:
    with open(file_path, "r") as f:
        each = yaml.safe_load(f.read())
    conf.update(each)

rabbitmq_conf = conf.get("rabbitmq")
