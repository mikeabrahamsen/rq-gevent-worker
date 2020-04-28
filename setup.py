"""
rq-gevent-worker
================

Implement a new rq worker based on gevent

Install
-------

    $ pip install -e git+https://github.com/mikeabrahamsen/rq-gevent-worker@master#egg=rq-gevent-worker

Usage
-----

    $ rq-gevent-worker --help

    $ source venv/bin/activate; rq-gevent-worker

For more information: https://github.com/mikeabrahamsen/rq-gevent-worker
"""
from setuptools import setup

setup(
    name='rq-gevent-worker',
    version='0.2.1',
    py_modules=['rq_gevent_worker'],
    entry_points={
        'console_scripts': [
            'rq-gevent-worker=rq_gevent_worker:main',
            ]
        },
    url='https://github.com/mikeabrahamsen/rq-gevent-worker',
    license='BSD',
    author='Lyon Zhang, Michael Abrahamsen',
    author_email='lyzhang87@gmail.com, support@michaelabrahamsen.com',
    description='Implement a new worker based on gevent',
    long_description=__doc__,
    install_requires=['rq >= 1.2.2', 'gevent >= 20.4.0'],
)
