from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from django.db import models


class Customer(models.Model):
    customerid = models.CharField(db_column='CustomerId', primary_key=True, max_length=50)  # Field name made lowercase.
    customerfirstname = models.CharField(db_column='CustomerFirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerlastname = models.CharField(db_column='CustomerLastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customeremail = models.CharField(db_column='CustomerEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerphotourl = models.TextField(db_column='CustomerPhotoURL', blank=True, null=True)  # Field name made lowercase.
    customerphone = models.CharField(db_column='CustomerPhone', unique=True, max_length=11, blank=True, null=True)  # Field name made lowercase.
    customercreateddate = models.DateTimeField(db_column='CustomerCreatedDate', blank=True, null=True)  # Field name made lowercase.
    customerregistereddate = models.DateTimeField(db_column='CustomerRegisteredDate', blank=True, null=True)  # Field name made lowercase.
    customermobileotp = models.CharField(db_column='CustomerMobileOTP', max_length=6, blank=True, null=True)  # Field name made lowercase.
    customerisactive = models.IntegerField(db_column='CustomerIsActive', blank=True, null=True)  # Field name made lowercase.
    customer_promotioncode = models.OneToOneField('Promotion', models.DO_NOTHING, db_column='Customer_PromotionCode', blank=True, null=True)  # Field name made lowercase.
    customerisdelete = models.IntegerField(db_column='CustomerIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Customerlocation(models.Model):
    customerlocationid = models.CharField(db_column='customerLocationId', primary_key=True, max_length=50)  # Field name made lowercase.
    customerlocation_customerid = models.TextField(db_column='customerLocation_customerId', blank=True, null=True)  # Field name made lowercase.
    customerlocation_locationname = models.CharField(db_column='customerLocation_LocationName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customerlocationlatitude = models.TextField(db_column='customerLocationLatitude', blank=True, null=True)  # Field name made lowercase.
    customerlocationlongitude = models.TextField(db_column='customerLocationLongitude', blank=True, null=True)  # Field name made lowercase.
    customerlocationisdelete = models.IntegerField(db_column='customerLocationIsDelete', blank=True, null=True)  # Field name made lowercase.
    locdate = models.DateTimeField(db_column='LocDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customerlocation'


class Discounts(models.Model):
    discountid = models.CharField(db_column='DiscountId', primary_key=True, max_length=50)  # Field name made lowercase.
    discountdescription = models.TextField(db_column='DiscountDescription', blank=True, null=True)  # Field name made lowercase.
    discountstartdate = models.DateField(db_column='DiscountStartDate', blank=True, null=True)  # Field name made lowercase.
    discountenddate = models.DateField(db_column='DiscountEndDate', blank=True, null=True)  # Field name made lowercase.
    discountisdelete = models.IntegerField(db_column='DiscountIsDelete', blank=True, null=True)  # Field name made lowercase.
    discountpercentage = models.IntegerField(db_column='DiscountPercentage')  # Field name made lowercase.
    maximumdiscount = models.IntegerField(db_column='MaximumDiscount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discounts'


class Employee(models.Model):
    employeeid = models.CharField(db_column='EmployeeId', primary_key=True, max_length=50)  # Field name made lowercase.
    employeefirstname = models.TextField(db_column='EmployeeFirstName', blank=True, null=True)  # Field name made lowercase.
    employeelastname = models.TextField(db_column='EmployeeLastName', blank=True, null=True)  # Field name made lowercase.
    employeeemail = models.TextField(db_column='EmployeeEmail', blank=True, null=True)  # Field name made lowercase.
    employeephotourl = models.TextField(db_column='EmployeePhotoURL', blank=True, null=True)  # Field name made lowercase.
    employeephone = models.CharField(db_column='EmployeePhone', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    employeeaadharnumber = models.TextField(db_column='EmployeeAadharNumber', blank=True, null=True)  # Field name made lowercase.
    employeecreateddate = models.DateTimeField(db_column='EmployeeCreatedDate', blank=True, null=True)  # Field name made lowercase.
    employeeregistereddate = models.DateTimeField(db_column='EmployeeRegisteredDate', blank=True, null=True)  # Field name made lowercase.
    employeemobileotp = models.CharField(db_column='EmployeeMobileOTP', max_length=6, blank=True, null=True)  # Field name made lowercase.
    employeeimei = models.TextField(db_column='EmployeeIMEI', blank=True, null=True)  # Field name made lowercase.
    employeeisdelete = models.IntegerField(db_column='EmployeeIsDelete', blank=True, null=True)  # Field name made lowercase.
    emprole = models.CharField(db_column='EmpRole', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Employeerole(models.Model):
    employeeroleid = models.CharField(db_column='EmployeeRoleId', primary_key=True, max_length=50)  # Field name made lowercase.
    employeeroledescription = models.TextField(db_column='EmployeeRoleDescription', blank=True, null=True)  # Field name made lowercase.
    employeerole_employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmployeeRole_EmployeeId', blank=True, null=True)  # Field name made lowercase.
    employeerole_roleid = models.ForeignKey('Role', models.DO_NOTHING, db_column='EmployeeRole_RoleId', blank=True, null=True)  # Field name made lowercase.
    employeeroleisdelete = models.IntegerField(db_column='EmployeeRoleisDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employeerole'


class Invoice(models.Model):
    invoiceid = models.CharField(db_column='InvoiceId', primary_key=True, max_length=50)  # Field name made lowercase.
    invoicenumber = models.IntegerField(db_column='InvoiceNumber', blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    invoicetime = models.TimeField(db_column='InvoiceTime', blank=True, null=True)  # Field name made lowercase.
    invoice_saleid = models.ForeignKey('Sale', models.DO_NOTHING, db_column='Invoice_SaleId', blank=True, null=True)  # Field name made lowercase.
    invoiceisdelete = models.IntegerField(db_column='InvoiceIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice'


class Invoiceitem(models.Model):
    invoiceitemid = models.CharField(db_column='InvoiceItemId', primary_key=True, max_length=50)  # Field name made lowercase.
    invoiceitem_itemid = models.CharField(db_column='InvoiceItem_ItemId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invoiceitem_invoiceid = models.CharField(db_column='InvoiceItem_InvoiceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invoiceitemsisdelete = models.IntegerField(db_column='InvoiceItemsIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoiceitem'


class Item(models.Model):
    itemid = models.CharField(db_column='ItemId', primary_key=True, max_length=50)  # Field name made lowercase.
    toditemname = models.TextField(db_column='TodItemName', blank=True, null=True)  # Field name made lowercase.
    toditemdescription = models.TextField(db_column='TodItemDescription', blank=True, null=True)  # Field name made lowercase.
    toditemurl = models.TextField(db_column='TodItemURL', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.TextField(db_column='ItemType', blank=True, null=True)  # Field name made lowercase.
    tomitemname = models.TextField(db_column='TomItemName', blank=True, null=True)  # Field name made lowercase.
    tomitemdescription = models.TextField(db_column='TomItemDescription', blank=True, null=True)  # Field name made lowercase.
    tomitemurl = models.TextField(db_column='TomItemURL', blank=True, null=True)  # Field name made lowercase.
    isveg = models.IntegerField(db_column='IsVeg', blank=True, null=True)  # Field name made lowercase.
    itemisdelete = models.IntegerField(db_column='ItemIsDelete', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Miscellanous(models.Model):
    cgst = models.DecimalField(db_column='CGST', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sgst = models.DecimalField(db_column='SGST', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deliverycharges = models.IntegerField(db_column='DeliveryCharges', blank=True, null=True)  # Field name made lowercase.
    minorderdeliveryfree = models.IntegerField(db_column='MinOrderDeliveryFree', blank=True, null=True)  # Field name made lowercase.
    miscid = models.AutoField(db_column='MiscId', primary_key=True)  # Field name made lowercase.
    adminemail = models.CharField(db_column='AdminEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'miscellanous'


class MsgMisc(models.Model):
    msg_misc_id = models.AutoField(db_column='Msg_misc_id', primary_key=True)  # Field name made lowercase.
    reminder_interval = models.IntegerField(db_column='Reminder_Interval', blank=True, null=True)  # Field name made lowercase.
    frequeny_in_days = models.IntegerField(db_column='Frequeny_in_days', blank=True, null=True)  # Field name made lowercase.
    frequeny_per_day = models.IntegerField(db_column='Frequeny_per_day', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'msg_misc'


class Mytest(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    mydate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mytest'


class Orders(models.Model):
    orderid = models.CharField(db_column='OrderId', primary_key=True, max_length=50)  # Field name made lowercase.
    ordermenuid = models.TextField(db_column='OrderMenuId', blank=True, null=True)  # Field name made lowercase.
    ordercustomerid = models.CharField(db_column='OrderCustomerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ordcreateddate = models.TextField(db_column='OrdCreatedDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.TextField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    subscription = models.TextField(db_column='Subscription', blank=True, null=True)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='TotalPrice', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qty = models.TextField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    promotion = models.CharField(db_column='Promotion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tax = models.TextField(db_column='Tax', blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    weekend = models.TextField(db_column='Weekend', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Orderspayments(models.Model):
    orderspaymentsid = models.CharField(db_column='OrdersPaymentsId', primary_key=True, max_length=50)  # Field name made lowercase.
    paymentid = models.CharField(db_column='PaymentId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.IntegerField(db_column='PaymentStatus', blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerId', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderspayments'


class PayuPayments(models.Model):
    account = models.CharField(max_length=255)
    payable_id = models.PositiveIntegerField(blank=True, null=True)
    payable_type = models.CharField(max_length=255, blank=True, null=True)
    txnid = models.CharField(max_length=255)
    mihpayid = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    amount = models.FloatField()
    discount = models.FloatField()
    net_amount_debit = models.FloatField()
    data = models.TextField()
    status = models.CharField(max_length=255)
    unmappedstatus = models.CharField(max_length=255)
    mode = models.CharField(max_length=255, blank=True, null=True)
    bank_ref_num = models.CharField(max_length=255, blank=True, null=True)
    bankcode = models.CharField(max_length=255, blank=True, null=True)
    cardnum = models.CharField(max_length=255, blank=True, null=True)
    name_on_card = models.CharField(max_length=255, blank=True, null=True)
    issuing_bank = models.CharField(max_length=255, blank=True, null=True)
    card_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payu_payments'


class Permission(models.Model):
    permissionid = models.CharField(db_column='PermissionId', primary_key=True, max_length=50)  # Field name made lowercase.
    permissionname = models.CharField(db_column='PermissionName', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    permissionmapid = models.CharField(db_column='PermissionMapId', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    permissionisdelete = models.IntegerField(db_column='PermissionisDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permission'


class Permissionmap(models.Model):
    permissionmapid = models.CharField(db_column='PermissionMapId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    permissionmapdescription = models.TextField(db_column='PermissionMapDescription', blank=True, null=True)  # Field name made lowercase.
    permissionmapcodes = models.TextField(db_column='PermissionMapCodes', blank=True, null=True)  # Field name made lowercase.
    permissionmapisdelete = models.IntegerField(db_column='PermissionMapIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permissionmap'


class Promotion(models.Model):
    promotionid = models.CharField(db_column='PromotionId', primary_key=True, max_length=50)  # Field name made lowercase.
    promotiondescription = models.TextField(db_column='PromotionDescription', blank=True, null=True)  # Field name made lowercase.
    promotioncode = models.CharField(db_column='PromotionCode', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    promotionstartdate = models.DateTimeField(db_column='PromotionStartDate', blank=True, null=True)  # Field name made lowercase.
    promotionenddate = models.DateTimeField(db_column='PromotionEndDate', blank=True, null=True)  # Field name made lowercase.
    promotionisdelete = models.IntegerField(db_column='PromotionIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotion'


class Promotiondiscountsale(models.Model):
    promotiondiscountsaleid = models.CharField(db_column='PromotionDiscountSaleId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discountcode = models.IntegerField(db_column='DiscountCode', blank=True, null=True)  # Field name made lowercase.
    promotiondiscountsale_saleid = models.CharField(db_column='PromotionDiscountSale_SaleId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    promotiondiscountsale_promotionid = models.CharField(db_column='PromotionDiscountSale_PromotionId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    promotiondiscountsaleisdelete = models.IntegerField(db_column='PromotionDiscountSaleIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotiondiscountsale'


class Restaurantlocation(models.Model):
    locationid = models.CharField(db_column='LocationId', primary_key=True, max_length=50)  # Field name made lowercase.
    locationname = models.CharField(db_column='LocationName', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    locationlatitude = models.TextField(db_column='LocationLatitude', blank=True, null=True)  # Field name made lowercase.
    locationlongitude = models.TextField(db_column='LocationLongitude', blank=True, null=True)  # Field name made lowercase.
    locationlastupdated = models.DateTimeField(db_column='LocationLastUpdated', blank=True, null=True)  # Field name made lowercase.
    locationisdelete = models.IntegerField(db_column='LocationIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restaurantlocation'


class Role(models.Model):
    roleid = models.CharField(db_column='RoleId', primary_key=True, max_length=50)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', unique=True, max_length=23, blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'


class Rolepermission(models.Model):
    rolepermissionid = models.CharField(db_column='RolePermissionId', primary_key=True, max_length=50)  # Field name made lowercase.
    rolepermission_permissionid = models.ForeignKey(Permission, models.DO_NOTHING, db_column='RolePermission_PermissionId', blank=True, null=True)  # Field name made lowercase.
    rolepermission_roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='RolePermission_RoleId', blank=True, null=True)  # Field name made lowercase.
    rolepermissionisdelete = models.IntegerField(db_column='RolePermissionIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rolepermission'


class Sale(models.Model):
    saleid = models.CharField(db_column='SaleId', primary_key=True, max_length=50)  # Field name made lowercase.
    salenumber = models.IntegerField(db_column='SaleNumber', blank=True, null=True)  # Field name made lowercase.
    saledate = models.DateField(db_column='SaleDate', blank=True, null=True)  # Field name made lowercase.
    saletime = models.TimeField(db_column='SaleTime', blank=True, null=True)  # Field name made lowercase.
    sale_promotionid = models.ForeignKey(Promotion, models.DO_NOTHING, db_column='Sale_PromotionId', blank=True, null=True)  # Field name made lowercase.
    saleisdelete = models.IntegerField(db_column='SaleIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sale'


class Tax(models.Model):
    taxid = models.CharField(db_column='TaxId', primary_key=True, max_length=50)  # Field name made lowercase.
    taxcode = models.IntegerField(db_column='TaxCode', blank=True, null=True)  # Field name made lowercase.
    taxdescription = models.TextField(db_column='TaxDescription', blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.CharField(db_column='TaxPercent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tax_saleid = models.ForeignKey(Sale, models.DO_NOTHING, db_column='Tax_SaleId', blank=True, null=True)  # Field name made lowercase.
    taxisdelete = models.IntegerField(db_column='TaxIsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tax'


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
