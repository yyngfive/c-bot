import yaml
from munch import DefaultMunch


def read_config(path: str) -> DefaultMunch:
    with open(path, encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return DefaultMunch.fromDict(config)
