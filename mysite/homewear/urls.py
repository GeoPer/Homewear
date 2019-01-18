from django.urls import path

from . import views
app_name = 'homewear'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /homewear/5/
    path('category/<int:category_id>/', views.detail_cat, name='detail_cat'),
    # ex: /homewear/5/
    path('product/<int:product_id>/', views.detail_prod, name='detail_prod'),
    # ex: /polls/5/results/
    path('category/<int:category_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('category/<int:category_id>/vote/', views.vote, name='vote'),
]