mypackage microservice
============================

Getting Started
---------------

This service runs on Python 2.7 or 3.4+. You can execute it locally from a
[virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Once your virtual env is created, install the required dependencies into it:

```
$ pip install -r requirements.txt
```

Next, make sure to locate the service in your `PYTHONPATH`:

```
$ python setup.py develop
```

View the command line arguments:

```
$ python mypackage/main.py --help
```


You can now execute the service as follow:

```
$ python mypackage/main.py
```

By default, the service will listen on port 8080.

Log to syslog
-------------

You can send your application logs to a local or remote syslog as follows:

```
$ python mypackage/main.py --syslog IP:PORT
```

Where `IP:PORT` is the syslog endpoint address. Be aware that this only supports UDP.

Run through a Docker container
------------------------------

You can run the application through a Docker container. First you need to build the image:

```
$ docker build -t mypackage:0.0.1 .
```

Next, you can run it like this:

```
$ docker run --rm -p 8080:8080 -it mypackage:0.0.1
```

You can pass the same arguments as without running from a container.

Execute your tests
------------------

To run your tests, execute the following command:

```
$ cd tests
$ py.test --cov=mypackage --cov-report=html --flake8
```

This will generate a coverage report in the local `htmlcov` directory. In addition, this will also
check for common style issues in your tests based on [PEP-8](https://pypi.python.org/pypi/pep8).

The package ignores a set of rules that are a little too harsh generally speaking. See `setup.cfg`.


Validate your Python style
--------------------------

You can check your code matches [PEP-8](https://pypi.python.org/pypi/pep8) guidelines by running the next command:

```
$ flake8 mypackage
```

Some defaults can be found in `setup.cfg`.

History
-------

Originally created by Atomist on 2016-07-05.

