# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Martin Constante
# All rights reserved.
#

from connect_ext.extension import Martin01Extension


def test_process_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Martin01Extension(client, logger, config)
    result = ext.process_asset_purchase_request(request)
    assert result.status == 'success'
