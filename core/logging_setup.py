import yaml
from pathlib import Path
import logging.config

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def setup_logging():
    log_dir = PROJECT_ROOT / "logs"
    log_dir.mkdir(exist_ok=True)
    
    with open(PROJECT_ROOT / "config" / "logging.yaml", encoding="utf-8") as file:
        logging.config.dictConfig(yaml.safe_load(file))