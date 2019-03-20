import yaml
import os

class readYaml():

    def __init__(self):

        filepath = os.path.join(os.path.abspath("./"),"accout.yaml")
        print(filepath)
        file = open(filepath,encoding='utf-8')
        res = yaml.load(file)
        print(res)


readYaml()