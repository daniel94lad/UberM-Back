from django.contrib.auth.models import User
from django.db import models
from postalcode.models import PostalCode

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField()
    avatar = models.ImageField(upload_to='user/pictures', blank=True, null=True)
    active = models.NullBooleanField()
    streetAddress = models.CharField(max_length=40)
    postalCode = models.ForeignKey(PostalCode, on_delete=models.CASCADE, to_field='postalCode', related_name='postalCode_id')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

#   I'm not sure the purpose of this code
#    def _self_(self):
#        return self.email

    def __str__(self):
        return self.user.username