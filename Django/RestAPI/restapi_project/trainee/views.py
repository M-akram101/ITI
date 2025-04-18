from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trainee
from .serializer import TraineeSerializer


# Generic View for GET (Retrieve) and DELETE
class TraineeDetailView(RetrieveDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer


# Class-Based View for POST (Create) and PUT (Update)
class TraineeCreateUpdateView(APIView):
    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TraineeSerializer(trainee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
