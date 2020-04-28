rq-gevent-worker
================

Implement a new rq worker based on gevent

Install
-------

```bash
    # create virtualenv
    $ python3 -m venv venv

    # install via pip
    $ pip install -e git+https://github.com/mikeabrahamsen/rq-gevent-worker@master#egg=rq-gevent-worker
```
Usage
-----

```bash
    # activate virtualenv
    $ source venv/bin/activate

    # check cli options
    $ rq-gevent-worker --help
    $ rq-gevent-worker
```

##Test

    $ pip install -r requirements.txt

    $ py.test tests

##TODO

* Add a command line option to specify gevent pool size

###Crash
The official `Worker` uses `os.fork()` to spawn a child process to execute a job,
so if the job cause the process to crash, the worker process is still alive.

When using gevent essentially we are allowing multiple to be actively run at the
same time on a single process.  A side effect of this is that if a job 
causes the process to crash, then all of the other jobs running on 
that process may also crash.

###Why not use `rqworker -w <geventworker>`
Because we need gevent monkey patch to be imported at the start of the process. 
rqworker will import many modules before importing geventworker, 
so it will may cause geventworker to not work normally.


Most of the code is from [lechup](https://gist.github.com/lechup/d886e89490b2f6c737d7) and [jhorman](https://gist.github.com/jhorman/e16ed695845fca683057), 
