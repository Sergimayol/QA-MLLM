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

    def __parse_txt(self) -> str or None:
        content = None
        try:
            with open(self.document, "rb") as f:
                content = f.read().decode("utf-8")
        except Exception as e:
            LOGGER.error(f"Error while parsing txt document: {e}")

        return content

    def __parse_md(self) -> str:
        pass

    def __parse_html(self) -> str:
        pass

    def __parse_pdf(self) -> str:
        pass
