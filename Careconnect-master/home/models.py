from django.db import models
from django.contrib.auth.models import User

gen=(('Male','Male'),
     ('Female','Female'),
     ('Other','Other'))
sta=(('Andhra Pradesh','Andhra Pradesh'),
     ('Arunachal Pradesh','Arunachal Pradesh'),
     ('Assam','Assam'),
     ('Bihar','Bihar'),
     ('Chhattisgarh','Chhattisgarh'),
     ('Goa','Goa'),
     ('Gujarat','Gujarat'),
     ('Haryana','Haryana'),
     ('Himachal Pradesh','Himachal Pradesh'),
     ('Jharkhand','Jharkhand'),
     ('Karnataka','Karnataka'),
     ('Kerala','Kerala'),
     ('Madhya Pradesh','Madhya Pradesh'),
     ('Maharashtra','Maharashtra'),
     ('Manipur','Manipur'),
     ('Meghalaya','Meghalaya'),
     ('Mizoram','Mizoram'),
     ('Nagaland','Nagaland'),
     ('Odisha','Odisha'),
     ('Punjab','Punjab'),
     ('Rajasthan','Rajasthan'),
     ('Sikkim','Sikkim'),
     ('Tamil Nadu','Tamil Nadu'),
     ('Telangana','Telangana'),
     ('Tripura','Tripura'),
     ('Uttar Pradesh','Uttar Pradesh'),
     ('Uttarakhand','Uttarakhand'),
     ('West Bengal','West Bengal'),
     ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
     ('Chandigarh','Chandigarh'),
     (' Dadra and Nagar Haveli and Daman and Diu',' Dadra and Nagar Haveli and Daman and Diu'),
     ('Lakshadweep','Lakshadweep'),
     ('Delhi','Delhi'),
     ('Puducherry','Puducherry')
    )
status=(('Married','Married'),
        ('Unmarried','Unmarried'))
class registration(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    full_name=models.CharField(max_length=200)
    fathers_name=models.CharField(max_length=200)
    gender=models.CharField(choices=gen,max_length=200)
    email=models.CharField(max_length=200,unique=True)
    code=models.TextField()
    address1=models.TextField()
    address2=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(choices=sta,max_length=50)
    zip=models.IntegerField()

class lo(models.Model):
    username=models.CharField(max_length=200)  

status=(('Married','Married'),
        ('Unmarried','Unmarried'))

gen=(('Male','Male'),
     ('Female','Female'),
     ('Other','Other'))

ge=(('Male','Male'),
     ('Female','Female'),
     ('Others','Others'))
class patient_info(models.Model):
    Hospital_name = models.CharField(max_length=300)
    Bed_id=models.CharField(max_length=300,unique=True)
    Ward_number=models.IntegerField()
    Room_number=models.IntegerField()
    Disease=models.CharField(max_length=200)
    Bed_type=models.CharField(max_length=300)
    patient_name=models.CharField(max_length=200)
    patient_gender=models.CharField(choices=ge,max_length=300)
    patient_age=models.PositiveBigIntegerField()
    address=models.TextField()
    mobile_number=models.PositiveBigIntegerField()
    current_medication=models.TextField()
    allergies=models.TextField()
    past_surgeries=models.TextField()
    insurance_policy=models.TextField()
    Policy_number=models.TextField()
    special_request=models.TextField()


class info(models.Model):
    hospital_name=models.CharField(max_length=300)
    hospital_image=models.ImageField(upload_to="hospital_images")
    hospital_address=models.TextField()
    hospital_details=models.TextField()

class beds(models.Model):
    Hospital_name = models.CharField(max_length=300)
    Bed_id=models.CharField(max_length=300,unique=True)
    Ward_number=models.CharField(max_length=100)
    Room_number=models.CharField(max_length=100)
    Bed_type=models.CharField(max_length=300)

class feed(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=2000)


class profiledata(models.Model):
    full_name=models.CharField(max_length=200)
    fathers_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    code=models.TextField()
    address1=models.TextField()
    address2=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(choices=sta,max_length=50)
    zip=models.IntegerField()


class filldata(models.Model):
    Hospital_name = models.CharField(max_length=300)
    Bed_id=models.CharField(max_length=300,unique=True)
    Ward_number=models.IntegerField()
    Room_number=models.IntegerField()
    Disease=models.CharField(max_length=200)
    Bed_type=models.CharField(max_length=300)
    patient_name=models.CharField(max_length=200)
    patient_gender=models.CharField(choices=ge,max_length=300)
    patient_age=models.PositiveBigIntegerField()
    address=models.TextField()
    mobile_number=models.PositiveBigIntegerField()
    current_medication=models.TextField()
    allergies=models.TextField()
    past_surgeries=models.TextField()
    insurance_policy=models.TextField()
    Policy_number=models.TextField()
    special_request=models.TextField()





      
   


                   
                   
                   
                  
                   