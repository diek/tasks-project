import re
from random import choice, randint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

fake = Faker(['en_CA'])


def get_phone_number():
    ''' Faker is not consistent when generating phone numbers
    '''
    phone = fake.phone_number()
    phone_number = re.findall(r'[0-9]+', phone)

    if len(phone_number) == 3:
        phone = "".join(phone_number)
        return f"+1{phone}"
    elif len(phone_number) == 4 and int(phone_number[0]) == 1:
        phone = "".join(phone_number)
        return f"+{phone}"
    else:
        # with extension
        phone = "".join(phone_number)[:-3]
        return f"+1{phone}"


def check_email(*args):
    # Needs to check if email exists
    first_name, last_name = args
    provider_choice = randint(0, 1)
    if provider_choice:
        provider = fake.domain_name()
    else:
        provider = fake.free_email_domain()

    return f"{first_name.lower()}.{last_name.lower()}@{provider}"


def generate_user():
    User = get_user_model()
    password = fake.password()
    male_female = randint(0, 1)
    if male_female:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
    else:
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()

    user_email = check_email(first_name, last_name)
    first_name = first_name
    last_name = last_name
    email = user_email
    joined = choice([24, 48, 72, 96, 120])
    phone_number = get_phone_number()
    user = User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        date_joined=timezone.now() + timezone.timedelta(hours=-joined, seconds=-1),
        last_login=timezone.now(),
        phone_number=phone_number
    )
    return user


class Command(BaseCommand):
    help = 'Generates x number of users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            generate_user()
