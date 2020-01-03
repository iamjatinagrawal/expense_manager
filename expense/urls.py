from django.conf.urls import url
from expense import views

app_name = 'expense'

urlpatterns = [
    url(r'^$',views.IndexView.as_view()),
    url(r'^list/',views.ExpenseListView.as_view(),name='list'),
    url(r'^create/$',views.CreateExpenseView.as_view(),name='create'),

]