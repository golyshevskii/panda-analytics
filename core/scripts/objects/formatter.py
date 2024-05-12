from config import PATH


class Formatter:
    """Class for formatting messages

    Attributes:
        template: Template for formatting
    """

    def __init__(self, template_path: str):
        self.template = self._import_template(template_path)

    def _import_template(self, template_path: str) -> str:
        """
        Imports template from file

        Params:
            template_path: Path to the template file
        """
        with open(f"{PATH}{template_path}", "r", encoding="utf-8") as file:
            return file.read()

    def fmessage(self, data: dict) -> str:
        """
        Formats text message

        Params:
            data: Dictionary with values for formatting
        """
        return self.template.format(**data)
