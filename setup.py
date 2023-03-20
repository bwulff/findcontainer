from setuptools import setup, find_packages

setup(
    name='findcontainer',
    version='0.1',
    package_dir={"": "src"},
    packages=find_packages("src/"),
    include_package_data=True,
    install_requires=[
        'click', 'docker'
    ],
    entry_points='''
        [console_scripts]
        findcontainer=findcontainer.cli:cli
    ''',
)
