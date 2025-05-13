from data_access.booking_data_access import BookingDataAccess

# Initialize the BookingDataAccess
test_init = BookingDataAccess()

# Test Data
guest_id = 6
room_id = 6

print("Testing BookingDataAccess")

# Create a Booking
print("\nCreating a booking: ")
check_in_date = "2025-06-01"
check_out_date = "2025-06-05"
total_amount = 578.98

booking_id, _ = test_init.create_booking(str(check_in_date), str(check_out_date), int(guest_id), int(room_id), float(total_amount))
print(f"Booking has been created with ID: {booking_id}")

# Fetch all bookings
print("\nFetching all available bookings: ")
all_bookings = test_init.get_all_bookings()
for booking in all_bookings:
    print(booking)

# Fetch booking by guest ID
print("\nFetching booking by guest ID: ")
guest_bookings = test_init.get_booking_by_guest_id(guest_id)
for booking in guest_bookings:
    print(booking)

# Update the booking
print("\nUpdate my bookings: ")
new_check_in_date = "2025-06-05"
new_check_out_date = "2025-06-15"
new_total_amount = 785.55

test_init.update_booking(int(booking_id), str(new_check_in_date), str(new_check_out_date), float(new_total_amount))
print(f"Booking has been updated with ID: {booking_id}")

# Fetch the updated booking
print("\nFetch the updated booking: ")
updated_booking = test_init.get_booking_by_id(booking_id)
print(updated_booking)

# Delete the booking
print("\nDeleting a booking: ")
test_init.delete_booking(booking_id)
print(f"Booking has been deleted with ID: {booking_id}")

# Fetch all bookings to confirm deletion
print("\nFetch all bookings again: ")
all_bookings = test_init.get_all_bookings()
for booking in all_bookings:
    print(booking)