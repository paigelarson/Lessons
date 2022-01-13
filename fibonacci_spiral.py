# Python program for Plotting Fibonacci 
# spiral fractal using Turtle 
import turtle 
import math 
  
def fibonacciPlot(n): 
  #starting numbers
    a = 0
    b = 1
    square_a = a 
    square_b = b 

    t.pencolor("blue") 
  
    # Drawing the first square 
    t.forward(b * factor) 
    t.left(90) 
    t.forward(b * factor) 
    t.left(90) 
    t.forward(b * factor) 
    t.left(90) 
    t.forward(b * factor) 
  
    #number switch
    temp = square_b 
    square_b = square_b + square_a 
    square_a = temp 
      
    # Drawing the rest of the squares 
    for i in range(1, n): 
        t.backward(square_a * factor) 
        t.right(90) 
        t.forward(square_b * factor) 
        t.left(90) 
        t.forward(square_b * factor) 
        t.left(90) 
        t.forward(square_b * factor) 
  
        #rest of the number switches
        temp = square_b 
        square_b = square_b + square_a 
        square_a = temp 
  
    #bring pen back to begin spiral
    t.penup() 
    t.seth(0 )
    t.setposition(factor,0) #1 
    t.pendown() 
    t.pencolor("red") 
  
    # Fibonacci Spiral Plot 
    t.left(90) 
    for i in range(n): 
        print(b) 
        fdwd = math.pi * b *factor    / 2
        fdwd /= 90
        for j in range(90): 
            t.forward(fdwd) 
            t.left(1) 
        temp = a 
        a = b 
        b = temp + b 
  
  

factor = 5
  
n = int(input('Enter the number of iterations (must be > 1): ')) 

#actual process
if n > 0: 
    print("Fibonacci series for", n, "elements :") 
    t = turtle.Turtle() 
    t.speed(0) 
    fibonacciPlot(n) 
    turtle.done()  
