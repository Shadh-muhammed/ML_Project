from setuptools import setup, find_packages

# Function to load the list of requirements from 'requirements.txt'
def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
    return requirements

# Setting up the package
setup(
    name='ML_Project',  
    version='0.0.1',  # Initial version of your project
    author='shadh',  
    author_email='shadhbnc@gmail.com',  
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=get_requirements('requirements.txt'),  # List of dependencies
)
