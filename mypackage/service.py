# -*- coding: utf-8 -*-
import socket

from flask import Flask, jsonify

from mypackage.swagger import spec


__all__ = ['app', 'spec']


app = Flask(__name__)


@app.route('/api')
def swagger():
    return jsonify(spec.to_dict())


@app.route('/info')
def info():
    """
    Some metadata regarding this service.
    """
    return jsonify({
        "app": {
            "version": "0.0.1",
            "group_id": "jackietreehornpublishing",
            "artifact_id": "jackiesfirstpythonservice"
        },
        "git": {
            "branch": "",
            "commit": {
                "id": "",
                "time": ""
            }
        },
        "sys": {
            "host": socket.gethostname()
        }
    })


@app.route('/health')
def health():
    """
    Responds with the current's service health.

    Could be used by the liveness probe of a Kubernetes cluster for instance.
    """
    # put some logic here to decide if your app is doing well or not
    # by default, we'll always return everything is okay!
    return ""


@app.route('/status')
def status():
    """
    Responds with the current's service health.

    Could be used by the readiness probe of a Kubernetes cluster.
    """
    # put some logic here to decide if your app is doing well or not
    # by default, we'll always return everything is okay!
    return ""