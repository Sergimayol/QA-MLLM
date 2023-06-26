import os
from utils import config
from preprocessor.parser import Parser


class InputAnalyzer:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.file_extension = self.__get_file_extension()

    def analyze(self) -> str or None:
        if not self.__is_valid_file():
            return None
        parser = Parser(self.input_file, self.file_extension)
        content = parser.parse()
        return content

    def __get_file_extension(self) -> str:
        return self.input_file.split(".")[-1] if "." in self.input_file else None

    def __is_valid_file(self) -> bool:
        if not os.path.isfile(self.input_file):
            return False
        if not self.file_extension:
            return False
        return self.file_extension in config.ALLOWED_EXTENSIONS

    def allowed_extensions(self) -> str:
        return ", ".join(config.ALLOWED_EXTENSIONS)
