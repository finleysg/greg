from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import ContactMessage


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def contact_message(request):
    sender = request.data["full_name"]
    sender_email = request.data["email"]
    message_text = request.data["message_text"]
    message = ContactMessage(full_name=sender, email=sender_email, message_text=message_text)
    message.save()

    send_mail(
        "Contact Message from " + sender,
        message_text,
        sender_email,
        ["northernsummitconstruction@gmail.com", "finleysg@gmail.com", ]
    )

    return Response(data="message sent", status=201)
