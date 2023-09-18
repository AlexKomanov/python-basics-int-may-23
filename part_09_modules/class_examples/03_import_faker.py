from faker import Faker
from mimesis import Person

fake_data_gen = Faker()
person = Person()

print(fake_data_gen.name())
print(fake_data_gen.address())

print(person.name(), person.last_name(), person.academic_degree())
