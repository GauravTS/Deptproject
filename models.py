from email.headerregistry import Address
from sre_constants import BRANCH
from xmlrpc.client import UNSUPPORTED_ENCODING
from django.db import models

# Create your models here.
class Student(models.Model):
    Name     = models.CharField(max_length=50, null=True)  # max_length = required)  
    USN      = models.CharField(max_length=10)
    Branch   = models.CharField(max_length=10)
    Ph_no    = models.DecimalField(max_digits=10, decimal_places=0)
    Email_id = models.CharField(max_length=50)
    Address  = models.TextField(max_length=100, null=True)

    

class Department(models.Model):
    Dept_name       = models.CharField(max_length=30)  # max_length = required
    Dept_id         = models.CharField(max_length=10)
    Dept_head       = models.CharField(max_length=30)
    