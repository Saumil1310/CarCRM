from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from app import views

urlpatterns=[
	path('index/', views.index, name='index'),
	path('inventory/', views.inventory, name='inventory'),
	path('car_list/', views.car_list, name='car_list'),
	path('update_car?id=<id>', views.update_car, name='update_car'),
	path('car_view?id=<id>', views.car_view, name='car_view'),
	path('car_delete/', views.car_delete, name='car_delete'),
	path('add_lead/', views.add_lead, name='add_lead'),
	path('lead_list/', views.lead_list, name='lead_list'),
	path('lead_view?id=<id>', views.lead_view, name='lead_view'),
	path('lead_update?id=<id>', views.lead_update, name='lead_update'),
	path('lead_delete/', views.lead_delete, name='lead_delete'),
	path('lead_convert', views.lead_convert, name='lead_convert'),
	path('cust_list/', views.cust_list, name='cust_list'),
	path('cust_view?id=<id>', views.cust_view, name='cust_view'),
	path('cust_delete/', views.cust_delete, name='cust_delete'),
	path('sold_cars/', views.sold_cars, name='sold_cars'),
	path('sold_view?id=<id>', views.sold_view, name='sold_view'),
	path('admin_reg/', views.admin_register, name='admin_reg'),
	path('admin_login/', views.admin_login, name='admin_login'),
	path('logout/',views.logout,name='logout'),
	path('all_rep/', views.all_rep, name='all_rep'),
	path('sales/',  csrf_exempt(views.sales), name='sales'),
	path('sales_rep/', views.sales_rep.as_view(), name='sales_rep'),
	path('expense/', views.expense, name='expense'),
	path('exp_rep/', views.exp_rep.as_view(), name='exp_rep'),
	path('profit/', views.profit, name='profit'),
	path('profit_rep/', views.profit_rep.as_view(), name='profit_rep'),
	path('inventory_rep/', views.inventory_rep, name='inventory_rep'),
	path('Inventory_rep/', views.Inventory_rep.as_view(), name='Inventory_rep'),
	path('ledger/', views.ledger, name='ledger'),
	path('ledger_rep/', views.ledger_rep.as_view(), name='ledger_rep'),
	path('sell_car?id=<id>', views.sell_car, name='sell_car'),
	path('temp/', csrf_exempt(views.temp), name='temp'),
	path('invoice?id=<id>', views.invoice, name='invoice'),
	# path('lead_ajax/', csrf_exempt(views.lead_ajax), name='lead_ajax'),
	path('car_ajax/', csrf_exempt(views.car_ajax), name='car_ajax'),
]