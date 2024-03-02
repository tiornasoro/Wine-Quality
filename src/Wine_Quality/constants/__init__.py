from pathlib import Path

# Dossier principale du projet
ROOT_DIRECTORY_PATH = Path(__file__).parent.parent.parent.parent / ""
# CONFIG_FILE_PATH = Path("/config/config.yaml")
CONFIG_FILE_PATH = Path(ROOT_DIRECTORY_PATH / "config/config.yaml")

PARAMS_FILE_PATH= Path( ROOT_DIRECTORY_PATH / "params.yaml")
#PARAMS_FILE_PATH= Path("params.yaml")
SCHEMA_FILE_PATH= Path(ROOT_DIRECTORY_PATH / "schema.yaml")