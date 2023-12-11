from datetime import datetime, timedelta
 # Assuming your Trip model is in myapp.models
import datetime
def send_trip_notifications():
    # Current time
    now = datetime.datetime.now()
    today_date = datetime.datetime.today().strftime('%d/%m/%Y')

    # Time four hours from now
    four_hours_later = now + timedelta(hours=4)
    print(now)
    print(today_date)
    print(four_hours_later)

    # Find trips that are starting in four hours
    # trips = Trip.objects.filter(starting_time__range=[now, four_hours_later])

    # for trip in trips:
    #     driver = trip.truck_driver_id  # Assuming each trip has a related driver
    #     # Send notification to the driver
    #     # Implement your notification logic here, e.g., send email or SMS

send_trip_notifications()