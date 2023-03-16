from django.urls import path
from . import views

urlpatterns = [
    # URLs, aka routes in express
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='index'),
    path('vinyls/<int:vinyl_id>', views.vinyls_detail, name='detail'),
    path('vinyls/create', views.VinylCreate.as_view(), name='vinyls_create'),
    path('vinyls/<int:pk>/update', views.VinylUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('accounts/signup', views.signup, name='signup'),
    path('recordplayers/', views.RecordPlayerList.as_view(), name='recordplayers_index'),
    path('recordplayers/<int:pk>', views.RecordPlayerDetail.as_view(), name='recordplayers_detail'),
    path('recordplayers/create', views.RecordPlayerCreate.as_view(), name='recordplayers_create'),
    path('recordplayers/update/<int:pk>', views.RecordPlayerUpdate.as_view(), name='recordplayers_update'),
    path('recordplayers/delete/<int:pk>', views.RecordPlayerDelete.as_view(), name='recordplayers_delete')


]