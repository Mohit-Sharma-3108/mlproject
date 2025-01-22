from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """Function to return list of requirements

    Args:
        file_path (str): file path of requirements.txt

    Returns:
        List[str]: list of packages that will be installed
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Mohit Sharma",
    author_email="mohit1d.lp@gmail.com",
    install_reqauires = get_requirements("requirements.txt")
)