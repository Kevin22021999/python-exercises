home = "FRANCE"
away = "ITALY"

print("First team:", home)
print("Second team:", away)
print("First leg")
print(home, "against", away)
print(home[0],home[1],home[2], ":", away[0],away[1],away[2])



"""
home_temp = home
home = away
away = home_temp
"""
home, away = away, home


print("First team:", home)
print("Second team:", away)
print("Return leg:")
print(home, "against", away)
print(home[0],home[1],home[2], ":", away[0],away[1],away[2])
