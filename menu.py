import random


def get_foods_list():
  foods = "치킨,피자,햄버거,김밥,라면,돈까스,덮밥,떡볶이,카레,밀면,칼국수,수제비,우동,국밥,김치전,파전,자장면,초밥,김치찌개,된장찌개,소불고기".split(',')
  foods_list = random.sample(foods, k=len(foods))
  return foods_list
