from django.db import models

class User(models.Model):
    Rollnumber = models.CharField(max_length=300)
    DOB = models.CharField(max_length=300)
    Name= models.CharField(max_length=300, default='')
    EFFP_UEM= models.CharField(max_length=300, default='')
    EFFP_IAM= models.CharField(max_length=300, default='')
    EFFP_TM = models.CharField(max_length=300, default='')
    EFFP_G = models.CharField(max_length=300, default='')  # Add default value as an empty string
    AIB_UEM = models.CharField(max_length=300, default='')
    AIB_IAM = models.CharField(max_length=300, default='')
    AIB_TM = models.CharField(max_length=300, default='')
    AIB_G = models.CharField(max_length=300, default='')
    FA_UEM = models.CharField(max_length=300, default='')
    FA_IAM = models.CharField(max_length=300, default='')
    FA_TM = models.CharField(max_length=300, default='')
    FA_G = models.CharField(max_length=300, default='')
    AGO_UEM = models.CharField(max_length=300, default='')
    AGO_IAM = models.CharField(max_length=300, default='')
    AGO_TM = models.CharField(max_length=300, default='')
    AGO_G = models.CharField(max_length=300, default='')
    SGO_UEM = models.CharField(max_length=300, default='')
    SGO_IAM = models.CharField(max_length=300, default='')
    SGO_TM = models.CharField(max_length=300, default='')
    SGO_G = models.CharField(max_length=300, default='')
    TTM = models.CharField(max_length=300, default='')
    TIM = models.CharField(max_length=300, default='')
    TCM = models.CharField(max_length=300, default='')
    GT = models.CharField(max_length=300, default='')
    P = models.CharField(max_length=300, default='')
    R = models.CharField(max_length=300, default='')
    NOSF = models.CharField(max_length=300, default='', null=True)
    S = models.CharField(max_length=300, default='', null=True)



























    def __str__(self):
        return self.Rollnumber

    class Meta:
        app_label = 'result'
