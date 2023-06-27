"""
"""
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Parser:
    def __init__(self, document: str, extension: str):
        self.document = document
        if not document:
            raise Exception("Invalid document, file is not specified")
        self.extension = extension

    def parse(self) -> str or None:
        if self.extension == "txt":
            return self.__parse_txt()
        elif self.extension == "md":
            return self.__parse_md()
        elif self.extension == "html":
            return self.__parse_html()
        elif self.extension == "pdf":
            return self.__parse_pdf()
        else:
            # It should never happen
            raise Exception("Invalid extension")

    def __read_file(self) -> str or None:
        content = None
        try:
            with open(self.document, "rb") as f:
                content = f.read().decode("utf-8")
        except Exception as e:
            LOGGER.error(f"Error while reading document: {e}")

        return content

    def __remove_patterns(self, content: str, patterns: list) -> str:
        import re

        for pattern in patterns:
            content = re.sub(pattern, "", content)
        return content

    def __parse_txt(self) -> str or None:
        return self.__read_file()

    def __parse_md(self) -> str:
        # TODO: Improve this to allow to process more complex markdown files
        content = self.__read_file()
        # Get rid of markdown syntax
        patterns = [
            r"#",
            r"\*",
            r"_",
            r"`",
            r"```",
            r"~~",
            r">",
            r"=",
            r"\+",
            r"-",  # Maybe we want to keep this one
            r"\d\.",
            r"\d\)",
            r"\[",
            r"\]",
            r"\(",
            r"\)",
            r"\|",
        ]
        content = self.__remove_patterns(content, patterns)
        return content

    def __parse_html(self) -> str:
        pass

    def __parse_pdf(self) -> str:
        from tika import parser

        content = None
        try:
            parsed = parser.from_file(self.document)
            # Get only the content and ignore the metadata
            content = parsed["content"]
            patterns = [
                r"(\n\s+){2,}",
                r"(\n){2,}",
                r"(\t){2,}",
                r"(\r){2,}",
                r"(\s){2,}",
            ]
            content = self.__remove_patterns(content, patterns)
        except Exception as e:
            LOGGER.error(f"Error while parsing pdf: {e}")

        return content
