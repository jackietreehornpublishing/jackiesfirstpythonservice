# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name = "mypackage",
      version = "0.0.1",
      description = "$description",
      maintainer = "russmiles",
      maintainer_email = "russ@russmiles.com",
      url = "myurl",
      packages = ["mypackage"],
      platforms = ["any"],
      long_description = "$description"
     )
