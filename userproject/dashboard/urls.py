from django.urls import path
from . import views
from dashboard import views as dash_views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('adminlogin/',views.admin_login,name='adminlogin'),
    path('admindisplay/',views.admin_display,name='admindisplay'),
    path('edit_admindetail/<int:user_id>/',views.edit_admindetail,name='edit_admindetail'),
    path('adminedit_item/<int:item_id>/',views.admin_edititem,name='admin_edititem'),
    path('adminview_item/<int:item_id>/',views.admin_viewitem,name='admin_viewitem'),
    path('admin_approved/',views.admin_approved,name='admin_approved'),
    path('admin_rejected/',views.admin_rejected,name='admin_rejected'),



    
    path('logout/',views.logout_view,name='logout'),

    path('displayprofile/',views.profile_view,name='displayprofile'),
    path('editprofile/<int:user_id>/',views.profile_edit,name='editprofile'),
    path('additem/', views.item_add, name='additem'),
    path('viewtask/<int:item_id>/',views.item_view,name='viewtask'),

    path('edititem/<int:item_id>/',views.item_edit,name='edititem'),
    path('deleteitem/<int:item_id>/',views.item_delete,name='deleteitem'),
    path('approved_task/',views.approved_task,name='approved_task'),
    path('rejected_task/',views.rejected_task,name='rejected_task'),



    ]
