# -*- coding: utf-8 -*-

height = input('Height: ')
weight = input('Weight: ')

bmi = float(weight) / (float(height) * float(height))

if bmi < 18.5:
  print('你嘅bmi指数系' + str(bmi) + '，过轻')
elif bmi <= 25:
  print('你嘅bmi指数系' + str(bmi) + '，正常')
elif bmi <= 28:
  print('你嘅bmi指数系' + str(bmi) + '，过重')
elif bmi <= 32:
  print('你嘅bmi指数系' + str(bmi) + '，肥胖')
else:
  print('你嘅bmi指数系' + str(bmi) + '，严重肥胖')