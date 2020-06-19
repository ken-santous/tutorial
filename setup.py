from setuptools import setup, find_packages

DEPENDENCIES = open('requirements.txt', 'r').read().split('\n')
README = open('README.md', 'r').read()

setup(
    name='cti_injection',
    version='0.1.0',
    description='Setting up a python package',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='Ken Santous',
    author_email='ken.santous@gmail.com',
    url='https://github.com/ken-santous',
    install_requires=DEPENDENCIES,
    keywords=['security', 'network'],
    packages=find_packages(include=['ucminjection', 'ucminjection.*']),
    extras_require={},
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['myscript=ucminjection.cti_injection:main']

    },
    package_data={'ucminjection': ['data/schema.json']}
)