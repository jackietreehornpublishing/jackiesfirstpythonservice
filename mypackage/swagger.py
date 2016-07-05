# -*- coding: utf-8 -*-
from apispec import APISpec
from marshmallow import Schema, fields


__all__ = ['spec']


spec = APISpec(
    title='mypackage',
    version='0.0.1',
    info=dict(
        description='${description}'
    ),
    plugins=['apispec.ext.marshmallow']
)


spec.add_path(
    path='/',
    operations=dict(
        get=dict(
            responses={
                '200': {
                    'schema': {'type': 'string'}
                }
            }
        )
    )
)
