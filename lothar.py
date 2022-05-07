''' write a program that receives a user number and repeat following process using 'while'
- if number is pair, then divide for 2
- if number is odd, then multiply for 3 and add for 1
Repeat this process until reach number 1, then show in screen the amount of steps it took to arrive
'''

def lothar(n):
    contador = 0
    while (n != 1): 
        if(n%2 == 0): 
            n=n/2 
            contador = contador+1 
        else: 
            n = n*3+1 
            contador = contador+1 
    return contador

n = int(input())
print(lothar(n))


