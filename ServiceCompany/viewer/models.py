from django.db.models import Model, CharField


class Client(Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    phone_number = CharField(max_length=128)
    adress = CharField(max_length=128)
    email = CharField(max_length=128)


    def __str__(self):
        return self.name +" "+ self.surname + " " + self.adress

class Service(Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    specialization = CharField(max_length=128)


    def __str__(self):
        return self.name +" "+ self.surname + " : " + self.specialization