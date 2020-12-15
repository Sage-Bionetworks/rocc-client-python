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
from roccclient.models.page_of_challenges_all_of import PageOfChallengesAllOf  # noqa: E501
from roccclient.rest import ApiException

class TestPageOfChallengesAllOf(unittest.TestCase):
    """PageOfChallengesAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageOfChallengesAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = roccclient.models.page_of_challenges_all_of.PageOfChallengesAllOf()  # noqa: E501
        if include_optional :
            return PageOfChallengesAllOf(
                challenges = [
                    roccclient.models.challenge.Challenge(
                        challenge_id = '507f1f77bcf86cd799439011', 
                        name = 'Awesome Challenge', 
                        start_date = 'Mon Nov 09 16:00:00 PST 2020', 
                        end_date = 'Wed Dec 30 16:00:00 PST 2020', 
                        url = 'https://synapse.org/awesome-challenge', 
                        status = 'open', 
                        tags = [
                            'awesome-tag'
                            ], )
                    ]
            )
        else :
            return PageOfChallengesAllOf(
        )

    def testPageOfChallengesAllOf(self):
        """Test PageOfChallengesAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()