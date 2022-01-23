from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import table , BookingTime
from .serializers import tableSerializer,BookingTimeSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class TableApi(APIView):
    def get(self,request):
        tables = table.objects.all()
        serializer = tableSerializer(tables,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        d = {}
        name = data['name']
        seats = data['seats']
        if(name != None and seats != None):
            tableobj = table.objects.create(name = name , seats = seats)
            tableobj.save()
            return Response(status=status.HTTP_201_CREATED)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
class BookingApi(APIView):
    def get_object(self,id):
        try :
            tbook = BookingTime.objects.get(id=id)
            return tbook
        except :
            return "NOT FOUND"

    def post(self,request,id):
        tablebook = table.objects.get(id=id)
        tbookings = BookingTime.objects.filter(tablebook = tablebook).order_by("stime")
        data = request.data
        stime = datetime.strptime(data["stime"], '%Y-%m-%dT%H:%M:%S.%fZ')
        etime = datetime.strptime(data["etime"], '%Y-%m-%dT%H:%M:%S.%fZ')
        stime.replace(tzinfo=None)
        etime.replace(tzinfo=None)
        n= len(tbookings)
        if(n==0 or n==None):
            tbookings = BookingTime.objects.create(tablebook = tablebook , stime = stime , etime = etime)
            d = {}
            d["Table"] = tablebook.name
            d["BookingId"] = tbookings.id
            d["stime"] = stime
            d["etime"] = etime
            return Response(d)
        for i, tbook in enumerate(tbookings):
            if(tbook.stime.replace(tzinfo=None) >= stime and tbook.stime.replace(tzinfo=None) >= etime and i == 0):
                tbookings = BookingTime.objects.create(tablebook = tablebook , stime = stime , etime = etime)
                d = {}
                d["Table"] = tablebook.name
                d["BookingId"] = tbookings.id
                d["stime"] = stime
                d["etime"] = etime
                return Response(d)
            elif (tbook.etime.replace(tzinfo=None) <= stime and i != n-1 and tbookings[i+1].stime.replace(tzinfo=None) >= etime):
                tbookings = BookingTime.objects.create(tablebook = tablebook , stime = stime , etime = etime)
                d = {}
                d["Table"] = tablebook.name
                d["BookingId"] = tbookings.id
                d["stime"] = stime
                d["etime"] = etime
                return Response(d)
            else :
                a=0
            if(i==n-1 and tbook.etime.replace(tzinfo=None) <= stime):
                tbookings = BookingTime.objects.create(tablebook = tablebook , stime = stime , etime = etime)
                d = {}
                d["Table"] = tablebook.name
                d["BookingId"] = tbookings.id
                d["stime"] = stime
                d["etime"] = etime
                return Response(d)
            else :
                a=0
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class BookingView(APIView):
    def get(self,request,id):
        tbook=self.get_object(id)
        if(tbook!="NOT FOUND"):
            serializer = BookingTimeSerializer(tbook)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND) 
    def delete(self,request,id):
        tbooking=self.get_object(id)
        tbooking.delete()
        return Response(status=status.HTTP_200_OK) 
class BookingShedule(APIView):
    def post(self,request):
        data = request.data
        stime = data["time"]
        dtime = datetime.strptime(stime, '%Y-%m-%dT%H:%M:%S.%fZ')
        etime =  dtime + timedelta(1)
        tables = table.objects.all()
        d={}
        for tablebook in tables:
            dfree=[]
            tbookings = BookingTime.objects.filter(tablebook = tablebook).order_by("stime")
            start = dtime
            n = len(tbookings)
            if(n==0 or n == None):
                dfree.append([start,etime])
            for i, tbook in enumerate(tbookings):
                comp = tbook.stime.replace(tzinfo=None)
                if(start.replace(tzinfo=None) < comp):
                    dfree.append([start,tbook.stime])
                    start = tbook.etime
                if(i== n-1):
                    comp = tbook.etime.replace(tzinfo=None)
                    if(comp < etime.replace(tzinfo=None)):
                        dfree.append([tbook.etime,etime])
            d[tablebook.name] = dfree
        return Response(d) 