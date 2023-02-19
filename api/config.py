import yaml
from munch import DefaultMunch

def load_config(): 
    with open("config.yaml", "r") as f: 
        config = yaml.load(f, Loader=yaml.FullLoader)
    return DefaultMunch.fromDict(config)

