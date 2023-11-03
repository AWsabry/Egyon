from django.shortcuts import render
from categories_and_products.models import (
    Category,

    Product,
    Vendor,

)
from django.http import JsonResponse
from rest_framework import status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view
from rest_framework.response import Response
from categories_and_products.serializers import CategorySerializer, ProductsSerializer, RestaurantSerializer
from rest_framework.views import APIView

def index(request):
    return render(request,"index.html")

# APIs Handling

@api_view(['GET','POST'])
# Getting Restaurants
def get_restaurants(request,):
    if request.method == 'GET':
        all = Vendor.objects.filter(active = True,)
        serializer = RestaurantSerializer(all,many = True,)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = RestaurantSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET','POST'])
# Getting Restaurants by id
def get_restaurants_by_id(request,id):
    if request.method == 'GET':
        all = Vendor.objects.filter(active = True,id=id)
        serializer = RestaurantSerializer(all,many = True,)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = RestaurantSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET','POST'])
# Getting Categories
def get_category(request,):
    if request.method == 'GET':
        all = Category.objects.filter(active = True,)
        serializer = CategorySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = CategorySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET','POST'])
# Getting Categories by id
def get_category_by_id(request,id):
    if request.method == 'GET':
        all = Category.objects.filter(active = True,id=id)
        serializer = CategorySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = CategorySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET','POST'])
# Getting Restaurants Category
def get_category_of_restaurants(request,id):
    if request.method == 'GET':
        all = Category.objects.filter(active = True,Restaurant__id = id)
        serializer = CategorySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = CategorySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET','POST'])
# Getting Products
def get_products(request):
    if request.method == 'GET':
        all = Product.objects.filter(active = True)
        serializer = ProductsSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = ProductsSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET','POST'])
# Getting Products by id
def get_products_by_id(request,id):
    if request.method == 'GET':
        all = Product.objects.filter(active = True,id=id)
        serializer = ProductsSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = ProductsSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

# Getting Most Sold Products
class GetMostSoldProducts(APIView):
    def get(self, request, location_id):
        products = Product.objects.filter(active=True, Most_Popular=True, Restaurant__locations__id=location_id)
        serializer = ProductsSerializer(products, many=True)
        return Response({"Names": serializer.data})

# Getting New Products
class GetNewProducts(APIView):
    def get(self, request, location_id):
        products = Product.objects.filter(active=True, New_Products=True, Restaurant__locations__id=location_id)
        serializer = ProductsSerializer(products, many=True)
        return Response({"Names": serializer.data})


# Getting Best Offer
class GetBestOfferProducts(APIView):
    def get(self, request, location_id):
        products = Product.objects.filter(active=True, Best_Offer=True, Restaurant__locations__id=location_id)
        serializer = ProductsSerializer(products, many=True)
        return Response({"Names": serializer.data})



# Getting Products by restaurant id
class GetProductsByRestaurantId(APIView):
    def get(self, request, id):
        products = Product.objects.filter(active=True, Restaurant__id=id)
        serializer = ProductsSerializer(products, many=True)
        return Response({"Names": serializer.data})

# Getting Products by restaurant & category
class GetProductsByRestaurantAndCategory(APIView):
    def get(self, request, restaurant_id, category_id):
        products = Product.objects.filter(active=True, Restaurant__id=restaurant_id, category__id=category_id)
        serializer = ProductsSerializer(products, many=True)
        return Response({"Names": serializer.data})




        





    

# Getting Searched Restaurants
class GetSearchedRestaurants(APIView):
    def get(self, request, searched):
        if searched:
            restaurants = Vendor.objects.filter(active=True, Name__icontains=searched)

            if restaurants.exists():
                serializer = RestaurantSerializer(restaurants, many=True)
                response_data = {"Names": serializer.data}
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No matching restaurants found"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"message": "Please provide a search query"}, status=status.HTTP_403_FORBIDDEN)

# Getting Searched Products in Restaurants
class GetSearchedProductsInRestaurant(APIView):
    def get(self, request, searched, restaurant):
        if searched:
            products = Product.objects.filter(
                active=True,
                Restaurant__Name__iregex=restaurant,
                name__icontains=searched
            )

            if products.exists():
                serializer = ProductsSerializer(products, many=True)
                response_data = {"Names": serializer.data}
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No matching products found"}, status=status.HTTP_403_FORBIDDEN,safe=False)
        else:
            return Response({"message": "Please provide a search query"}, status=status.HTTP_403_FORBIDDEN,safe=False)
        



# Getting Searched Products
class get_searched_products(APIView):
    def get(self,request,searched):
        if searched:
            englishName = Product.objects.filter(active = True,name__icontains = searched,)
            englishSerializer = ProductsSerializer(englishName,many = True,)
            if englishName :
               return JsonResponse({"Names": englishSerializer.data}, safe=False)
            else:
                arabicName = Product.objects.filter(active = True,ArabicName__icontains = searched,)
                arabicSerializer = ProductsSerializer(arabicName,many = True,)
                return JsonResponse({"Names": arabicSerializer.data}, safe=False)
        else:
            return JsonResponse('No Values Found', safe=False)


class get_restaurants_by_location(APIView):
    def get(self,request,location_slug):
        all = Vendor.objects.filter(active = True,locations__location_slug=location_slug)
        serializer = RestaurantSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)

