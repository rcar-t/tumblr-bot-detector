from dataclasses import dataclass
import yaml

@dataclass
class RequestConfig: 
    api_base_url: str
    oauth_base_url: str
    oauth_uri: str

@dataclass
class TumblrConfig: 
    requests: RequestConfig

def load_config(): 
    with open("config.yaml", "r") as f: 
        config = yaml.load(f, Loader=yaml.FullLoader)
    print(config)
    return config