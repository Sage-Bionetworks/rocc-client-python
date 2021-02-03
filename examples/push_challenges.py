"""Push Challenge Metadata to Database

Using the ROCC client, this script will add metadata from the DREAM
Landscape to the ROCC database, either to:
  * prod: http://10.41.27.32:8080/api/v1
  *  dev: http://localhost:8080/api/v1 (default)

Assumptions:
  * DREAM Landscape must be in JSON format. If needed, use the
    `reformat_csv_to_json.py` script before using this one.
  * Database is currently empty. If not, it may add duplicate
    entries that do not require uniqueness, e.g. persons
"""

from __future__ import print_function

import argparse
import json
import re
import time

import roccclient
from roccclient.rest import ApiException


def reformat_id(s):
    """Reformat ID string.

    Valid IDs must be lowercase and single dash-delimited.
    """
    s = s.replace("'", "")
    s = re.sub(r"[ \"'\.?!/]", "-", s)
    s = re.sub(r"\-+", "-", s)
    return s.lower()


def add_tag(api, tag):
    """Create a new Tag entry in the database.

    Exception:
        409: tagId already exists
    """
    tag_id = reformat_id(tag.get("tagId"))
    try:
        api.create_tag(tag_id,
                       tag_create_request=roccclient.TagCreateRequest())
    except ApiException as err:
        if err.status == 409:
            print(f"Duplicate tag: {tag_id}")
        else:
            print(f"Exception when calling TagApi->create_tag: {err}")


def add_organization(api, org):
    """Create a new Organization entry in the database.

    Exception:
        409: organizationId already exists
    """

    # Use organization's short name for ID; otherwise, full name.
    org_id = reformat_id(org.get("shortName", org.get("name")))
    org_request = roccclient.OrganizationCreateRequest(
        name=org.get("name"),
        short_name=org.get("shortName"),
        url=org.get("url")
    )
    try:
        api.create_organization(org_id,
                                organization_create_request=org_request)
    except ApiException as err:
        if err.status == 409:
            print(f"Duplicate organization: {org_id}")
        else:
            print("Exception when calling OrganizationApi ->"
                  f"create_organization: {err}")


def add_person(api, person, organizations):
    """Create a new Person entry in the database.

    Returns:
        person.personId

    TODO:
        Use some properties to check for duplicates (maybe email?)
    """

    # Replace person.organizations with properly-formatted list
    person_orgs = [
        reformat_id(organizations.get(org).get("shortName", org))
        for org in person.get("organizations")
    ]
    person["organizations"] = person_orgs

    person = api.create_person(person_create_request=person)
    return person.person_id


def add_challenge(api, challenge, persons):
    """Create a new Challenge entry in the database.

    Exception:
        409: challenge name already exists
    """
    try:
        # Replace challenge.organizers with properly-formatted list
        organizers = [
            persons.get(person.get("firstName") + person.get("lastName"))
            for person in challenge.get("organizers")
        ]
        challenge["organizers"] = organizers
        api.create_challenge(challenge_create_request=challenge)

    except ApiException as err:
        if err.status == 409:
            print(f"Duplicate challenge: {challenge.get('name')}")
        else:
            print("Exception when calling ChallengeApi ->"
                  f"create_challenge: {err}")


def populate_db(client, dump):
    """Add past challenges from the JSON dump file."""
    tag_api = roccclient.TagApi(client)
    org_api = roccclient.OrganizationApi(client)
    person_api = roccclient.PersonApi(client)
    challenge_api = roccclient.ChallengeApi(client)

    data = json.load(dump)

    # Add 5ms of sleep so connection does not time out.
    print("Adding tags...")
    tags = data.get("tags")
    for tag in tags:
        add_tag(tag_api, tag)
        time.sleep(0.05)

    print("Adding organizations...")
    organizations = data.get("organizations")
    for _, org in organizations.items():
        add_organization(org_api, org)
        time.sleep(0.05)

    print("Adding persons...")
    person_ids = {}
    persons = data.get("persons")
    for person in persons:
        person_id = add_person(person_api, person, organizations)
        name = person.get("firstName") + person.get("lastName")
        person_ids[name] = person_id
        time.sleep(0.05)

    print("Adding challenges...")
    challenges = data.get("challenges")
    for challenge in challenges:
        add_challenge(challenge_api, challenge, person_ids)
        time.sleep(1)


def main():
    """Main function."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--prod",
                        action="store_true",
                        help="Push data to the production db if flagged")
    parser.add_argument("-j", "--json_file",
                        type=str, default="past_dream_challenges.json",
                        help="JSON file containing the DREAM Landscape")
    args = parser.parse_args()

    host = "http://10.41.27.32:8080/api/v1" if args.prod \
        else "http://localhost:8080/api/v1"
    configuration = roccclient.Configuration(host=host)
    with roccclient.ApiClient(configuration) as api_client, \
            open(args.json_file) as json_dump:
        populate_db(api_client, json_dump)


if __name__ == "__main__":
    main()
