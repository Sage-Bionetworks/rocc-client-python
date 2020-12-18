from __future__ import print_function

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
        api.create_tag(tag_id, tag=roccclient.Tag())
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
    try:
        api.create_organization(
            org_id,
            organization=org
        )
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

    person = api.create_person(person=person)
    return person.person_id


def add_challenge(api, challenge, persons):
    """Create a new Challenge entry in the database.

    TODO:
        Use 'name' property to check for duplicates
    """

    # Replace challenge.organizers with properly-formatted list
    organizers = [
        persons.get(person.get("firstName") + person.get("lastName"))
        for person in challenge.get("organizers")
    ]
    challenge["organizers"] = organizers

    api.create_challenge(challenge=challenge)


def populate_db(client, dump):
    """Add past challenges from the JSON dump file."""
    tag_api = roccclient.TagApi(client)
    org_api = roccclient.OrganizationApi(client)
    person_api = roccclient.PersonApi(client)
    challenge_api = roccclient.ChallengeApi(client)

    data = json.load(dump)

    # Add 5ms of sleep so connection does not time out.
    tags = data.get("tags")
    for tag in tags:
        add_tag(tag_api, tag)
        time.sleep(0.05)

    organizations = data.get("organizations")
    for _, org in organizations.items():
        add_organization(org_api, org)
        time.sleep(0.05)

    person_ids = {}
    persons = data.get("persons")
    for person in persons:
        person_id = add_person(person_api, person, organizations)
        name = person.get("firstName") + person.get("lastName")
        person_ids[name] = person_id
        time.sleep(0.05)

    challenges = data.get("challenges")
    for challenge in challenges:
        add_challenge(challenge_api, challenge, person_ids)
        time.sleep(0.05)


def main():
    """Main function."""

    configuration = roccclient.Configuration(
        host="http://10.41.27.32:8080/api/v1"  # prod
        # host="http://localhost:8080/api/v1"  # dev
    )
    json_filename = "past_dream_challenges.json"
    with roccclient.ApiClient(configuration) as api_client, \
            open(json_filename) as json_dump:
        populate_db(api_client, json_dump)


if __name__ == "__main__":
    main()
