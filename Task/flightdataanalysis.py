# Flight data analysis
# Given a tuple of flights (flight_number, origin, destination, duration_in_minutes
# flights = (
#    ("AA123","NYC", "LA" , 300),
#    ("DL456","ATL","MIA", 150),
#    ("UA789","ORD","DFW", 180),
#    ("SW101","SFO","SEA", 120),
#    ("BA202","LON","PAR", 90)
#)

#print all flights originating from NYC
#sort flights by duration (shortest to longest) and print the sorted list
#find the flight with the longest duration and print its details

flights = (
   ("AA123","NYC", "LA" , 300),
   ("DL456","ATL","MIA", 150),
   ("UA789","ORD","DFW", 180),
   ("SW101","SFO","SEA", 120),
   ("BA202","LON","PAR", 90)
)
 
# Print all flights originating from NYC
print("Flights originating from NYC:")
for flight in flights:
    if flight[1] == "NYC":
        print(flight)
    

# Sort flights by duration (shortest to longest) and print the sorted list
sorted_flights = sorted(flights, key=lambda x: x[3])
print("\nFlights sorted by duration (shortest to longest):")
for flight in sorted_flights:
    print(flight)
    
 # Find the flight with the longest duration and print its details
longest_flight = max(flights, key=lambda x: x[3])
print("\nFlight with the longest duration:")
print(longest_flight)
   