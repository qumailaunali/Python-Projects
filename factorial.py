user = int(input("ENTER NUMBER : "))
total = user
a = 1
while a<user:
    total = total * (user-a)
    a = a +1
print(total)

def factorialy(num):
    if num == 0 or num == 1:
        return 1 
    else:
        fac = num * factorialy(num-1)
        return fac
if __name__ == '__main__':
    num = int(input("ENTER NUMBER : "))
    print(factorialy(int(num)))