import yaml
from config import PATH


class Configurator:
    """
    Class for working with config from yaml file

    Attributes:
        config: Config imported from yaml file
    """

    def __init__(self, config_path: str):
        self.config = self._import_config(config_path)

    def _import_config(self, yaml_path: str) -> dict:
        """
        Imports config from yaml file

        Params:
            yaml_path: Path to the yaml file
        """
        with open(f"{PATH}{yaml_path}", "r") as file:
            return yaml.safe_load(file)

    def get(self) -> dict:
        """Returns config imported from yaml file"""
        return self.config
