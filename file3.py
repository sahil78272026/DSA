from faker import Faker


fake = Faker()

for i in range(10):
    print(fake.name())
    print(fake.address())
    print(fake.zipcode())
    print(fake.country())
    print(fake.city())
    print(fake.date_of_birth(maximum_age=35))
    print('******************')


