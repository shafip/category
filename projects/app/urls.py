from django.urls import path
from . import views
from .views import *

from .views import CourseView
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.home,name="home"),
    #

    path('categoryform', views.CategoryForms,name="catform"),
    path('catogoryview', views.serchcategory,name='cat-table'),
    path('update/<str:pk>/', views.updatecat, name='updatecat'),
    path('category/enable/',views.enableview, name='cat-enable'),
     path('cdisable/<str:pk>/', views.disableview, name='disable'),


    path('subcat/',views.subforms,name="subform"),
    path('subtable/',views.serchsubcategory,name="subtable"),
    path('updatesub/<str:pk>/', views.updatesub, name='update_sub'),
    path('delete/<str:pk>/', views.delete, name='deletesub'),
    path('subcat/subenable/',views.subenableview, name='enablesub'),
    path('disablesub/<str:pk>/', views.disablesub, name='disablesub'),

    path('courseform/', views.CourseView.as_view(), name="courseform"),
    path('coursetable', views.coursepageview, name="cotable"),
    path('c-update/<int:pk>/', views.UpdateViews.as_view(), name='c_update'),
    path('course/enable/',views.co_disable, name='co-disable'),
    path('coenable/<int:pk>', views.EnableView.as_view(), name='co-enable'),
    #
    # # #
    path('topicform/', views.TopicView.as_view(), name="topicform"),
    path('topictable/', views.TopicTable.as_view(), name="topictable"),
    path('t-update/<int:pk>/', views.UpdateTopicView.as_view(), name='t_update'),
    path('topicdisable/<int:pk>', views.DeleteViewTopic.as_view(), name='to-disable'),
    path('topiccoenable/<int:pk>', views.EnableViewTopic.as_view(), name='to-enable'),
    #
    #
    #
    #
    # path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logins/', auth_view.LoginView.as_view(template_name='login/login.html'), name="login"),
    path('logout/',auth_view.LogoutView.as_view(template_name='home.html'),name="logout")


]