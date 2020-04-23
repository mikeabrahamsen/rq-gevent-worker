"""
rq-gevent-worker
================

Implement a new worker based on gevent

Install
-------

.. code-block:: bash

    $ pip install rq-gevent-worker

Usage
-----

.. code-block:: bash

    $ rq-gevent-worker --help

    $ export PYTHONPATH=<your project import path>:$PYTHONPATH; rq-gevent-worker

    # or you can source your virtual env
    $ source venv/bin/activate; rq-gevent-worker

For more information: https://github.com/zhangliyong/rq-gevent-worker
"""
from setuptools import setup

setup(
    name='rq-gevent-worker',
    version='0.2.0',
    py_modules=['rq_gevent_worker'],
    entry_points={
        'console_scripts': [
            'rq-gevent-worker=rq_gevent_worker:main',
            ]
        },
    url='https://github.com/zhangliyong/rq-gevent-worker',
    license='BSD',
    author='',
    author_email='lyzhang87@gmail.com',
    description='Implement a new worker based on gevent',
    long_description=__doc__,
    install_requires=['rq >= 1.2.2', 'gevent >= 20.4.0'],
)
