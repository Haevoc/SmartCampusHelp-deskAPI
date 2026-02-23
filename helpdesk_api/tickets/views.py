from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from django.db.models import Q

from .models import Ticket
from .serializers import TicketSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def ticket_list(request):
    if request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    tickets = Ticket.objects.all()

    # FILTERING
    category = request.query_params.get('category')
    status = request.query_params.get('status')
    if category:
        tickets = tickets.filter(category=category)
    if status:
        tickets = tickets.filter(status=status)

    # SEARCH
    search = request.query_params.get('search')
    if search:
        tickets = tickets.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )

    # ORDERING
    ordering = request.query_params.get('ordering')
    if ordering:
        tickets = tickets.order_by(ordering)

    # PAGINATION
    paginator = PageNumberPagination()
    paginator.page_size = 2
    paginated = paginator.paginate_queryset(tickets, request)

    serializer = TicketSerializer(paginated, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def ticket_detail(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return Response({'error': 'Ticket not found'}, status=404)

    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    if request.method == 'PATCH':
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        ticket.delete()
        return Response({'message': 'Ticket deleted'})