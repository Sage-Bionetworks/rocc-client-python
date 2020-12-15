# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import roccclient
from roccclient.models.page_of_organizations import PageOfOrganizations  # noqa: E501
from roccclient.rest import ApiException

class TestPageOfOrganizations(unittest.TestCase):
    """PageOfOrganizations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageOfOrganizations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = roccclient.models.page_of_organizations.PageOfOrganizations()  # noqa: E501
        if include_optional :
            return PageOfOrganizations(
                offset = 56, 
                limit = 56, 
                links = roccclient.models.response_page_metadata_links.ResponsePageMetadata_links(
                    next = '0', ), 
                organizations = [
                    roccclient.models.organization.Organization(
                        organization_id = 'awesome-organization', 
                        name = '0', 
                        short_name = '0', 
                        url = '0', )
                    ]
            )
        else :
            return PageOfOrganizations(
                offset = 56,
                limit = 56,
                links = roccclient.models.response_page_metadata_links.ResponsePageMetadata_links(
                    next = '0', ),
        )

    def testPageOfOrganizations(self):
        """Test PageOfOrganizations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()