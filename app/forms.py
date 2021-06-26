from django import forms

#Car Detail Form 
class InventoryForm(forms.Form):
	CarName=forms.CharField(max_length=255)
	OldCustomer=forms.CharField(max_length=255)
	CarModel=forms.CharField(max_length=255)
	MfgDate=forms.DateField()
	BuyPrice=forms.CharField(max_length=255)
	SellPrice=forms.CharField(max_length=255)
	CarImage=forms.ImageField()
	RegNo=forms.CharField(max_length=255)
	Milage=forms.CharField(max_length=255)
	Engine=forms.CharField(max_length=255)
	BodyShop_Amount = forms.CharField(max_length=20)
	Bodyshop_Details = forms.CharField(max_length=255)
	Mechanic_Amount = forms.CharField(max_length=20)
	Mechanic_Details = forms.CharField(max_length=255)
	Mot_Amount = forms.CharField(max_length=20)
	Mot_Details = forms.CharField(max_length=255)
	Travelling_Amount = forms.CharField(max_length=20)
	Travelling_Details = forms.CharField(max_length=255)
	Fuel_Amount = forms.CharField(max_length=20)
	Fuel_Details = forms.CharField(max_length=255)


#Customer Detail Form
class LeadForm(forms.Form):
	Name=forms.CharField(max_length=255)
	Email=forms.EmailField(max_length=255)
	Address=forms.CharField(max_length=255)
	MobileNo=forms.IntegerField()
	OfferPrice=forms.CharField(max_length=255)
	CHOICES=[('Cash','Cash'),
         ('Finance','Finance')]
	Payment = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class AdminForm(forms.Form):
	Email=forms.EmailField(max_length=255)
	Password=forms.CharField(max_length=255)




