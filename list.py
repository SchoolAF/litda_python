#
# Aliffathur Muhammad Revan (714220066)
# 1B Teknik Informatika
# me@herobuxx.me
#

# Create a new variable as a list
new_list = ["python", "True", 100, [1, 2, 3], 9.5];

# Problem No 1
#
# Add a list as new_list and show the output
# Print the list out on terminal
#
print("Problem No.1");
print(new_list);

# Problem No 2
#
# We wanted to show dats from element number 2
# Print the list out on terminal
#
print("Problem No.2");
print(new_list[2]);

# Problem No 3
# 
# We wanted teh avlue of the element 1, 2, and 3
# So, here we show the data between 0-3 which contains 1, 2, and 3
# Print the list out on terminal
#
print("Problem No.3");
print(new_list[0:3]);

# Problem No 4
# 
# Combine a and b list. Here we use exnted function to do it.
# Print the list out on terminal
#

a = [1, 2, 'hai'];
b = ['hello', 200]

a.extend(b);

print(a);

# Problem No 4
# 
# Combine a and b list. Here we use exnted function to do it.
# Print the list out on terminal
#

del new_list[-1];
print(new_list);