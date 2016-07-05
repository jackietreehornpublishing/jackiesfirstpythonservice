# -*- coding: utf-8 -*-
import json


def test_swagger_endpoint(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    assert "info" in spec

    info = spec["info"]
    assert "title" in info
    assert info["title"] == "mypackage"
    assert "version" in info
    assert info["version"] == "0.0.1"
    assert "description" in info
    assert info["description"] == "${description}"

    assert "definitions" in spec
    assert len(spec["definitions"]) == 0

    assert "parameters" in spec
    assert len(spec["parameters"]) == 0

    assert "paths" in spec

    paths = spec["paths"]
    assert "/" in paths

    hello_service = paths["/"]
    assert "get" in hello_service

    get_op = hello_service["get"]
    assert "responses" in get_op

    responses = get_op["responses"]
    assert "200" in responses

    response_ok = responses["200"]
    assert "schema" in response_ok

    schema = response_ok["schema"]
    assert schema == {"type": "string"}


def test_health(app):
    rv = app.get('/health')
    assert rv.status_code == 200
    assert b'' in rv.data


def test_info(app):
    rv = app.get('/info')
    assert rv.status_code == 200

    info = json.loads(rv.data.decode('utf-8'), 'utf-8')

    assert "app" in info
    app = info["app"]

    assert "version" in app
    assert app["version"] == "0.0.1"

    assert "group_id" in app
    assert app["group_id"] == "jackietreehornpublishing"

    assert "artifact_id" in app
    assert app["artifact_id"] == "jackiesfirstpythonservice"

    assert "git" in info
    git = info["git"]

    assert "branch" in git
    assert "commit" in git

    assert "commit" in info
    commit = git["commit"]

    assert "id" in commit
    assert "time" in commit
    

def test_hello_service(app):
    rv = app.get('/')
    assert b'Hello!' in rv.data

