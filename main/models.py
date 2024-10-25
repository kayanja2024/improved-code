from django.db import models
from multiselectfield import MultiSelectField
from twilio.rest import Client

# Create your models here.

class score(models.Model):
    result = models.PositiveIntegerField()


    def __str__(self):
        return str(self.result)
    

    def save(self, *args, **kwargs):
        if self.result < 70:

            account_sid = 'ACa093272eb83f62f7f1a991ef24a316af'
            auth_token = 'f3fc4bb1af0156c3a2f0f24c8af36d7d'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'the current result is bad-{self.result}',
                                        from_='+12085497868',
                                        to='+256759613893'
            )

            print(message.sid)
            return super().save(*args, **kwargs)   








class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    dob = models.DateField(null=True)
    patient_relative_name = models.CharField(max_length=50, null=True)
    patient_relative_contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=50)
    PREGNANCY_SYMPTOMS = (
        ('Fever', 'Fever'),
        ('vomiting', 'vomiting'),
        (' fatigue', ' fatigue'),
        ('Heartburn', 'Heartburn'),
        ('nausea', 'nausea'),
        ('Missed Periods', 'Missed Periods'),
        ('Swollen Breasts', 'Swollen Breasts'),
        ('Food Cravings', 'Food Cravings'),
        ('Mood Swings', 'Mood Swings'),   
        ('Loss of taste or smell', 'Loss of taste or smell'),
        ('Heartburn', 'Heartburn'),
        
    )

    symptoms = MultiSelectField(choices=PREGNANCY_SYMPTOMS, null=True)
    Last_menstrual_period = models.DateTimeField(blank=True, null=True)
    Current_gestational_age = models.FloatField(blank=True, null=True)
    Details_of_previous_deliveries = models.TextField(max_length=200)
    prior_ailments = models.TextField(blank=True, null=True)

    food_preferences = (
        ('Proteins', 'Proteins'),
        ('Carbohydrates', 'Carbohydrates'),
        ('Fats', 'Fats'),
        ('Vitamins and Minerals', 'Vitamins and Minerals'),
    )

    Diet_and_nutrition = MultiSelectField(choices=food_preferences, null=True)
    exercise_culture = (
        ('Normal exercises', 'Normal exercises'),
        ('not enough exercises', 'not enough exercises'),
        ('rarely do exercises', 'rarely do exercises'),
    )

    Exercise_routine = MultiSelectField(choices=exercise_culture, null=True)
    status = models.CharField(max_length=50)
    Blood_pressure = models.FloatField(blank=True, null=True)
    Heart_rate = models.FloatField(blank=True, null=True)
    Temperature = models.FloatField(blank=True, null=True)
    Weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    Body_Mass_Index = models.FloatField(blank=True, null=True)
    Blood_type_and_Rh_factor = models.FloatField(blank=True, null=True)

    habits = (
        ('Smoking', 'Smoking'),
        ('alcohol_drinking', 'alcohol_drinking'),
        ('drug_use', 'drug_use'),
    )

    personal_behavious = MultiSelectField(choices=habits, null=True)
    amburance_num = models.ForeignKey("Ambulance", on_delete=models.CASCADE)
    bed_num = models.ForeignKey("Bed", on_delete=models.CASCADE, null=True)
    
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    doctors_notes = models.TextField(null=True, blank=True)
    
    doctors_visiting_time = models.CharField(null=True, max_length=50, blank=True)
    operated = models.BooleanField(blank=True, null=True)
    delivered = models.BooleanField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    #def save(self, *args, **kwargs):
    # def save(phone_num, message):
        

    #         account_sid = 'ACa093272eb83f62f7f1a991ef24a316af'
    #         auth_token = 'f3fc4bb1af0156c3a2f0f24c8af36d7d'
    #         client = Client(account_sid, auth_token)

    #         message = client.messages.create(
    #                                     body=f'kawempe hospital has registered you-{self.name}',
    #                                     from_='+12085497868',
    #                                     to='+256759613893'
    #         )

    #         print(message.sid)
    #         return super().save(phone_num, message)   
        


class Ambulance(models.Model):
    ambulance_number = models.CharField(max_length=50)
    occupied = models.BooleanField()
    def __str__(self):
        return self.ambulance_number


class Bed(models.Model):
    bed_number = models.CharField(max_length=50)
    occupied = models.BooleanField()
    def __str__(self):
        return self.bed_number


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.name




class patiant_data(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True)
    
     

