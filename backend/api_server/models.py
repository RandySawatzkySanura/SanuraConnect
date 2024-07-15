from django.db import models



class InventoryWebSupplement(models.Model):
    sku = models.CharField(primary_key=True, max_length=20)
    brand = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    department_web = models.CharField(max_length=100, blank=True, null=True)
    description_short = models.CharField(max_length=100, blank=True, null=True)
    description_web = models.CharField(max_length=3000, blank=True, null=True)
    key_feature_1 = models.CharField(max_length=1000, blank=True, null=True)
    key_feature_2 = models.CharField(max_length=1000, blank=True, null=True)
    key_feature_3 = models.CharField(max_length=1000, blank=True, null=True)
    key_feature_4 = models.CharField(max_length=1000, blank=True, null=True)
    sales_tagline = models.CharField(max_length=1000, blank=True, null=True)
    pack_length = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    pack_width = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    pack_height = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    pack_weight = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    pack_type = models.CharField(max_length=10, blank=True, null=True)
    price_web = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    web_enabled = models.BooleanField()
    has_image = models.CharField(max_length=50)
    dim_weight_lbs_ups = models.DecimalField (max_digits=5,decimal_places=2, blank=True, null=True)
    dim_weight_lbs_canadapost = models.DecimalField (max_digits=5,decimal_places=2, blank=True, null=True)
    shipping_class = models.CharField(max_length=15, blank=True, null=True)
    web_category_1 = models.IntegerField()
    web_category_2 = models.IntegerField()
    web_category_3 = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'inventory_web_supplement'
        db_table_comment = 'a table to store web information'