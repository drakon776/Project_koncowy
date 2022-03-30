from django.db.models import Model, CharField, IntegerField, TextField, CASCADE, OneToOneField, ForeignKey
from django.contrib.auth.models import User


class Client(Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    phone_number = CharField(max_length=128)
    address = CharField(max_length=128)
    email = CharField(max_length=128)

    def __str__(self):
        return self.name + " " + self.surname + " " + self.address


class Service(Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    specialization = CharField(max_length=128)

    def __str__(self):
        return self.name + " " + self.surname + " : " + self.specialization


class FaultType(Model):
    fault_types = (
        ("Inne", "Inne"),
        ("Domofon", "Domofon"),
        ("CCTV", "CCTV"),
        ("Alarm", "Alarm"),
        ("Telewizja", "Telewizja"),
        ("C.O.", "C.O."),
        ("C.W.", "C.W."),
        ("Prace ślusarskie", "Prace ślusarskie"),
        ("Prace Hydrauliczne", "Prace Hydrauliczne"),
    )
    name = CharField(max_length=100, choices=fault_types, default='Inne')
    address = CharField(max_length=128)
    desc = TextField(null=True, blank=True)
    phone = IntegerField(null=True, default='Brak')
    user = ForeignKey(User, null=True, on_delete=CASCADE)

    def __str__(self):
        return self.address


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    telephone = TextField()
