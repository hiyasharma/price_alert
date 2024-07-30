from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Alert
from rest_framework import generics
from .serializers import AlertSerializer
from .binance_websocket import btc_price
from rest_framework import status



class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class AlertCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    def create(self, request, *args, **kwargs):
        request.data['username']=request.user.username
        request.data['currentPrice']=btc_price['price']
        return super().create(request, *args, **kwargs)

class AlertList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class AlertDelete(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class AlertUpdate(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class BitcoinPriceAlert(APIView):
    def get(self, request):
        try:
            price = btc_price['price']
            return Response({'bitcoin_price': price}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)