# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import roccclient
from roccclient.models.user import User  # noqa: E501
from roccclient.rest import ApiException

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = roccclient.models.user.User()  # noqa: E501
        if include_optional :
            return User(
                id = '507f1f77bcf86cd799439011', 
                username = 'John78', 
                password = '012', 
                first_name = 'John', 
                last_name = 'Smith', 
                email = 'john.smith@example.com', 
                role = 'user', 
                organizations = [
                    roccclient.models.organization.Organization(
                        id = '507f1f77bcf86cd799439011', 
                        name = 'Sage Bionetworks', 
                        url = 'https://sagebionetworks.org/', )
                    ]
            )
        else :
            return User(
                username = 'John78',
                email = 'john.smith@example.com',
        )

    def testUser(self):
        """Test User"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
