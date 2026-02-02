# Create and Access Tuple
tuple1 = (10, 20, 30, 40)
print("Tuple:", tuple1)
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])

# Nested Tuple
print("2. Nested Tuple")
nested_tuple = (1, 2, (3, 4, 5), 6)
print("Nested Tuple:", nested_tuple)
print("Access nested element:",
nested_tuple[2][1])

# Repetition of Tuple
print("3. Repetition of Tuple")
tuple2 = (7, 8)
repeated_tuple = tuple2 * 3
print("Original Tuple:", tuple2)
print("Repeated Tuple:", repeated_tuple)

# Concatenation of Tuples
print("4. Concatenation of Tuples")
tuple3 = (100, 200)
tuple4 = (300, 400)
concatenated_tuple = tuple3 + tuple4
print("First Tuple:", tuple3)
print("Second Tuple:", tuple4)
print("Concatenated Tuple:", concatenated_tuple)