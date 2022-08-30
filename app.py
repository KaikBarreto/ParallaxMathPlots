import matplotlib.pyplot as plt
import numpy as np
import re

def main():
  a, b, c, expression = handle_user_input()
  
  x_values_list = np.arange(-25, 25.1, 1)

  y_values_list = handleY(x_values_list,a,b, c)

  yaxis = np.arange(-200, 600.5, .5)

  function_roots = []

  for value in x_values_list:
    if handleY(value, a, b, c) == 0:
      function_roots.append(value)

  #bg
  plt.figure(num=0,dpi=180)
  # function f(x)
  plt.plot(x_values_list, y_values_list, label=f"f(x): {expression}")
  # (+/-) areas
  plt.axvspan(xmin=function_roots[0], xmax=function_roots[1], ymin=0, ymax=2, color='#ff0000', alpha=0.15)
  plt.axvspan(xmin=function_roots[1], xmax=25, ymin=0, ymax=2, color='#00ff00', alpha=0.3)
  plt.axvspan(xmin=-25, xmax=function_roots[0], ymin=0, ymax=2, color='#00ff00', alpha=0.3)
  # x axis
  plt.plot(x_values_list, x_values_list*0, "--g", label="eixo X")
  #y axis
  plt.plot(yaxis * 0, yaxis, "--r", label="eixo Y")
  
  #root lines
  for index, root in enumerate(function_roots):
    plt.axvline(x=root, color='b', label=f'root {index + 1}: {root}')
    
  # names
  plt.title("Parallax Plots")
  plt.xlabel("X Value")
  plt.ylabel("Y Value")
  plt.legend()
  
  plt.show()

def handleY(x, a: int, b: int, c: int):
  return a*x**2+b*x+c


def handle_user_input():
  # expression = "1x²-2x-15"
  
  expression = input("What's the expression? [ex.: x²-2x-15] ")
  
  function_regex = "^([0-9]{1,2})?x²([+|-])([0-9])x([+|-])([0-9]{1,3})$"
  if matches := re.search(function_regex, expression):
    
    if matches.group(1) == None:
      a = 1
    else:
      a = int(matches.group(1))
      
    b = int(f"{matches.group(2)}{matches.group(3)}")
    c = int(f"{matches.group(4)}{matches.group(5)}")
    
    print(f"a: {a} ; b: {b} ; c: {c}")
    
    return [a, b, c, expression]
    
    
if __name__ == "__main__":
  main()