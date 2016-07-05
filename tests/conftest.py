# -*- coding: utf-8 -*-
import pytest

from mypackage.service import app as _app
import mypackage.views


@pytest.fixture(scope='function')
def app():
    _app.testing = True
    return _app.test_client()

