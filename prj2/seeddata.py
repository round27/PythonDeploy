import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','prj2.settings')

import django 
django.setup()


from myapp.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

#pip install faker
from faker import Faker


fakegen= Faker()

def add_student():
    fake_name=fakegen.name()
    fake_email=fakegen.email()
    fake_dob=fakegen.date()

    std=Student.objects.get_or_create(
        name=fake_name,
        email=fake_email,
        dob=fake_dob
    )[0]
    return std


def populate_data(n=5):
    for x in range(n):
        std=add_student()


if __name__=='__main__':
    print("populating data please wait...")
    print("#"*80)
    populate_data(28)
    print("populating data complete.")
    print("#"*80)
    try:
        User.objects.get_or_create(
            username='lipi',
            password=make_password('1234'),
            email='lipi@love.com',
            first_name='lipi',
            last_name='Last Hasan',
            is_staff=True,
            is_superuser=True,
            is_active=True

            )

        print('User created successfully')
    except:
        print('User already exists!!!')


    

