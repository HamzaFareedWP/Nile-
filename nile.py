from math import sqrt

SHIPPING_PRICES = {'Ground': 1.5, 'Express': 2.5, 'Overnight': 4.0}

def get_distance(from_lat, from_long, to_lat, to_long):
  return sqrt((to_lat - from_lat) ** 2 + (to_long - from_long) ** 2)

def format_price(price):
  return '${:,.2f}'.format(price)
