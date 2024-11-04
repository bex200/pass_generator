# Task 1
print("Task one results")
x=1
for i in range(x, 101):
    if i%3==0 or i%5==0 or i%7==0 or i%9==0:
        print(i, end=" ")

print("\n End of Task 1")

# # Task 2
print('\n Task 2 results')
name = "Congratulations"
l = len(name)

for k in range(l):
    if k%2==0:
        print(name[k], end="")

print("\n End of Task 2")

# Task 3
print("\nTask 3 results")
i = 1
b = []
while i <= 1000:  
    if i % 15 == 0 or i % 17 == 0 or i % 25 == 0:
        i += 1
        continue  
    b.append(i)
    i += 1
print(b, "\nSum of the numbers is " + str(sum(b)))

    

        
    
    
    
    
