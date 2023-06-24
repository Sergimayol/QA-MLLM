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
MODELS = {}

# Database configuration
DB_CONFIG = {}

# Allowed file extensions for input files
ALLOWED_EXTENSIONS = set(["txt", "pdf", "html", "md"])
