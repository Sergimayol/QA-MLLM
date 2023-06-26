"""This module contains the configuration for the application.
It includes:
    - Aplication mode (debug or not) 
    - ML models configuration
    - Database configuration
    - Allowed file extensions for input files
"""

# Aplication mode
DEBUG = True

# ML models configuration
MODELS = {
    "qa": {
        "model_name": "deepset/roberta-base-squad2",
        "tokenizer_name": "deepset/roberta-base-squad2",
        "pipeline_name": "question-answering",
    },
    "summarization": {
        "model_name": "facebook/bart-large-cnn",
        "tokenizer_name": "facebook/bart-large-cnn",
        "pipeline_name": "summarization",
        "framework_name": "pt",
    },
}

# Max length of the qa input
MAX_INPUT_LENGTH = 10000

# Event loop exit key
EXIT_KEY = "q"

# Database configuration
DB_CONFIG = {}

# Allowed file extensions for input files
ALLOWED_EXTENSIONS = set(["txt", "pdf", "html", "md"])
