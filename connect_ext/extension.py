# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Martin Constante
# All rights reserved.
#
from connect.eaas.extension import (
    Extension,
    ProcessingResponse,
)


class Martin01Extension(Extension):

    def approve_asset_request(self, request, template_id):
        # This function is used to approve purchase request;
        # note that only the request parameter is necessary to obtain a required
        # request object

        self.logger.info(f'request_id={request["id"]} - template_id={template_id}')

        # This code instantiates the client,
        # specifies the collection operation, provides request IDs,
        # and defines the required action

        self.client.requests[request['id']]('approve').post(
            {
                'template_id': template_id,
            }
        )
        self.logger.warning(f"Approved request {request['id']}")

        # Note that your project can have different logging levels.

    def process_asset_purchase_request(self, request):
        self.logger.info(f"Obtained Request with id {request['id']}")
        self.logger.info(f"Status {request['status']}")

        if request['status'] == 'pending':
            self.client.requests[request['id']].update(
                {
                    "asset":{
                        "params":[
                            {
                                "id": "param_a",
                                "value": self.config['PARAM_A']
                            },
                            {
                                "id": "param_b",
                                "value": self.config['PARAM_B']
                            }                            
                        ]
                    }
                }
            )
            self.logger.info("Updating fulfillment paramters")
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    