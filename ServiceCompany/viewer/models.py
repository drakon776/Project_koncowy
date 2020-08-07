from django.db.models import Model, CharField, TextField, CASCADE, OneToOneField, ForeignKey
from django.contrib.auth.models import User



class Client(Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    phone_number = CharField(max_length=128)
    address = CharField(max_length=128)
    email = CharField(max_length=128)

    def __str__(self):
        return self.name +" "+ self.surname + " " + self.address

class Service(Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    specialization = CharField(max_length=128)

    def __str__(self):
        return self.name +" "+ self.surname + " : " + self.specialization

class FaultType(Model):
    name = CharField(max_length=128, null=True)
    address = CharField(max_length=128)
    desc = TextField(null=True, blank=True)

    def __str__(self):
        return self.address


class Profile(Model):
    user =OneToOneField(User,on_delete=CASCADE)
    telephone = TextField()
