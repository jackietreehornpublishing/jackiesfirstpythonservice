# -*- coding: utf-8 -*-
import argparse
import logging
import logging.handlers

import cherrypy
from requestlogger import WSGILogger, ApacheFormatter
from werkzeug.debug import DebuggedApplication

from mypackage import __version__
from mypackage.service import app
import mypackage.views


def run(host='0.0.0.0', port=8080, debug=False, syslog=None):
    """
    Start the application server and listen for incoming connection.
    """
    configure_logging(app, debug, syslog)

    # serve the Flask app using the CherryPy HTTP server
    cherrypy.tree.graft(app)

    cherrypy.config.update({
      'server.socket_host': host,
      'server.socket_port': port
    })

    if not debug:
        cherrypy.config.update({'environment': 'production'})

    # handle SIGINT/SIGTERM properly
    cherrypy.engine.signals.subscribe()

    # let's dance
    cherrypy.engine.start()
    cherrypy.engine.block()


def configure_logging(app, debug=False, syslog=None):
    """
    Set the appropriate handlers based on the given parameters.

    If `debug` is set, the CherryPy error logger will be set to the `DEBUG`
    level.
    If the `syslog` address is provided, both the CherryPy logger and WSGI
    access logger will forward to it.
    """
    app.debug = debug
    app.use_debugger = debug

    # let's not pollute the root logger
    cherrypy_access_logger = logging.getLogger('cherrypy.access')
    cherrypy_access_logger.propagate = False
    # we can disable the access logger provided by CherryPy since
    # we are not running a pure CherryPy app
    cherrypy_access_logger.disabled = True

    cherrypy_error_logger = logging.getLogger('cherrypy.error')
    cherrypy_error_logger.propagate = False

    if debug:
        cherrypy_error_logger.setLevel(logging.DEBUG)
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    wsgi_handlers = [logging.StreamHandler()]
    if syslog is not None:
        syslog_addr, syslog_port = syslog.rsplit(':', 1)
        syslog_handler = logging.handlers.SysLogHandler(
            address=(syslog_addr, int(syslog_port))
        )
        wsgi_handlers.append(syslog_handler)
        cherrypy_error_logger.handlers.append(syslog_handler)

    app.wsgi_app = WSGILogger(app.wsgi_app, wsgi_handlers, ApacheFormatter())


def parse_commandline():
    parser = argparse.ArgumentParser()

    parser.add_argument('--host', dest='host', action='store',
                        default='0.0.0.0',
                        help='Server binding address.')

    parser.add_argument('--port', dest='port', action='store',
                        default=8080, type=int,
                        help='Server binding port.')

    parser.add_argument('--debug', dest='debug', action='store_true',
                        help='Enable Flask debug mode.')

    parser.add_argument('--version', action='version',
                        version=__version__)

    parser.add_argument('--syslog', action='store',
                        help='Set the remote syslog endpoint')

    return parser.parse_args()


if __name__ == "__main__":  # pragma: no cover
    options = parse_commandline()
    run(options.host, options.port, options.debug, options.syslog)
