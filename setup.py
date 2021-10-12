from setuptools import setup, find_packages

required = [
    'alembic==1.2.1',
    'click',
    'Flask==1.1.1',
    'Flask-Cors==3.0.8',
    'numpy',
    'opencv-contrib-python==4.2.0.32',
    'opencv-python==3.4.2.16',
    'PyMySQL==0.9.3',
    'requests==2.22.0',
    'scikit-image',
    'SQLAlchemy==1.3.10',
    'twilio==6.32.0',
    'pytest',
    'factory-boy',
]

setup(
    name='ipt_pk',
    version='0.5.2',
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    install_requires=required,
    entry_points='''
        [console_scripts]
        ipt=ipt_pk.ipt:cli
    ''',
)