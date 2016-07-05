# -*- coding: utf-8 -*-
from mypackage.service import app


__all__ = ['hello']


@app.route("/")
def hello():
    return "Hello!"
