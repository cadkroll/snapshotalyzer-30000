from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Andy Kroll",
    author_email="andy.kroll@tstc.edu",
    description="Snapshotalyzer 30000 is a tool to manage AWS EC2 instances and snapshots",
    packages=['shotty'],
    url="https://github.com/cadkroll/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
