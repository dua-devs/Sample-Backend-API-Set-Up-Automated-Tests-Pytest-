from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer


@api_view(["GET", "POST"])
def bookings_view(request):

    # GET → يرجع كل الحجوزات
    if request.method == "GET":
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST → إنشاء حجز جديد
    if request.method == "POST":
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Sum

TOTAL_SEATS_PER_FLIGHT = 20

@api_view(["GET"])
def availability_view(request):
    flight_id = request.query_params.get("flight_id")
    travel_date = request.query_params.get("travel_date")
    seats = request.query_params.get("seats")

    # تحقق من وجود البيانات
    if not flight_id or not travel_date or not seats:
        return Response(
            {"error": "flight_id, travel_date, and seats are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        flight_id = int(flight_id)
        seats = int(seats)
    except ValueError:
        return Response({"error": "flight_id and seats must be integers"}, status=status.HTTP_400_BAD_REQUEST)

    if seats <= 0:
        return Response({"error": "seats must be greater than 0"}, status=status.HTTP_400_BAD_REQUEST)

    # حساب المقاعد المحجوزة لهذه الرحلة في هذا التاريخ
    total_booked = (
        Booking.objects.filter(flight_id=flight_id, travel_date=travel_date)
        .aggregate(total=Sum("seats"))
        .get("total") or 0
    )

    remaining = TOTAL_SEATS_PER_FLIGHT - total_booked
    available = remaining >= seats

    return Response(
        {"available": available, "remaining_seats": max(0, remaining)},
        status=status.HTTP_200_OK
    )
