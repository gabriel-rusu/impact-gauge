from setuptools import setup, find_packages
from src.utils.constants import Paths


Paths.init_folder_structure()
setup(name='impact-gauge',
      packages=find_packages(where='src'),
      package_dir={'': '.'},
      version='0.0.1',
      install_requires=[], )