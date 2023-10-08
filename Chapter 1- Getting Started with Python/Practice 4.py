def get_area(a, b, c):
   s = (a+b+c)/2
   return (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(get_area(30, 35, 30))