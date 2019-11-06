from setuptools import setup, find_packages

setup(
    name='ipt_pk',
    version='0.3.4',
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ipt=ipt_pk.ipt:main
    ''',
)