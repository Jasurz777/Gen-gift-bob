from django.urls import path
from .views import *
from dashboard.category import views as category
from dashboard.human import views as human
from dashboard.situation import views as situation
from dashboard.interests import views as interests
from dashboard.cash import views as cash
from dashboard.age import views as age
from dashboard.registiratsiya import views as reg_views
from dashboard.product import views as product

urlpatterns = [

    path("category", category.category, name="dash_category"),
    path("category/form", category.category_form, name="dash_category_form"),
    path("category/edit/<int:pk>/", category.category_edit, name="dash_category_edit"),
    path("category/delete/<int:pk>", category.delete_category, name='dash_category_delete'),
    path('category/delete/<int:dlt>/', category.delete_category, name="dash_category_delete"),

    path('human/', human.human_handler, name='dash_human'),
    path('human/add', human.human_add, name='dash_human_add'),
    path('human/edit/<int:pk>/', human.edit, name='dash_human_edit'),
    path("human/delete/<int:pk>", human.delete_human, name='dash_human_delete'),
    path('human/delete/<int:dlt>/', human.delete_human, name="dash_human_delete"),

    path("situation/", situation.situation_handler, name='dash_situation'),
    path("situation/add/", situation.situation_add, name='dash_situation_add'),
    path("situation/edit/<int:pk>/", situation.edit, name='dash_situation_edit'),
    path("situation/delete/<int:pk>", situation.delete_situation, name='dash_situation_delete'),
    path('situation/delete/<int:dlt>/', situation.delete_situation, name="dash_situation_delete"),

    path("", index, name='dashboardHome'),
    path("interests/", interests.interests_list, name='dash_tables'),
    path("interests/edit/<int:pk>/", interests.edit_interests, name='dash_interests_edit'),
    path("interests/add/", interests.add_interests, name='dash_interests_add'),
    path("interests/delete/<int:pk>", interests.delete_interests, name='dash_interests_delete'),
    path('interests/delete/<int:dlt>/', interests.delete_interests, name="dash_interests_delete"),

    path("cash/", cash.fact_list, name='dash_cash_list'),
    path("cash/add", cash.add, name='dash_cash_add'),
    path("cash/edit/<int:pk>/", cash.edit_cash, name='dash_cash_edit'),
    path("cash/delete/<int:pk>", cash.delete_cash, name='dash_cash_delete'),
    path('cash/delete/<int:dlt>/', cash.delete_cash, name="dash_cash_delete"),

    path("age", age.age_list, name="dash_age_list"),
    path("age/add", age.age_add, name="dash_age_list_add"),
    path("age/edit/<int:pk>/", age.age_edit, name="dash_age_list_edit"),
    path("age/delete/<int:pk>", age.age_delete, name='dash_age_delete'),
    path('age/delete/<int:dlt>/', age.age_delete, name="dash_age_delete"),

    path('product/', product.product_list, name='dash_product'),
    path('product/add/', product.product_add, name='dash_product_add'),
    path('product/edit/<int:pk>/', product.product_edit, name='dash_product_edit'),
    path("product/delete/<int:pk>", product.delete_product, name='dash_product_delete'),
    path('product/delete/<int:dlt>/', product.delete_product, name="dash_product_delete"),

    path("register/register", reg_views.register, name="dash_register_reg"),
    path("register/add", reg_views.register_add, name="dash_register_add"),
    path("register/edit/<int:pk>/", reg_views.register_edit, name="dash_register_edit"),
    path("register/", register, name="dash_register"),
    path("register/delete/<int:pk>", reg_views.delete_register, name='dash_register_delete'),
    path('register/delete/<int:dlt>/', reg_views.delete_register, name="dash_register_delete"),

    path('login/', dash_login, name='dash_login'),
    path('login/logout', dash_logout, name='dash_logout'),
    path('account/', account, name='dash_account'),
    path('passwordChange', changePassword, name='dash_password_change')

]



