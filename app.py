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
      root = value
      function_roots.append(root)

  #bg
  plt.figure(num=0,dpi=180)
  # function f(x)
  plt.plot(x_values_list, y_values_list, label=f"f(x): {expression}")
  # (+/-) areas
  if len(function_roots) >= 2:
    plt.axvspan(xmin=function_roots[0], xmax=function_roots[1], ymin=0, ymax=2, color='#ff0000', alpha=0.15)
    plt.axvspan(xmin=function_roots[1], xmax=25, ymin=0, ymax=2, color='#00ff00', alpha=0.3)
    plt.axvspan(xmin=-25, xmax=function_roots[0], ymin=0, ymax=2, color='#00ff00', alpha=0.3)
  # x axis
  plt.plot(x_values_list, x_values_list*0, "--g", label="eixo X")
  #y axis
  plt.plot(yaxis * 0, yaxis, "--r", label="eixo Y")
  
  #root lines
  for index, root in enumerate(function_roots):
    # plt.axvline(x=root, ymin=0.25, ymax=0.3, color='b', label=f'root {index + 1}: {root}')
    if root:
      plt.plot([root - 0.05, root + 0.05],[-10, 10], color='b', label=f'root {index + 1}: {root}')
    
  # names
  plt.title("Parallax Plots")
  plt.xlabel("X Value")
  plt.ylabel("Y Value")
  plt.legend()
  
  plt.show()

def handleY(x, a: int, b: int, c: int):
  return a*x**2+b*x+c


def handle_user_input():
  
  expression = input("What's the expression? [ex.: x²-2x-15]: ")
  
  function_regex = "^(-)?([0-9]{1,4})?x²([+|-][0-9]{1,4})x([+|-][0-9]{1,5})$"
  if matches := re.search(function_regex, expression):
    
    if matches.group(1) and matches.group(2):
      a = int(f"{matches.group(1)}{matches.group(2)}")
    elif matches.group(1) and not matches.group(2):
      a = -1
    elif matches.group(2) and not matches.group(1):
      a = int(matches.group(2))
    elif not matches.group(1) and not matches.group(2):
      a = 1
      
    b = int(matches.group(3))
    c = int(matches.group(4))
    
    print(f"a: {a} ; b: {b} ; c: {c}")
    
    return [a, b, c, expression]
    
    
if __name__ == "__main__":
  main()