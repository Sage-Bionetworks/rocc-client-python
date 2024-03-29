> March 8, 2022: This project has been moved to [Sage-Bionetworks/challenge-registry](https://github.com/Sage-Bionetworks/challenge-registry).

# ROCC Client Library for Python

[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/rocc-client.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-client/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/rocc-client/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-client)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/rocc-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-client)
[![PyPi](https://img.shields.io/pypi/v/rocc-client.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=PyPi&logo=PyPi)](https://pypi.org/project/rocc-client)

# Introduction
TBA


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.4
- Package version: 0.1.5
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://Sage-Bionetworks.github.io/rocc-schemas/latest/docs](https://Sage-Bionetworks.github.io/rocc-schemas/latest/docs)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Sage-Bionetworks/rocc-client
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Sage-Bionetworks/rocc-client`)

Then import the package:
```python
import roccclient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import roccclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)

# Enter a context with an instance of the API client
with roccclient.ApiClient(configuration) as api_client:

    # Create an instance of the API class
    api_instance = roccclient.ChallengeApi(api_client)
    challenge_create_request = roccclient.ChallengeCreateRequest() # ChallengeCreateRequest |

    try:
        # Add a challenge
        api_response = api_instance.create_challenge(challenge_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->create_challenge: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://rocc.org/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChallengeApi* | [**create_challenge**](docs/ChallengeApi.md#create_challenge) | **POST** /challenges | Add a challenge
*ChallengeApi* | [**delete_challenge**](docs/ChallengeApi.md#delete_challenge) | **DELETE** /challenges/{challengeId} | Delete a challenge
*ChallengeApi* | [**get_challenge**](docs/ChallengeApi.md#get_challenge) | **GET** /challenges/{challengeId} | Get a challenge
*ChallengeApi* | [**list_challenges**](docs/ChallengeApi.md#list_challenges) | **GET** /challenges | List all the challenges
*GrantApi* | [**create_grant**](docs/GrantApi.md#create_grant) | **POST** /grants | Create a grant
*GrantApi* | [**delete_grant**](docs/GrantApi.md#delete_grant) | **DELETE** /grants/{grantId} | Delete a grant
*GrantApi* | [**get_grant**](docs/GrantApi.md#get_grant) | **GET** /grants/{grantId} | Get a grant
*GrantApi* | [**list_grants**](docs/GrantApi.md#list_grants) | **GET** /grants | Get all grants
*OrganizationApi* | [**create_organization**](docs/OrganizationApi.md#create_organization) | **POST** /organizations | Create an organization
*OrganizationApi* | [**delete_organization**](docs/OrganizationApi.md#delete_organization) | **DELETE** /organizations/{organizationId} | Delete an organization
*OrganizationApi* | [**get_organization**](docs/OrganizationApi.md#get_organization) | **GET** /organizations/{organizationId} | Get an organization
*OrganizationApi* | [**list_organizations**](docs/OrganizationApi.md#list_organizations) | **GET** /organizations | Get all organizations
*PersonApi* | [**create_person**](docs/PersonApi.md#create_person) | **POST** /persons | Create a person
*PersonApi* | [**delete_person**](docs/PersonApi.md#delete_person) | **DELETE** /persons/{personId} | Delete a person
*PersonApi* | [**get_person**](docs/PersonApi.md#get_person) | **GET** /persons/{personId} | Get a person
*PersonApi* | [**list_persons**](docs/PersonApi.md#list_persons) | **GET** /persons | Get all persons
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /tags | Create a tag
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **DELETE** /tags/{tagId} | Delete a tag
*TagApi* | [**get_tag**](docs/TagApi.md#get_tag) | **GET** /tags/{tagId} | Get a tag
*TagApi* | [**list_tags**](docs/TagApi.md#list_tags) | **GET** /tags | Get all tags
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /users | Create a user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /users/{username} | Delete a user
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /users/{username} | Get a user
*UserApi* | [**list_users**](docs/UserApi.md#list_users) | **GET** /users | Get all users


## Documentation For Models

 - [Challenge](docs/Challenge.md)
 - [ChallengeCreateRequest](docs/ChallengeCreateRequest.md)
 - [ChallengeCreateResponse](docs/ChallengeCreateResponse.md)
 - [ChallengeFilter](docs/ChallengeFilter.md)
 - [ChallengeResults](docs/ChallengeResults.md)
 - [ChallengeStatus](docs/ChallengeStatus.md)
 - [Error](docs/Error.md)
 - [Grant](docs/Grant.md)
 - [GrantCreateRequest](docs/GrantCreateRequest.md)
 - [GrantCreateResponse](docs/GrantCreateResponse.md)
 - [Organization](docs/Organization.md)
 - [OrganizationCreateRequest](docs/OrganizationCreateRequest.md)
 - [OrganizationCreateResponse](docs/OrganizationCreateResponse.md)
 - [PageOfChallenges](docs/PageOfChallenges.md)
 - [PageOfChallengesAllOf](docs/PageOfChallengesAllOf.md)
 - [PageOfGrants](docs/PageOfGrants.md)
 - [PageOfGrantsAllOf](docs/PageOfGrantsAllOf.md)
 - [PageOfOrganizations](docs/PageOfOrganizations.md)
 - [PageOfOrganizationsAllOf](docs/PageOfOrganizationsAllOf.md)
 - [PageOfPersons](docs/PageOfPersons.md)
 - [PageOfPersonsAllOf](docs/PageOfPersonsAllOf.md)
 - [PageOfTags](docs/PageOfTags.md)
 - [PageOfTagsAllOf](docs/PageOfTagsAllOf.md)
 - [PageOfUsers](docs/PageOfUsers.md)
 - [PageOfUsersAllOf](docs/PageOfUsersAllOf.md)
 - [Person](docs/Person.md)
 - [PersonCreateRequest](docs/PersonCreateRequest.md)
 - [PersonCreateResponse](docs/PersonCreateResponse.md)
 - [PersonFilter](docs/PersonFilter.md)
 - [ResponsePageMetadata](docs/ResponsePageMetadata.md)
 - [ResponsePageMetadataLinks](docs/ResponsePageMetadataLinks.md)
 - [Tag](docs/Tag.md)
 - [TagCreateRequest](docs/TagCreateRequest.md)
 - [TagCreateResponse](docs/TagCreateResponse.md)
 - [TagFilter](docs/TagFilter.md)
 - [User](docs/User.md)
 - [UserCreateRequest](docs/UserCreateRequest.md)
 - [UserCreateResponse](docs/UserCreateResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Authors

- thomas.schaffter@sagebionetworks.org
- verena.chung@sagebase.org


