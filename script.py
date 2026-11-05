from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function
 
# ERROR 1 (indentation): everything inside a function must be indented.
# Your paste showed the function bodies flush left, which causes IndentationError.
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'):
  from_lat, from_long = from_coords
  to_lat, to_long = to_coords
 
  # ERROR 2 (duplicate code): you wrote the two unpacking lines twice.
  # Harmless, but redundant, so the second copy is removed.
 
  distance = get_distance(from_lat, from_long, to_lat, to_long)
 
  # ERROR 3 (NameError): you wrote "shipping_rates" here but used "shipping_rate" below.
  # Fixed: both places now use "shipping_rate".
  shipping_rate = SHIPPING_PRICES[shipping_type]
 
  price = distance * shipping_rate
 
  return format_price(price)
 
test_function(calculate_shipping_cost)
 
def calculate_driver_cost(distance, *drivers):
  cheapest_driver = None
  cheapest_driver_price = None
 
  for driver in drivers:
    driver_time = distance / driver.speed
    price_for_driver = driver_time * driver.salary
 
    # ERROR 4 (SyntaxError): you wrote "if cheapest_driver = None" with no colon.
    # "=" assigns a value, but we want to compare, so use "is" (best for None)
    # and end the line with a colon ":".
    if cheapest_driver is None:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
 
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
 
  return cheapest_driver_price, cheapest_driver
 
# ERROR 6 (missing test): you had no test call for this function. Added it.
test_function(calculate_driver_cost)
 
def calculate_money_made(**trips):
  total_money_made = 0
 
  for trip_id, trip in trips.items():
    trip_revenue = trip.cost - trip.driver.cost
 
    # ERROR 5 (AttributeError): you wrote "trip.revenue", but a trip has no such attribute.
    # The value is stored in your variable "trip_revenue", so use that.
    total_money_made += trip_revenue
 
  return total_money_made
 
test_function(calculate_money_made) 