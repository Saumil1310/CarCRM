from django.shortcuts import render, redirect
from .models import InventoryMaster, CarDocMaster, LeadMaster, CustomerMaster, AdminMaster, SoldCarsMaster, \
    LeadgerMaster
from .forms import InventoryForm, LeadForm, AdminForm
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
import collections
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers


# Create your views here.

# Home Page
def index(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        return render(request, 'index.html', context)
    else:
        return redirect('admin_login')


# Admin Register
def admin_register(request):
    context = {}
    if request.POST:
        if not AdminMaster.objects.filter(AdminEmail=request.POST['Email']).exists():
            AdminMaster.objects.create(AdminEmail=request.POST['Email'], AdminPassword=request.POST['Password'],
                                       AdminUsername=request.POST['Username'])
            return redirect('admin_login')
        else:
            context['msg'] = 'This Email already exists'
    return render(request, 'register.html', context)


# Admin Login
def admin_login(request):
    context = {}
    if not 'login' in request.session:
        if request.POST:
            if AdminMaster.objects.filter(AdminEmail=request.POST['Email'],
                                          AdminPassword=request.POST['Password']).exists():
                user_name = AdminMaster.objects.filter(AdminEmail=request.POST['Email']).values('AdminUsername')[0][
                    'AdminUsername']
                request.session['login'] = True
                request.session['user_name'] = user_name
                user = request.session['user_name']
                return redirect('index')
            else:
                context['msg'] = 'Invalid Username or Password'
        return render(request, 'login.html', context)
    else:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        return redirect('index')


def logout(request):
    del request.session['login']
    del request.session['user_name']
    return redirect('admin_login')


# Add Cars in inventory
def inventory(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        today_date = datetime.now()
        today_date = today_date.today().strftime("%Y-%m-%d")
        context['today_date'] = today_date
        if request.POST:
            # print(request.FILES.get('car_image'))
            # print(request.FILES['car_image'])
            InventoryMaster.objects.create(CarName=request.POST.get('cname'), OldCust=request.POST.get('old_cus'),
                                           CarModel=request.POST.get('cmodel'), Mfg=request.POST.get('mfg'),
                                           CarImage=request.FILES['car_image'], RegNo=request.POST.get('reg_no'),
                                           Engine=request.POST['engine'], Milage=request.POST.get('milage'),
                                           BuyPrice=request.POST['buy_price'], SellPrice=request.POST['sell_price'],
                                           Date=request.POST['date'], BodyShop_Amount=request.POST.get('bodyshop'),
                                           BodyShop_Details=request.POST.get('bodyshop1'),
                                           Mechanic_Amount=request.POST.get('mechanic'),
                                           Mechanic_Details=request.POST.get('mechanic1'),
                                           MOT_Amount=request.POST.get('mot'), MOT_Details=request.POST.get('mot1'),
                                           Travelling_Amount=request.POST.get('travelling'),
                                           Travelling_Details=request.POST.get('travelling1'),
                                           Fuel_Amount=request.POST.get('fuel'), Fuel_Details=request.POST.get('fuel1'),
                                           IsActive=1)
            car_id = InventoryMaster.objects.filter(RegNo=request.POST['reg_no']).values()[0]['CarID']
            car_id_instance = InventoryMaster.objects.filter(CarID=car_id)[0]
            kw_no = 'KW' + str(car_id)
            ############################
            Docs = request.FILES.getlist('docfile[]')
            texts = request.POST.getlist('doc[]')
            for img, des in zip(Docs, texts):
                images = CarDocMaster.objects.create(CarID=car_id_instance, Doc=img, DocDescription=des,
                                                     CarName=request.POST['cname'], RegNo=request.POST['reg_no'])
            ############################
            total = []
            total.append(int(request.POST['bodyshop']))
            total.append(int(request.POST['mechanic']))
            total.append(int(request.POST['mot']))
            total.append(int(request.POST['travelling']))
            total.append(int(request.POST['fuel']))
            total_expence = sum(total)
            InventoryMaster.objects.filter(RegNo=request.POST['reg_no']).update(Total_Expenses=total_expence)
            Final_buyprice = []
            Final_buyprice.append(int(request.POST['buy_price']))
            Final_buyprice.append(int(total_expence))
            Purchase_price = sum(Final_buyprice)
            InventoryMaster.objects.filter(CarID=car_id).update(FinalPrice=Purchase_price, KWNo=kw_no)
            LeadgerMaster.objects.create(Date=request.POST['date'], CarName=request.POST.get('cname'),
                                         RegNo=request.POST.get('reg_no'), KWNo=kw_no, FinalPrice=Purchase_price,
                                         Vtype='Buy')
            return redirect('car_list')
        return render(request, 'car-details1.html', context)
    else:
        return redirect('admin_login')


# Cars List
def car_list(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        car_list = InventoryMaster.objects.all()
        context['car_list'] = car_list
        return render(request, 'car.html', context)
    else:
        return redirect('admin_login')


# Car View
def car_view(request, id):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        car_detail = InventoryMaster.objects.filter(CarID=id).values()
        context['car_detail'] = car_detail
        return render(request, 'car-view.html', context)
    else:
        return redirect('admin_login')


# Update Car Details
def update_car(request, id):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        car_detail = InventoryMaster.objects.filter(CarID=id).values()
        context['car_detail'] = car_detail
        car_regno = InventoryMaster.objects.filter(CarID=id).values('RegNo')[0]['RegNo']
        car_doc = CarDocMaster.objects.filter(CarID=id).values()
        context['car_doc'] = car_doc
        if request.POST:
            InventoryMaster.objects.filter(RegNo=car_regno).update(CarName=request.POST['cname'],
                                                                   OldCust=request.POST['old_cus'],
                                                                   CarModel=request.POST['cmodel'],
                                                                   Mfg=request.POST.get('mfg'),
                                                                   RegNo=request.POST['reg_no'],
                                                                   Engine=request.POST['engine'],
                                                                   Milage=request.POST['milage'],
                                                                   BuyPrice=request.POST['buy_price'],
                                                                   SellPrice=request.POST['sell_price'],
                                                                   Date=request.POST['date'],
                                                                   BodyShop_Amount=request.POST.get('bodyshop'),
                                                                   BodyShop_Details=request.POST.get('bodyshop1'),
                                                                   Mechanic_Amount=request.POST.get('mechanic'),
                                                                   Mechanic_Details=request.POST.get('mechanic1'),
                                                                   MOT_Amount=request.POST.get('mot'),
                                                                   MOT_Details=request.POST.get('mot1'),
                                                                   Travelling_Amount=request.POST.get('travelling'),
                                                                   Travelling_Details=request.POST.get('travelling1'),
                                                                   Fuel_Amount=request.POST.get('fuel'),
                                                                   Fuel_Details=request.POST.get('fuel1'))
            if request.FILES.get('car_image') == None:
                InventoryMaster.objects.filter(RegNo=car_regno).update(CarImage=request.POST['c_img'])
            else:
                InventoryMaster.objects.filter(RegNo=car_regno).update(CarImage=request.FILES['car_image'])
            ########################
            Docs = request.FILES.getlist('docfile[]')
            print('Doc 1:', Docs)
            print('Doc 2:', request.FILES.getlist('docfile1[]'))
            texts = request.POST.getlist('doc[]')
            for img, des in zip(Docs, texts):
                images = CarDocMaster.objects.filter(CarID=id).update(CarID=id, Doc=img, DocDescription=des,
                                                                      RegNo=request.POST['reg_no'],
                                                                      CarName=request.POST['cname'])
            ########################
            total = []
            total.append(int(request.POST['bodyshop']))
            total.append(int(request.POST['mechanic']))
            total.append(int(request.POST['mot']))
            total.append(int(request.POST['travelling']))
            total.append(int(request.POST['fuel']))
            total_expence = sum(total)
            InventoryMaster.objects.filter(RegNo=car_regno).update(Total_Expenses=total_expence)
            ##########################
            Final_buyprice = []
            Final_buyprice.append(int(request.POST['buy_price']))
            Final_buyprice.append(int(total_expence))
            Purchase_price = sum(Final_buyprice)
            InventoryMaster.objects.filter(CarID=id).update(FinalPrice=Purchase_price)
            return redirect('car_list')
        return render(request, 'car-update.html', context)
    else:
        return redirect('admin_login')


# Delete Car
def car_delete(request, id):
    InventoryMaster.objects.filter(CarID=id).delete()
    return redirect('car_list')


# Add Lead
def add_lead(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        today_date = datetime.now()
        today_date = today_date.today().strftime("%Y-%m-%d")
        context['today_date'] = today_date
        car_names = InventoryMaster.objects.all()
        context['car_names'] = car_names
        lead = LeadMaster.objects.all()
        context['lead'] = lead
        if request.POST:
            my_cars_list = request.POST.getlist('selected')  ##To get selected car list
            my_cars_string = ','.join(my_cars_list)
            LeadMaster.objects.create(LeadName=request.POST.get('name'), LeadEmail=request.POST.get('email'),
                                      LeadAddress=request.POST.get('address'), LeadMobile=request.POST.get('phone'),
                                      Choices=my_cars_string, Payment=request.POST['optradio'],
                                      OfferPrice=request.POST.get('sell-price'), Comment=request.POST.get('comment'),
                                      Date=request.POST['date'], IsActive=1)
        return render(request, 'lead-details.html', context)
    else:
        return redirect('admin_login')


# Lead list
def lead_list(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        lead = LeadMaster.objects.all()
        context['lead'] = lead
        return render(request, 'leads.html', context)
    else:
        return redirect('admin_login')


# Lead View
def lead_view(request, id):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        lead_details = LeadMaster.objects.filter(LeadID=id).values()
        context['lead_details'] = lead_details
        return render(request, 'lead-view.html', context)
    else:
        return redirect('admin_login')


# Lead Update
def lead_update(request, id):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        car_names = InventoryMaster.objects.all().values('CarName')
        cars = {
            k: [d.get(k) for d in car_names]
            for k in set().union(*car_names)
        }
        cars = cars['CarName']
        context['car_names'] = car_names
        lead_details = LeadMaster.objects.filter(LeadID=id).values()
        context['lead_details'] = lead_details
        lead_choices = LeadMaster.objects.filter(LeadID=id).values('Choices')[0]['Choices']
        lead_choices = lead_choices.split(',')
        context['lead_choices'] = lead_choices
        combine_list = cars + lead_choices
        print(combine_list)
        for x in lead_choices:
            cars.remove(x)
        print(cars)
        context['cars'] = cars
        if request.POST:
            my_cars_list = request.POST.getlist('selected')  ##To get selected car list
            my_cars_string = ','.join(my_cars_list)
            LeadMaster.objects.filter(LeadID=id).update(LeadName=request.POST.get('name'),
                                                        LeadEmail=request.POST.get('email'),
                                                        LeadAddress=request.POST.get('address'),
                                                        LeadMobile=request.POST.get('phone'), Choices=my_cars_string,
                                                        Payment=request.POST['optradio'],
                                                        OfferPrice=request.POST.get('sell-price'),
                                                        Comment=request.POST.get('comment'))
            return redirect('lead_list')
        return render(request, 'lead-update.html', context)
    else:
        return redirect('admin_login')


# Delete Lead
def lead_delete(request, id):
    LeadMaster.objects.filter(LeadID=id).delete()
    return redirect('lead_list')


# Lead to Customer
def lead_convert(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        if request.POST:
            lead_data = LeadMaster.objects.filter(LeadID=request.POST['lead_id']).values()[0]
            CustomerMaster.objects.create(CustName=lead_data['LeadName'], CustEmail=lead_data['LeadEmail'],
                                          CustMobile=lead_data['LeadMobile'], PurchasedCar=request.POST['car_name'],
                                          Amount=request.POST['amount'], OfferPrice=lead_data['OfferPrice'],
                                          Payment=lead_data['Payment'], Comment=lead_data['Comment'],
                                          Date=request.POST['date'], IsActive=1)
            car_data = InventoryMaster.objects.filter(RegNo=request.POST['RegNo']).values()[0]
            total_exp = InventoryMaster.objects.filter(RegNo=request.POST['RegNo']).values()[0]
            total_exp_list = []
            total_exp_list.append(int(car_data['BuyPrice']))
            total_exp_list.append(int(total_exp['Total_Expenses']))
            buy_exp = sum(total_exp_list)
            profit = int(request.POST['amount']) - int(buy_exp)
            SoldCarsMaster.objects.create(CarName=car_data['CarName'], OldCust=car_data['OldCust'],
                                          CarModel=car_data['CarModel'], Mfg=car_data['Mfg'],
                                          CarImage=car_data['CarImage'], RegNo=car_data['RegNo'],
                                          Engine=car_data['Engine'], Milage=car_data['Milage'], KWNo=car_data['KWNo'],
                                          BuyPrice=car_data['BuyPrice'], SellPrice=car_data['SellPrice'],
                                          CurrentCust=lead_data['LeadName'], Amount=request.POST['amount'],
                                          Total_Expenses=total_exp['Total_Expenses'], Buy_EXP=buy_exp, Profit=profit,
                                          Date=request.POST['date'])
            LeadgerMaster.objects.filter(RegNo=request.POST['RegNo']).update(Date=request.POST['date'],
                                                                             CarName=car_data['CarName'],
                                                                             RegNo=car_data['RegNo'],
                                                                             KWNo=car_data['KWNo'],
                                                                             Amount=request.POST['amount'],
                                                                             Vtype='Sales', FinalPrice='0')
            InventoryMaster.objects.filter(RegNo=request.POST['RegNo']).delete()
            LeadMaster.objects.filter(LeadID=request.POST['lead_id']).delete()
        return redirect('lead_list')
    else:
        return redirect('admin_login')


# Customers List
def cust_list(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        cust_detail = CustomerMaster.objects.all()
        context['cust_detail'] = cust_detail
        return render(request, 'customer.html', context)
    else:
        return redirect('admin_login')


# Customer View
def cust_view(request, id):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        cust_details = CustomerMaster.objects.filter(CustID=id).values()
        context['cust_details'] = cust_details
        return render(request, 'customer-view.html', context)
    else:
        return redirect('admin_login')


# Delete Customer
def cust_delete(request, id):
    CustomerMaster.objects.filter(CustID=id).delete()
    return redirect('cust_list')


# Sold Cars List
def sold_cars(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        sold_cars = SoldCarsMaster.objects.all()
        context['sold_cars'] = sold_cars
        return render(request, 'sold-cars.html', context)
    else:
        return redirect('admin_login')


# All Reports
def all_rep(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        return render(request, 'reports.html', context)
    else:
        return redirect('admin_login')


# Sales Report View
def sales(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        if request.POST:
            s_d = SoldCarsMaster.objects.filter(Date__range=[request.POST['f_date'], request.POST['t_date']]).values()
            context['s_d'] = s_d
            request.session['from'] = request.POST['f_date']
            request.session['to'] = request.POST['t_date']
        return render(request, 'sales-report.html', context)
    else:
        return redirect('admin_login')


# Sales Report
class sales_rep(View):
    def get(self, request, *args, **kwargs):
        context = {}
        from_date = request.session['from']
        context['from_date'] = from_date
        to_date = request.session['to']
        context['to_date'] = to_date
        sold_cars = SoldCarsMaster.objects.filter(Date__range=[from_date, to_date]).values()
        context['sold_cars'] = sold_cars
        counter = collections.Counter()
        total = []
        for d in sold_cars:
            total.append(int(d['Amount']))
        total = sum(total)
        context['total'] = total
        pdf = render_to_pdf('sales-pdf.html', context)
        del request.session['from']
        del request.session['to']
        return HttpResponse(pdf, content_type='application/pdf')


# Expence Report View
def expense(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        if request.POST:
            request.session['from'] = request.POST['f_date']
            request.session['to'] = request.POST['t_date']
            expense_details = InventoryMaster.objects.filter(
                Date__range=[request.POST['f_date'], request.POST['t_date']]).values()
            context['expense_details'] = expense_details
        return render(request, 'expense-report.html', context)
    else:
        return redirect('admin_login')


# Expence Report
class exp_rep(View):
    def get(self, request, *args, **kwargs):
        context = {}
        from_date = request.session['from']
        context['from_date'] = from_date
        to_date = request.session['to']
        context['to_date'] = to_date
        expense_details = InventoryMaster.objects.filter(Date__range=[from_date, to_date]).values()
        context['expense_details'] = expense_details
        counter = collections.Counter()
        total = []
        for d in expense_details:
            total.append(int(d['Total_Expenses']))
        total = sum(total)
        context['total'] = total
        pdf = render_to_pdf('expense-pdf.html', context)
        del request.session['from']
        del request.session['to']
        return HttpResponse(pdf, content_type='application/pdf')


# Profit Report View
def profit(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        if request.POST:
            request.session['from'] = request.POST['f_date']
            request.session['to'] = request.POST['t_date']
            sold_details = SoldCarsMaster.objects.filter(
                Date__range=[request.POST['f_date'], request.POST['t_date']]).values()
            context['sold_details'] = sold_details
        return render(request, 'profit-report.html', context)
    else:
        return redirect('admin_login')


# Profit Report
class profit_rep(View):
    def get(self, request, *args, **kwargs):
        context = {}
        from_date = request.session['from']
        context['from_date'] = from_date
        to_date = request.session['to']
        context['to_date'] = to_date
        sold_details = SoldCarsMaster.objects.filter(Date__range=[from_date, to_date]).values()
        context['sold_details'] = sold_details
        counter = collections.Counter()
        total = []
        for d in sold_details:
            total.append(int(d['Profit']))
        total = sum(total)
        context['total'] = total
        pdf = render_to_pdf('profit-pdf.html', context)
        del request.session['from']
        del request.session['to']
        return HttpResponse(pdf, content_type='application/pdf')


# Inventory Report View
def inventory_rep(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        if request.POST:
            request.session['from'] = request.POST['f_date']
            request.session['to'] = request.POST['t_date']
            Inventory = InventoryMaster.objects.all().values('CarName', 'CarModel', 'RegNo', 'FinalPrice', 'KWNo')
            context['Inventory'] = Inventory
        return render(request, 'inventory-report.html', context)
    else:
        return redirect('admin_login')


# Inventory Report
class Inventory_rep(View):
    def get(self, request, *args, **kwargs):
        context = {}
        from_date = request.session['from']
        context['from_date'] = from_date
        to_date = request.session['to']
        context['to_date'] = to_date
        Inventory = InventoryMaster.objects.all().values('CarName', 'CarModel', 'RegNo', 'FinalPrice', 'KWNo')
        context['Inventory'] = Inventory
        counter = collections.Counter()
        total = []
        for d in Inventory:
            total.append(int(d['FinalPrice']))
        total = sum(total)
        context['total'] = total
        pdf = render_to_pdf('inventory-pdf.html', context)
        del request.session['from']
        del request.session['to']
        return HttpResponse(pdf, content_type='application/pdf')


# ledger Report View
def ledger(request):
    if 'login' in request.session:
        context = {}
        user = request.session['user_name']
        context['user'] = user
        if request.POST:
            request.session['from'] = request.POST['f_date']
            request.session['to'] = request.POST['t_date']
            sold_details = LeadgerMaster.objects.all().values()
            context['sold_details'] = sold_details
        return render(request, 'ledger-report.html', context)
    else:
        return redirect('admin_login')


# Ledger Report
class ledger_rep(View):
    def get(self, request, *args, **kwargs):
        context = {}
        from_date = request.session['from']
        context['from_date'] = from_date
        to_date = request.session['to']
        context['to_date'] = to_date
        sold_details = LeadgerMaster.objects.all().values()
        # print(sold_details)
        context['sold_details'] = sold_details
        counter = collections.Counter()
        credit = []
        for d in sold_details:
            credit.append(int(d['Amount']))
        credit = sum(credit)
        context['credit'] = credit
        counter = collections.Counter()
        debit = []
        for d in sold_details:
            debit.append(int(d['FinalPrice']))
        debit = sum(debit)
        context['debit'] = debit
        pdf = render_to_pdf('ledger-pdf.html', context)
        del request.session['from']
        del request.session['to']
        return HttpResponse(pdf, content_type='application/pdf')


# Sell This Car
def sell_car(request, id):
    context={}
    # if request.is_ajax and request.method=="GET":
    # 	print('HELLO')
    # 	lead_data=LeadMaster.objects.all().values('LeadName')[0]['LeadName']
    # 	context['lead_data']=lead_data

    # return JsonResponse({"valid":lead_data}, status = 200)
    return render(request, 'sell-car.html', context)
# Sell This Car
# def sell_car(request, id):
# if request.is_ajax and request.method=="GET":
# 	print('HELLO')
# 	lead_data=LeadMaster.objects.all().values('LeadName')[0]['LeadName']
# 	context['lead_data']=lead_data

# return JsonResponse({"valid":lead_data}, status = 200)
# return render(request, 'sell-car.html', context)

# def lead_names(request):
# 	if request.is_ajax and request.method=="GET":
# 		list_name=['RAJ','AA']

# 	return JsonResponse({"valid":'lead_data'}, status = 200)
