from faker import Faker
fake = Faker()
fake.ssn()
print(fake.ssn())

# generate fake address for a specific US state
# print(fake.address_by_state(state_abbr='CA'))

from faker import Faker
fake = Faker("en_US")

address = {
    "street": fake.street_address(),
    "city": fake.city(),
    "state": "NJ",
    "zip": fake.zipcode_in_state(state_abbr="NJ")
}

print(address)
