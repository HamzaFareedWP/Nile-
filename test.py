class Obj:
  def __init__(self, **kw):
    self.__dict__.update(kw)

def test_function(func):
  name = func.__name__
  try:
    if name == 'calculate_shipping_cost':
      assert func((0, 0), (3, 4), 'Ground') == '$7.50'
      assert func((0, 0), (3, 4)) == '$20.00'
    elif name == 'calculate_driver_cost':
      a = Obj(speed=50, salary=20)
      b = Obj(speed=100, salary=30)
      price, driver = func(100, a, b)
      assert price == 30 and driver is b
    elif name == 'calculate_money_made':
      d = Obj(cost=60)
      t = Obj(cost=100, driver=d)
      assert func(t1=t, t2=t) == 80
    print('OK! {}() passes tests'.format(name))
  except Exception as e:
    print('FAIL! {}(): {!r}'.format(name, e))
