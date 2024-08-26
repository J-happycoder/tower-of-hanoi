import math

T3 = {0: 1, 1: 1, 2: 3}
T4 = {0: 1, 1: 1, 2: 3}
T5 = {0: 1, 1: 1, 2: 3}
T6 = {0: 1, 1: 1, 2: 3}
T7 = {0: 1, 1: 1, 2: 3}
T8 = {0: 1, 1: 1, 2: 3}
T9 = {0: 1, 1: 1, 2: 3}
T10 = {0: 1, 1: 1, 2: 3}
T11 = {0: 1, 1: 1, 2: 3}
T12 = {0: 1, 1: 1, 2: 3}
T13 = {0: 1, 1: 1, 2: 3}
T14 = {0: 1, 1: 1, 2: 3}
T15 = {0: 1, 1: 1, 2: 3}
T16 = {0: 1, 1: 1, 2: 3}
T17 = {0: 1, 1: 1, 2: 3}
T18 = {0: 1, 1: 1, 2: 3}
T19 = {0: 1, 1: 1, 2: 3}


def minimumValue(X, f):
  min = f(X[0])

  for x in X:
    if (f(x) < min):
      min = f(x)

  minX = []
  for x in X:
    if (f(x) == min):
      minX.append(x)

  return {"min": min, "minX": minX}


for n in range(3, 3000):
  T3[n] = 2 * T3[n - 1] + 1
  T4[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T4[k] + T3[n - k])["min"]
  T5[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T5[k] + T4[n - k])["min"]
  T6[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T6[k] + T5[n - k])["min"]
  T7[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T7[k] + T6[n - k])["min"]
  T8[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T8[k] + T7[n - k])["min"]
  T9[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T9[k] + T8[n - k])["min"]
  T10[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T10[k] + T9[n - k])["min"]
  T11[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T11[k] + T10[n - k])["min"]
  T12[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T12[k] + T11[n - k])["min"]
  T13[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T13[k] + T12[n - k])["min"]
  T14[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T14[k] + T13[n - k])["min"]
  T15[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T15[k] + T14[n - k])["min"]
  T16[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T16[k] + T15[n - k])["min"]
  T17[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T17[k] + T16[n - k])["min"]
  T18[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T18[k] + T17[n - k])["min"]
  T19[n] = minimumValue(X=list(range(1, n)), f=lambda k: 2 * T19[k] + T18[n - k])["min"]

for i in T19.keys():
  if math.sqrt(T19[i]) == int(math.sqrt(T19[i])):
    print(i)
