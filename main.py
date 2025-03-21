import numpy as np


def result(M):  #print matrix result
  for i in M:
    for j in i:
      print(j, end=" ")
    print()


def matrix(i, j, name, x):  #function create matrix A
  elements = []
  for s in range(i):
    strings = []
    for c in range(j):
      while True:
        try:  #checking elements A
          jx = int(
            input('Введіть елемент ' + x + str(s + 1) + str(c + 1) + ': '))
          if type(jx) == int:
            if -100 < jx < 100:
              break
            else:
              print(
                'Це число надто об\'ємне для елемента. Введіть двохрозрядне число!'
              )
              continue
        except:
          print('Виникла помилка! Введіть ціле число!')
          continue
      strings.append(jx)
    elements.append(strings)
  M = np.array(elements)
  print('Матриця ' + name + ':')
  for i in M:
    for j in i:
      print(j, end=" ")
    print()
  return M


def diagonal_matrix(i, j):  #create a diagonaling matrix
  elements = []
  for s in range(i):
    strings = []
    for c in range(j):
      if s - c == 0:
        jx = int(a)
      else:
        jx = int(0)
      strings.append(jx)
    elements.append(strings)
  diagonal = np.array(elements)
  return diagonal


def size(text_x):  #input size of matrix
  while True:
    try:  #checking size is int from 0 to 5
      x = int(input('Введіть кількість ' + text_x))
      if type(x) == int:
        if 5 > x > 0:
          break
        else:
          print('Число має бути менше 5 і більше 0!')
          continue
    except:
      print('Виникла помилка! Вводьте цілі числа!')
      continue
  return x


def oper(set_op):  #input operation from list of avaible operetions
  while True:
    operation = str(input('\nВведіть бажану дію зі списку: '))
    if {operation} <= set_op:  #checking operation is correct and avaible
      break
    else:
      print('Введіть дію зі списку вище!')
  return operation


#dicts of avaible operations
avaible_operat_A = {
  'Т': 'транспонування матриці',
  '*': 'множення матриці на деяке число',
  '+': 'додавання матриці до числа',
  '-': 'віднімання числа від матриці',
  '**2': 'піднесення матриці до квадрату',
}
avaible_operat_AB = {
  '*': 'множення матриці А на матрицю В',
  '+': 'сума матриць А і В',
  '-': 'відніманя матриці В від матриці А',
}

#cover of full programm
print('~' * 10 + ' ПРОГРАМА - МАТРИЧНИЙ КАЛЬКУЛЯТОР ' + '~' * 10)
answer = input(
  'Щоб почати роботу - натисніть ENTER,\nДля перегляду інструкції натисніть 1: '
)
#instruction
if answer == '1':
  print('-' * 13 + 'Можливі дії з матрицею А' + '-' * 13)
  for key, value in avaible_operat_A.items():
    print(key, ' : ', value)
  print('-' * 10 + 'Можливі дії з матрицями А та В' + '-' * 11)
  for key, value in avaible_operat_AB.items():
    print(key, ' : ', value)
  print('-' * 40 + '\n! Максимальна розмірність матриці 5х5\
\n! Не рекомендуєься використовувати числа з більше, ніж 2-ома розрядами\
\n! Всі введені числа мають бути цілими\
\n! Дії потрібно вводити так, як зазначено в списку операцій\n' + '-' * 40)
  answer = input('Щоб почати роботу - натисніть ENTER,\n')
else:
  print()

#start of the programm
while True:
  #creating a matrix А
  print('~' * 10 + ' Введення матриці A ' + '~' * 10)
  i1 = size('рядків: ')
  j1 = size('стовбців: ')
  A = matrix(i1, j1, 'A', 'a')
  while True:
    #question about matrix B
    another_matrix = str(
      input(
        'Для операції між матрицею та числом - натисніть ENTER\nДля дії між двома матрицями - натисніть 1: '
      ))
    if another_matrix == '1':  #Matrix A and B
      #creating a matrix B
      print('~' * 10 + ' Введення матриці В ' + '~' * 10)
      i2 = size('рядків: ')
      j2 = size('стовбців: ')
      B = matrix(i2, j2, 'B', 'b')
      AB_operations = set({})  #analysis of operations
      if j1 == i2:
        AB_operations.add('*')
      if i1 == i2 and j1 == j2:
        AB_operations.add('+')
        AB_operations.add('-')
      if AB_operations == set({}):  #if all operations is not avaible
        print(
          'Матриця В не узгоджена до матриці А. Виконати дії +, -, * неможливо!'
        )
        another_matrix = '0'
        continue
      else:  #print a list of operations
        print('Ви можете виконати такі дії з матрицями А та В:', end=' ')
        for a in AB_operations:
          print(a, end=' ')
        operationAB = oper(AB_operations)

    else:  #Only matrix A
      A_operations = {'T', 'Т', '*'}  #analysis of operations
      if i1 == j1:
        A_operations.add('+')
        A_operations.add('-')
        A_operations.add('**2')
      print('Для матриці А можете виконати такі дії:',
            end=' ')  #print a list of operations
      for a in A_operations:
        if a == 'Т':
          pass
        else:
          print(a, end=' ')
      operationA = oper(A_operations)

    #input a result
    if another_matrix == '1':
      if operationAB == '+':
        result(A + B)
      elif operationAB == '-':
        result(A - B)
      elif operationAB == '*':
        result(np.dot(A, B))
    else:
      if operationA == 'T' or operationA == 'Т':
        result(A.transpose())
      if operationA == '*' or operationA == '+' or operationA == '-':
        while True:
          try:  #checking number is int
            a = int(input('Введіть ціле число для виразу: '))
            if type(a) == int:
              break
          except:
            print('Виникла помилка! Введіть ціле число!')
            continue

        if operationA == '*':
          result(A * a)
        else:
          a_matrix = diagonal_matrix(i1, j1)
          if operationA == '+':
            result(A + a_matrix)
          elif operationA == '-':
            result(A - a_matrix)
      if operationA == '**2':
        result(np.dot(A, A))

    answer = str(
      input(
        'Якщо бажаєте продовжити роботу з введеною матрицею А, натисніть ENTER, ні - будь-який символ. '
      ))
    if answer == '':
      print('Матриця А:')
      result(A)
    else:
      break

  answer = str(
    input('Ввести нову матрицю? Так - ENTER, ні - будь-який символ.'))
  if answer == '':
    continue
  else:
    break

print('~' * 10 + 'Роботу програми успішно завершено!' + '~' * 10)
