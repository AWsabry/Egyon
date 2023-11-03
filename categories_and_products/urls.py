from django.urls import path
from categories_and_products import views as Api_handling
app_name = 'categories_and_products'


urlpatterns = [
    path('', view=Api_handling.index, name='index'),


    # APIs URL
    path('get_category/', view=Api_handling.get_category, name='get_category'),
    path('get_category_by_id/<int:id>', view=Api_handling.get_category_by_id, name='get_category_by_id'),
    path('get_category_of_restaurants/<int:id>', view=Api_handling.get_category_of_restaurants, name='get_category_of_restaurants'),

    
    
    path('get_products/', view=Api_handling.get_products, name='get_products'),
    path('get_products_by_id/<int:id>', view=Api_handling.get_products_by_id, name='get_products_by_id'),
    path('get_products_mostSold_products/<int:location_id>', view=Api_handling.GetMostSoldProducts.as_view(), name='get_products_mostSold_products'),
    path('  /<int:location_id>', view=Api_handling.GetNewProducts.as_view(), name='get_products_new_products'),
    path('get_best_offer_products/<int:location_id>', view=Api_handling.GetBestOfferProducts.as_view(), name='get_best_offer_products'),
    
    path('get_products_by_restaurant_id/<int:id>', view=Api_handling.GetProductsByRestaurantId.as_view(), name='get_products_by_restaurant_id'),
    path('get_products_of_restaurant_by_category/<str:restaurant_id>/<str:category_id>', view=Api_handling.GetProductsByRestaurantAndCategory.as_view(), name='get_products_of_restaurant_by_category'),




    path('get_restaurants_by_id/<int:id>', view=Api_handling.get_restaurants_by_id, name='get_restaurants_by_id'),
    path('get_restaurants/', view=Api_handling.get_restaurants, name='get_restaurants'),
    path('get_restaurants_by_location/<str:location_slug>', view=Api_handling.get_restaurants_by_location.as_view(), name='get_restaurants_by_location'),




    path('get_searched_products/<str:searched>', Api_handling.get_searched_products.as_view(), name='get_searched_products'),
    path('get_searched_restaurants/<str:searched>', Api_handling.GetSearchedRestaurants.as_view(), name='get_searched_restaurants'),
    path('get_searched_products_in_restaurant/<str:restaurant>/<str:searched>', Api_handling.GetSearchedProductsInRestaurant.as_view(), name='get_searched_products_in_restaurant'),





    

]
