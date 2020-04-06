"""
First of all, make zero dtaabase
For run of seed process,write this in terminal:
    python populate_script.py

This process take minutes.Just be patient)))

"""
import os,django,random

os.environ.setdefault("DJANGO_SETTINGS_MODULE","pcw.settings")
django.setup()

from faker import Faker
from blog.models import Post, User
fake = Faker()

def create_admin():
    username = fake.name()
    password = fake.password()
    email = fake.email()
    user = User.objects.create_user(username,email,password,is_staff=True,is_superuser=True)


def unique_username_generator(testName):
    qs = User.objects.filter(username=testName)
    if qs.exists():
        testName = fake.name()
        return unique_username_generator(testName)
    else:
        return testName

def create_author(N):
    for i in range(N):
        testName = fake.name()
        username = unique_username_generator(testName)
        password = fake.password()
        email = fake.email()
        User.objects.create_user(username,email,password,is_staff=False,is_superuser=False)



def create_posts(N):
    for i in range(N):
        random_id = random.randint(1,100)
        name = fake.name()
        body = fake.text()
        author = User.objects.get(id=random_id)
        Post.objects.create(name=name,body=body,author=author)


create_admin()
create_author(100)
create_posts(1000)

print('Data Is Populated Succesfully!')