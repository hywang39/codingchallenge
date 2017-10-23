from django.shortcuts import render
from challenge.models import FoodEntry, Serving, FoodCategory, FoodDetailCategory, DirectionalStatement
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from challenge.serializers import FoodEntrySerializer, ServingSerializer \
    , FoodCategorySerializer, FoodDetailCategorySerializer, DirectionalStatementSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
import json

# Create your views here.

def home(request):
    return render(request, template_name='main_page.html')


# def fix_food_category_id():
#     queryset = FoodEntry.objects.all()
#     for obj in queryset:
#         if obj.food_detail_category_id <=2:
#             obj.food_category_id = 1
#         if (obj.food_detail_category_id==3 or obj.food_detail_category_id ==4):
#             obj.food_category_id = 2
#         if (obj.food_detail_category_id==5 or obj.food_detail_category_id==6):
#             obj.food_category_id = 3
#         if (obj.food_detail_category_id ==7 or obj.food_detail_category_id ==8):
#             obj.food_category_id = 4
#         obj.save()
#

#
# @csrf_exempt
# def foodentry_list(request):
#     if request.method == 'GET':
#         foodentries = foodentry.objects.all()
#         serializer = FoodEntrySerializer(foodentries, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#
# @csrf_exempt
# def serving_list(request):
#     if request.method == 'GET':
#         servings = serving.objects.all()
#         serializer = ServingSerializer(servings, many=True)
#         return JsonResponse(serializer.data, safe=False)
#


from rest_framework import generics
from itertools import chain

#
#
# class FoodEntryList(APIView):
#     def get(self,request,format=None):
#         foodentries = foodentry.objects.all()
#         serializer = FoodEntrySerializer(foodentries, many=True)
#         return Response(serializer.data)
#
# class ServingList(APIView):
#     def get(self,request,format=None):
#         servings = serving.objects.all()
#         serializer = ServingSerializer(servings, many=True)
#         return Response(serializer.data)

class ServingList(generics.ListCreateAPIView):
    queryset = Serving.objects.all()
    def get(self, request, age, gender):
        queryset = self.get_queryset()
        queryset = queryset.filter(age_lower__lte = age, age_upper__gte = age,gender=gender)

        numList = []
        food_category_list = queryset.values('food_category_id').all()
        for obj in food_category_list:
            numList.append(obj['food_category_id'])

        queryset2 = FoodEntry.objects.filter(food_category_id__in=numList)

        serializer1 = ServingSerializer(queryset, many=True)
        serializer2 = FoodEntrySerializer(queryset2, many=True)

        return JsonResponse({'serving':serializer1.data,'foodentry': serializer2.data},safe=False)


class ServingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Serving.objects.all()
    serializer_class = ServingSerializer


