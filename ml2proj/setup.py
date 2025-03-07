from setuptools import find_packages,setup 
from typing import List

HYPHEN_E_DOT = '-e .'  # This is the string that is present in the requirements.txt file when the package is installed in editable mode

# Function to get the requirements from a requirements.txt file
def get_requirements(file_path:str)->List[str]:
    requirments =[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        #list comprehension used in below line to remove the new line character from the end of each line
        requirments=[req.replace("\n","") for req in requirments]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)


    return requirments


setup (
    name='ml2proj',
    packages=find_packages(),
    version='0.0.1',
    description='ML2 Project',
    author='asoka',
    license='MIT',
    install_requires= get_requirements('requirements.txt')
)

