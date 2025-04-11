def sum_even_num(start,end):
    return sum(num for num in range(start,end+1) if num%2==0)
start=1
end=10
res=sum_even_num(start,end)
print(f"Su of even nos from {start} and {end}: {res}")
