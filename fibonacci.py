def f(n):
    a=1;
    b=1;
    for i in range(1, n):
        b=a+b
        a=b-a
    return b;

print(f(15))