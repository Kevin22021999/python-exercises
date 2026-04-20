home = "France"
# We define a variable "home" and assign it the string value "France".
guest = "Switzerland"
# We define another variable "guest" and assign it the string value "Switzerland".
print(f"First leg:\n{home} vs {guest}")
# Prints the string "First leg:" followed by a newline, and then the values of the variables "home" and "guest" formatted as a match (e.g., "France vs Switzerland"). The curly brackets {} are used to indicate the variables to be printed.
print(home[0],home[1],home[2], ":" , guest[0], guest[1], guest[2])

# Swap the values of the two variables.
home, guest = guest, home
print(f"First leg:\n{home} vs {guest}")
# Prints the string "Return Leg:" followed by a newline (\n), and then the vales of the variables "guest" and"home".
print(home[0],home[1],home[2], ":" , guest[0], guest[1], guest[2])
