from django.urls import *
from rest_framework.routers import DefaultRouter
from .views import *
from .serializers import *
from Bachatgat import views

router = DefaultRouter()
router.register("bachatgat", BachatGatRegistrationViewSet),
router.register("member_registration",MemberRegistrationViewSet),
router.register("bank_detail",BankDetailsViewSet),
router.register("users",UserDetailViewSet),
router.register("saving_user",SavingsViewSet),
router.register("loan_",LoanViewSet),
router.register("fund_distribution",FundDistributionViewSet),

urlpatterns = [
    *router.urls,
    path('',include(router.urls)),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),

]