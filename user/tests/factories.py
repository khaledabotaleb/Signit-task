import factory
from factory import Sequence
from factory.django import DjangoModelFactory

from user.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Sequence(lambda n: u"email{}".format(n))
    full_name = Sequence(lambda n: u"full name{}".format(n))
    # password = Sequence(lambda n: u"password{}".format(n))