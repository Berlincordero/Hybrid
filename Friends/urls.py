from django.urls import path
from .views import (
    friends_suggestions_view,
    send_friend_request_view,
    accept_friend_request_view,
    reject_friend_request_view,
    cancel_friend_request_view,
    friends_list_view,  # Agregamos la vista de lista de amigos
)

urlpatterns = [
    path('suggestions/', friends_suggestions_view, name='friends_suggestions'),
    path('send-request/<int:user_id>/', send_friend_request_view, name='send_friend_request'),
    path('accept-request/<int:request_id>/', accept_friend_request_view, name='accept_friend_request'),
    path('reject-request/<int:request_id>/', reject_friend_request_view, name='reject_friend_request'),
    path('cancel-request/<int:request_id>/', cancel_friend_request_view, name='cancel_friend_request'),
    path('my-friends/', friends_list_view, name='friends_list'),
]
