from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from msg_api.quickstart.serializers import UserMessageSerializer
from msg_api.quickstart.models import UserMessage
from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User



# Create your views here.
class CreateMessage(generics.CreateAPIView):
    """
    Write message
    """
    serializer_class = UserMessageSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        sender = User.objects.filter(username=data.get('sender')).first()
        receiver = User.objects.filter(username=data.get('receiver')).first()
        msg_params = {
            'sender': sender,
            'receiver': receiver,
            'subject': data.get("subject"), 
            'message': data.get("message"),
        }
        msg = UserMessage(**msg_params)
        msg.save()
        serializer = self.serializer_class(msg)
        return Response(serializer.data)


class GetAllUserMessages(generics.ListAPIView):
    """
    Get all messages for a specific user
    """
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    
    def get( self, request, *args, **kwargs ):
        username = kwargs.get('username')
        self.queryset = self.queryset.filter(sender_id__username=username)
        return self.list(request, *args, **kwargs)

class GetAllUnreadUserMessages(generics.ListAPIView):
    """
    Get all unread messages for a specific user
    """
    queryset = UserMessage.objects.filter(unread=True)
    serializer_class = UserMessageSerializer

    def list( self, request, *args, **kwargs ):
        username = kwargs.get('username')
        queryset = self.get_queryset().filter(sender_id__username=username)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class ReadMessage(generics.RetrieveAPIView):
    """
    Read message (return one message)
    """
    queryset = UserMessage.objects.filter(unread=True).order_by('creation_date')
    serializer_class = UserMessageSerializer

    def retrieve( self, request, *args, **kwargs ):
        username = kwargs.get('username')
        message = self.get_queryset().filter(sender_id__username=username).first()
        if message:
            message.unread = False
            message.save()
            serializer = self.serializer_class(message)
            return Response(serializer.data)
        else:
            return Response()


class DeleteMessage(generics.DestroyAPIView):
    """
    Delete message (as owner or as receiver)
    """
    queryset = UserMessage.objects.all()

    def destroy(self, reqest,*args, **kwargs ): 
        message_id = kwargs.get('id')
        message = self.get_queryset().filter(id=message_id).first()
        if message:
            message.delete()
        return Response(status=status.HTTP_200_OK)