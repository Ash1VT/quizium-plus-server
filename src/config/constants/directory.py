from pathlib import Path

SRC_DIRECTORY = Path(__file__).resolve().parent.parent.parent
BASE_DIRECTORY = SRC_DIRECTORY.parent
ENV_DIRECTORY = BASE_DIRECTORY / "env"
LOGS_DIRECTORY = BASE_DIRECTORY / "logs"
