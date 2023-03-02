#
# Aliffathur Muhammad Revan (714220066)
# 1B Teknik Informatika
# me@herobuxx.me
#

# Problem No 1
#
# Add a dict as ad movie
# Print the list out on terminal
#

print("Problem No.1");
# Create a new variable as a movie dictionary
movies = {
    'Home Alone': 1990,
    'The Terminator': 1984,
    'Titanic': 1997,
    'Jurassic Park': 1993,
    'The Lord of the Rings': 2001,
    'Avatar': 2009
};

# Problem No 2
#
# Show values of Titanic
# Print the list out on terminal
#

print("Problem No.2");

# Create a new variable as a movie dictionary
movies = {
    'Home Alone': 1990,
    'The Terminator': 1984,
    'Titanic': 1997,
    'Jurassic Park': 1993,
    'The Lord of the Rings': 2001,
    'Avatar': 2009
};
titanic_value = movies['Titanic'];
print("Value:",titanic_value);

# Problem No 3
#
# Show all keys
# Print the list out on terminal
#

print("Problem No.3");
# Create a new variable as a movie dictionary
movies = {
    'Home Alone': 1990,
    'The Terminator': 1984,
    'Titanic': 1997,
    'Jurassic Park': 1993,
    'The Lord of the Rings': 2001,
    'Avatar': 2009
};
movies_keys = movies.keys();
print(movies_keys);

# Problem No 4
#
# Add Harry Potter to the Dictionary
# Print the list out on terminal
#

print("Problem No.4");
# Create a new variable as a movie dictionary
movies = {
    'Home Alone': 1990,
    'The Terminator': 1984,
    'Titanic': 1997,
    'Jurassic Park': 1993,
    'The Lord of the Rings': 2001,
    'Avatar': 2009
};

movies["Harry Potter"] = "2001";
print(movies);

# Problem No 1
#
# Remove The Ternminator from the dictionary
# Print the list out on terminal
#

print("Problem No.1");
# Create a new variable as a movie dictionary
movies = {
    'Home Alone': 1990,
    'The Terminator': 1984,
    'Titanic': 1997,
    'Jurassic Park': 1993,
    'The Lord of the Rings': 2001,
    'Avatar': 2009
};

del movies['The Terminator']
print(movies);