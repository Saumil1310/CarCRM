from django.db import models

# Create your models here.

# Car Details
class InventoryMaster(models.Model):
	CarID=models.AutoField(primary_key=True)
	CarName=models.CharField(max_length=255,null=False)
	OldCust=models.CharField(max_length=255,null=False)
	CarModel=models.CharField(max_length=255,null=False)
	Mfg=models.CharField(max_length=255,null=True, blank=True)
	BuyPrice=models.CharField(max_length=255,null=False)
	SellPrice=models.CharField(max_length=255,null=False)
	CarImage=models.ImageField(max_length=255,null=True,default='NULL')
	KWNo=models.CharField(max_length=255,null=False,default='KW01')
	RegNo=models.CharField(max_length=255,null=False,default='KW01')
	Date=models.DateField(null=True, blank=True)
	FinalPrice = models.CharField(max_length=255, null=False, default='00')
	Milage=models.CharField(max_length=255,null=False,default='KW01')
	Engine=models.CharField(max_length=255,null=False,default='KW01')
	BodyShop_Amount = models.CharField(max_length=20,default='NULL')
	BodyShop_Details = models.CharField(max_length=255,default='NULL')
	Mechanic_Amount = models.CharField(max_length=20,default='NULL')
	Mechanic_Details = models.CharField(max_length=255,default='NULL')
	MOT_Amount = models.CharField(max_length=20,default='NULL')
	MOT_Details = models.CharField(max_length=255,default='NULL')
	Travelling_Amount = models.CharField(max_length=20,default='NULL')
	Travelling_Details = models.CharField(max_length=255,default='NULL')
	Fuel_Amount = models.CharField(max_length=20,default='NULL')
	Fuel_Details = models.CharField(max_length=255,default='NULL')
	Total_Expenses = models.CharField(max_length=20, null=True,default='NULL')
	CreatedAt=models.DateTimeField(auto_now_add=True)
	ModifiedAt=models.DateTimeField(auto_now=True)
	IsActive=models.BooleanField(default=0)
	IsDelete=models.BooleanField(default=0)

	def __str__(self):
		return self.CarName


class SoldCarsMaster(models.Model):
	SoldID=models.AutoField(primary_key=True)
	CarName=models.CharField(max_length=255,null=False)
	OldCust=models.CharField(max_length=255,null=False)
	CurrentCust=models.CharField(max_length=255,null=False,default='NULL')
	CarModel=models.CharField(max_length=255,null=False)
	Mfg=models.DateField(null=True, blank=True)
	BuyPrice=models.CharField(max_length=255,null=False)
	SellPrice=models.CharField(max_length=255,null=False)
	CarImage=models.ImageField(max_length=255,default='NULL')
	KWNo=models.CharField(max_length=255,null=False,default='KW01')
	RegNo=models.CharField(max_length=255,null=False,default='KW01')
	Milage=models.CharField(max_length=255,null=False,default='KW01')
	Engine=models.CharField(max_length=255,null=False,default='KW01')
	Amount=models.CharField(max_length=255,default='NULL')
	Total_Expenses = models.CharField(max_length=20, null=True,default='NULL')
	Buy_EXP=models.CharField(max_length=20, null=True,default='NULL')
	Profit=models.CharField(max_length=20, null=True,default='NULL')
	Date=models.DateField(null=True, blank=True)
	CreatedAt=models.DateTimeField(auto_now_add=True)
	ModifiedAt=models.DateTimeField(auto_now=True)
	IsActive=models.BooleanField(default=0)
	IsDelete=models.BooleanField(default=0)

	def __str__(self):
		return self.CarName


#Car Documents
class CarDocMaster(models.Model):
	CarDocID=models.AutoField(primary_key=True)
	CarID=models.ForeignKey(InventoryMaster,null=True,on_delete=models.SET_NULL)
	Doc=models.FileField(max_length=255)
	DocDescription=models.CharField(max_length=255,default='NULL')
	CarName=models.CharField(max_length=255,default='NULL')
	RegNo=models.CharField(max_length=255,null=False,default='KW01')


#Lead Details
class LeadMaster(models.Model):
	LeadID=models.AutoField(primary_key=True)
	LeadName=models.CharField(max_length=255,null=False)
	LeadEmail=models.EmailField(max_length=255,blank=False)
	LeadAddress=models.CharField(max_length=255,blank=True,null=True)
	LeadMobile=models.BigIntegerField(blank=False)
	Choices=models.CharField(max_length=255,null=True,blank=True)
	OfferPrice=models.CharField(max_length=255,default='NULL')
	Comment=models.CharField(max_length=255,default='NULL')
	Payment=models.CharField(max_length=255,default='NULL')
	Date=models.DateField(null=True, blank=True)
	CreatedAt=models.DateTimeField(auto_now_add=True)
	ModifiedAt=models.DateTimeField(auto_now=True)
	IsActive=models.BooleanField(default=0)
	IsDelete=models.BooleanField(default=0)

	def __str__(self):
		return self.LeadName


#Customer Details
class CustomerMaster(models.Model):
	CustID=models.AutoField(primary_key=True)
	CustName=models.CharField(max_length=255)
	CustEmail=models.EmailField(max_length=255)
	CustMobile=models.BigIntegerField(blank=False)
	CustAddress=models.CharField(max_length=255,blank=True,null=True,default='NULL')
	OfferPrice=models.CharField(max_length=255,default='NULL')
	Comment=models.CharField(max_length=255,default='NULL')
	Payment=models.CharField(max_length=255,default='NULL')
	Amount=models.CharField(max_length=255,default='NULL')
	PurchasedCar=models.CharField(max_length=255)
	Date=models.DateField(null=True, blank=True)
	CreatedAt=models.DateTimeField(auto_now_add=True)
	ModifiedAt=models.DateTimeField(auto_now=True)
	IsActive=models.BooleanField(default=0)
	IsDelete=models.BooleanField(default=0)

	def __str__(self):
		return self.CustName


class AdminMaster(models.Model):
	AdminID=models.AutoField(primary_key=True)
	AdminEmail=models.EmailField(max_length=255,unique=True)
	AdminUsername=models.CharField(max_length=255,default='Admin')
	AdminPassword=models.CharField(max_length=255)

	def __str__(self):
		return self.AdminEmail


class LeadgerMaster(models.Model):
    LedgerID = models.AutoField(primary_key=True)
    Date = models.DateField(null=True, blank=True)
    CarName = models.CharField(max_length=255, null=False)
    RegNo = models.CharField(max_length=255, null=False, default='KW01')
    KWNo = models.CharField(max_length=255, null=False, default='KW01')
    FinalPrice = models.CharField(max_length=255, null=False, default='0')
    Amount = models.CharField(max_length=255, null=False,default='0')
    Vtype = models.CharField(max_length=255, null=False, default='KW01')







