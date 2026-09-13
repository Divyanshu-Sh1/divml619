from setuptools import find_packages,setup
hypen_e_dot="-e ."
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns list of reqirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n"," ") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements
setup(
name="mlproject2",
version="0.0.1",
authuor_name="divyasnhu",
authour_email="divyanshudcis@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
