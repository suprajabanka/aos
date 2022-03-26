from faker import Faker
fake = Faker(locale='en_CA')

website = 'Advantage Online Shopping'
advantage_url = 'https://advantageonlineshopping.com/#/'
advantage_title = '\xa0Advantage Shopping'


user_name = fake.user_name()
email = f'{user_name}@{fake.free_email_domain()}'
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()
city = fake.city()
address = fake.street_address()
state = fake.province_abbr()
postal_code = fake.postalcode()
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password
description = f'User added by {user_name} via Python Selenium Automated Script'  # fake.sentence(nb_words=100)

# --------------------------- Data Definitions -----------------------------------
account_test_data = {'usernameRegisterPage': user_name, 'emailRegisterPage': email, 'passwordRegisterPage': password,
             'confirm_passwordRegisterPage': password, 'first_nameRegisterPage': first_name, 'last_nameRegisterPage': last_name,
             'phone_numberRegisterPage': phone, 'cityRegisterPage': city, 'addressRegisterPage': address,
             'state_/_province_/_regionRegisterPage': state, 'postal_codeRegisterPage': postal_code}
# --------------------------------------------------------------------------------

