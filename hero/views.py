from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import serializers

from hero.models import SuperHero



# Create your views here.

class HeroListCreateView(APIView):

    def get(self,request):

        qs = SuperHero.objects.all().values()

        hero_list=list(qs)

        return Response(data=hero_list)

    def post(self,request):

        form_data = request.data

        universe = form_data.get("universe")

        if universe not in SuperHero.UNIVERSE_OPTIONS:

            raise serializers.ValidationError("invalid universe  !!!")

        SuperHero.objects.create(**form_data)

        return Response(data={"message":"created..."})

class HeroRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        qs = SuperHero.objects.filter(id=pk).values()

        hero_list=list(qs)

        return Response(data=hero_list)

    def put(self,request,pk=None):

        form_data = request.data

        qs = SuperHero.objects.filter(id=pk).update(**form_data)

        return Response(data={"message":"updated..."})

    def delete(self,request,pk=None):

        qs = SuperHero.objects.filter(id=pk).delete()

        return Response(data={"message":"deleted.... "})
    

