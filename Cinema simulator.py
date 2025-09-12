# Cinema simulator 

movies = {
    "1": {"name": "Movie A", "seats": [False]*5, "time": "6 PM"},
    "2": {"name": "Movie B", "seats": [False]*5, "time": "9 PM"}
}

for mid in movies:
    print(f"{mid}: {movies[mid]['name']} at {movies[mid]['time']}")

choice = input("Select movie (1 or 2): ")
if choice in movies:
    seats = movies[choice]["seats"]
    print("Seats status:", ["Free" if not s else "Booked" for s in seats])
    seat_choice = int(input("Select seat (0-4): "))
    if seat_choice >= 0 and seat_choice < len(seats):
        if not seats[seat_choice]:
            seats[seat_choice] = True
            print(f"Seat {seat_choice} booked for {movies[choice]['name']} at {movies[choice]['time']}")  # Logging
        else:
            print("Seat already booked.")  # Logging
    else:
        print("Invalid seat number.")  # Logging
else:
    print("Invalid movie choice.")  # Logging
