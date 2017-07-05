from django.conf.urls import url
# from booktest import views
# import
from booktest import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^delete/(\d+)',views.delete)

]



