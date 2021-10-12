from django.db import models

# Create your models here.
class semOne(models.Model):
    SUB1 = 'M1'
    SUB2 = 'CHEMISTRY'
    SUB3 = 'ELN'
    SUB4 = 'CPS'
    SUB5 = 'MECH'
    SUB6 = 'ENGLISH'
    WHICH_YEAR = [
        (SUB1, 'M1'),
        (SUB2, 'CHEMISTRY'),
        (SUB3, 'ELN'),
        (SUB4, 'CPS'),
        (SUB5, 'MECH'),
        (SUB6, 'ENGLISH'),
    ]
    select_sub = models.CharField(
        max_length=100,
        choices=WHICH_YEAR
    )
    module_name = models.IntegerField()
    pdf_module = models.FileField(upload_to='sem1media',null=True)
    def __str__(self):
        return self.select_sub

class semTwo(models.Model):
    SUB1 = 'M2'
    SUB2 = 'PHYSICS'
    SUB3 = 'ELE'
    SUB4 = 'CIVIL'
    SUB5 = 'EGDL'
    SUB6 = 'ENGLISH'
    WHICH_YEAR = [
        (SUB1, 'M2'),
        (SUB2, 'PHYSICS'),
        (SUB3, 'ELE'),
        (SUB4, 'CIVIL'),
        (SUB5, 'EGDL'),
        (SUB6, 'ENGLISH'),
    ]
    select_sub = models.CharField(
        max_length=100,
        choices=WHICH_YEAR
    )
    module_name = models.IntegerField()
    pdf_module = models.FileField(upload_to='sem2media',null=True)
    def __str__(self):
        return self.select_sub

class semThree(models.Model):
    SUB1 = 'M3'
    SUB2 = 'DSA'
    SUB3 = 'CO'
    SUB4 = 'ADE'
    SUB5 = 'DMS'
    SUB6 = 'KANNADA'
    WHICH_YEAR = [
        (SUB1, 'M3'),
        (SUB2, 'DSA'),
        (SUB3, 'CO'),
        (SUB4, 'ADE'),
        (SUB5, 'DMS'),
        (SUB6, 'KANNADA'),
    ]
    select_sub = models.CharField(
        max_length=100,
        choices=WHICH_YEAR
    )
    module_name = models.IntegerField()
    pdf_module = models.FileField(upload_to='sem3media',null=True)
    def __str__(self):
        return self.select_sub

class semFour(models.Model):
    SUB1 = 'M4'
    SUB2 = 'DAA'
    SUB3 = 'MCES'
    SUB4 = 'OS'
    SUB5 = 'OOPS'
    SUB6 = 'KANNADA'
    WHICH_YEAR = [
        (SUB1, 'M4'),
        (SUB2, 'DAA'),
        (SUB3, 'MCES'),
        (SUB4, 'OS'),
        (SUB5, 'OOPS'),
        (SUB6, 'KANNADA'),
    ]
    select_sub = models.CharField(
        max_length=100,
        choices=WHICH_YEAR,
    )
    module_name = models.IntegerField()
    pdf_module = models.FileField(upload_to='sem4media',null=True)
    def __str__(self):
        return self.select_sub


