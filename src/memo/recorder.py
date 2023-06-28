import os
import logging
import sqlite3
from datetime import datetime
from utils.config import DB_CONFIG

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Recorder:
    def __init__(self) -> None:
        self.db_name = DB_CONFIG["db_name"]
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except Exception as e:
            LOGGER.error(f"Error connecting to database: {e}")

    def create_db(self) -> None:
        pass

    def drop_db(self) -> None:
        pass

    def create_new_conversation(self, conversation_id: str, context: str) -> None:
        pass

    def add_message(self, conversation_id: str, message: str) -> None:
        pass
