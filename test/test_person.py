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
from roccclient.models.person import Person  # noqa: E501
from roccclient.rest import ApiException

class TestPerson(unittest.TestCase):
    """Person unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Person
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = roccclient.models.person.Person()  # noqa: E501
        if include_optional :
            return Person(
                id = '507f1f77bcf86cd799439011', 
                first_name = 'John', 
                last_name = 'Smith', 
                email = 'john.smith@example.com'
            )
        else :
            return Person(
                first_name = 'John',
                email = 'john.smith@example.com',
        )

    def testPerson(self):
        """Test Person"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()