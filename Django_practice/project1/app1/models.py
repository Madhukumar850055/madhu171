from django.db import models

# Create your models here.
class Person(models.Model):
          first_name=models.CharField(max_length=200)
          last_name=models.CharField(max_length=200)
          dateof_birth=models.DateField()
          email_id=models.EmailField()


          def __str__(self):
                    return self.first_name
          def __str__(self):
                    return self.last_name
          def __str__(self):
                    return self.dateof_birth
          def __str__(self):
                    return self.email_id