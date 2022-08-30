import matplotlib.pyplot as plt
import numpy as np
import re

def f(x, a, b, c):
  return a*x**2+b*x+c

def main():
  xlist = np.arange(-25, 25.1, 1)

  ylist = f(xlist,1,-2, -15)

  yaxis = np.arange(-200, 600.5, .5)

  roots = []

  for value in xlist:
    if f(value, 1, -2, -15) == 0:
      roots.append(value)

  #bg
  plt.figure(num=0,dpi=180)
  # function f(x)
  plt.plot(xlist, ylist, label="f(x): x²+2x-15")
  # (+/-) areas
  plt.axvspan(xmin=-3, xmax=5, ymin=0, ymax=2, color='#ff0000', alpha=0.15)
  plt.axvspan(xmin=5, xmax=25, ymin=0, ymax=2, color='#00ff00', alpha=0.3)
  plt.axvspan(xmin=-25, xmax=-3, ymin=0, ymax=2, color='#00ff00', alpha=0.3)
  # x axis
  plt.plot(xlist, xlist*0, "--g", label="eixo X")
  #y axis
  plt.plot(yaxis * 0, yaxis, "--r", label="eixo Y")
  
  #root lines
  for index, root in enumerate(roots):
    plt.axvline(x=root, color='b', label=f'root {index + 1}: {root}')
    
  # names
  plt.title("Parallax Plots")
  plt.xlabel("X Value")
  plt.ylabel("Y Value")
  plt.legend()
  
  plt.show()
  
if __name__ == "__main__":
  main()