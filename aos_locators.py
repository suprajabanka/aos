from faker import Faker
fake = Faker(locale='en_CA')

website = 'Advantage Online Shopping'
advantage_url = 'https://advantageonlineshopping.com/#/'
advantage_title = '\xa0Advantage Shopping'

#------------------ locators section-------------------------------
first_name = fake.first_name()
last_name = fake.last_name()
username = f'{(first_name + last_name[0:1]).lower()}'
email = f'{username}@happy.ca'
password = fake.password()
phone = fake.phone_number()
city = fake.city()
address = fake.street_address()
province = 'B.c'
postal_code = fake.postalcode()

# --------------------------- Data Definitions -----------------------------------
account_test_data = {'usernameRegisterPage': username, 'emailRegisterPage': email, 'passwordRegisterPage': password,
             'confirm_passwordRegisterPage': password, 'first_nameRegisterPage': first_name, 'last_nameRegisterPage': last_name,
             'phone_numberRegisterPage': phone, 'cityRegisterPage': city, 'addressRegisterPage': address,
             'state_/_province_/_regionRegisterPage': province, 'postal_codeRegisterPage': postal_code}
# ----------------------------------------------------------






