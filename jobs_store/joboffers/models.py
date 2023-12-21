from django.db import models

class Offer(models.Model):
    o_id = models.CharField(primary_key=True, max_length=50)
    o_search_keyword = models.CharField(max_length=255)
    o_title = models.CharField(max_length=255)
    o_department_code = models.IntegerField()
    o_city_code = models.IntegerField()
    o_city = models.CharField(max_length=100, null=True)
    o_company_name = models.CharField(max_length=255, null=True)
    o_description = models.TextField(null=True)
    o_contract = models.CharField(max_length=100, null=True)
    o_contact_mail = models.EmailField(null=True)
    o_added_at = models.DateTimeField(null=True)
    o_updated_at = models.DateTimeField(null=True)

class Geolocation(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE, related_name='geolocation')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

class Salary(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE, related_name='salary')
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    salary_description = models.TextField(null=True)

class Skill(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    exigence = models.CharField(max_length=1)