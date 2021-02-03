# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.4
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import roccclient
from roccclient.models.grant_create_request import GrantCreateRequest  # noqa: E501
from roccclient.rest import ApiException

class TestGrantCreateRequest(unittest.TestCase):
    """GrantCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GrantCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = roccclient.models.grant_create_request.GrantCreateRequest()  # noqa: E501
        if include_optional :
            return GrantCreateRequest(
                name = '0', 
                description = '0', 
                url = '0'
            )
        else :
            return GrantCreateRequest(
                name = '0',
        )

    def testGrantCreateRequest(self):
        """Test GrantCreateRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
