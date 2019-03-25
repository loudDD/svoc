import yaml
import os

class readYaml():

    def __init__(self,filename):

        filepath = os.path.join(os.path.abspath("./"),filename)
        # print(filepath)
        file = open(filepath,encoding='utf-8')
        res = yaml.load(file)
        # print(res)


# readYaml()