from django.urls import path, include

urlpatterns = [
    path('category/', include('apps.category.urls')),
    path('feedback/', include('apps.feedback.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('type-food/', include('apps.kitchen.urls.typefood_urls')),
    path('food/', include('apps.kitchen.urls.food_urls')),
]
