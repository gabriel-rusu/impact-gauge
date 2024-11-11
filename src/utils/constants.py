import os.path as osp
from pathlib import Path
from typing import Final


class Paths:
    BASE_DIR: Final[str] = Path(__file__).resolve().parent.parent.parent
    REPOS_DIR: Final[str] = osp.join(BASE_DIR, "repos")
    LOGS_DIR: Final[str] = osp.join(BASE_DIR, "logs")
    CONFIG_DIR: Final[str] = osp.join(BASE_DIR, "config")


    @staticmethod
    def init_folder_structure():
        Path(Paths.REPOS_DIR).mkdir(parents=True, exist_ok=True)
        Path(Paths.LOGS_DIR).mkdir(parents=True, exist_ok=True)
        Path(Paths.CONFIG_DIR).mkdir(parents=True, exist_ok=True)



