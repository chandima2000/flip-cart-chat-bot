from setuptools import find_packages, setup
from typing import List


def get_requirements() ->List[str]:

    # empty list
    requirement_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            requirement_list = file.read().splitlines()
    except FileNotFoundError:
        print("requirements.txt file not found, continuing without external dependencies.")

    return requirement_list

setup(
    name = "flip-cart-chat-bot",
    version= "0.0.1",
    author="chandima",
    author_email="hychandima727@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)