n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_value = 0
second_value = 1
third_value = 2

print(second_value)

output = 0

if n > 1:
    print(third_value)
    for i in range(n-2):
        output = first_value + second_value + third_value

        first_value, second_value, third_value = second_value, third_value, output

        print(output)