from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'
# This function will return a list of requirements
def get_requirements(filename:str)->List[str]:
    """
    This function will return a list of requirements
    """
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
        
setup(
name = "mlproject",
version = "0.0.1",
author = "Akash",
author_email = "rawatakash750@gmail.com",
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)