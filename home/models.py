from django.db import models

# Create your models here.

class Departments(models.Model):
    dept_name=models.CharField(max_length=150)
    dept_description=models.TextField(max_length=250)

    def __str__(self):
        return self.dept_name

class Doctors(models.Model):
    doctor_name=models.CharField(max_length=250)
    doctor_specialisation=models.CharField(max_length=250)
    doctor_dept=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doctor_img=models.ImageField(upload_to='doctors')

    def __str__(self):
        return self.doctor_name
    

  
    # def __str__(self):
    #     return self.name

   

   