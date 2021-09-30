from django.db import models
class product(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField( default="0")
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")
    objects = models.Manager()
    def __str__(self):
        return self.product_name
# Create your models here.
class contact(models.Model):
    msg_id=models.AutoField(primary_key=True)

    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500,default="")

    objects = models.Manager()
    def __str__(self):
        return self.name
class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000,default="")
    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=50,default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50,default="")
    address=models.CharField(max_length=500,default="")

    objects = models.Manager()
class orderupdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.update_desc[0:7]+"..."