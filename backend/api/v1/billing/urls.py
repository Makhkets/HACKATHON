from django.urls import path

from api.v1.billing.views import SingleBillingAccountView, TransactionsListView, UserBillingAccountView

urlpatterns = [
    path('account/<int:pk>', SingleBillingAccountView.as_view()),
    path('useraccount', UserBillingAccountView.as_view()),
    path('transactions', TransactionsListView.as_view()),
]