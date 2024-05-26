import math
import pandas as pd

def aproximacion_stirling(n):
  return math.pow(n, n) * math.pow(math.e, -n) * math.sqrt(2 * math.pi * n)

def error_absoluto(real, aprox):
  return abs(real - aprox)

def error_relativo(error_absoluto, real):
  try:
    return abs(error_absoluto) / abs(real)
  except ZeroDivisionError:
    return None

def calculate_stirling(n):
  nf = 0
  data = []
  for x in range(n+1):
    if x == 0 or x == 1:
      nf = x
    nf *= x
    aprox = aproximacion_stirling(x)
    error_abs = error_absoluto(nf, aprox)
    error_rel = error_relativo(error_abs, nf)
    row = {'n': x, 'n!': nf, 'Aproximación de Stirling': aprox, 'Error Absoluto': error_abs, 'Error Relativo': error_rel}
    data.append(row)
  df = pd.DataFrame(data)
  return df

if __name__ == "__main__":
  df = calculate_stirling(25)
  print(df)
