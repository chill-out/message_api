from rest_framework import serializers
from msg_api.quickstart.models import UserMessage

class UserMessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    class Meta:
        model = UserMessage
        fields = ['sender', 'receiver', 'subject', 'message', 'id']
    
    def get_sender(self, obj):
        if obj.sender:
            return obj.sender.username
        return ''
    
    def get_receiver(self, obj):
        if obj.receiver:
            return obj.receiver.username
        return ''

    # @classmethod
    # def get_extra_actions(cls):
    #     return []
