import pizza

pizza.make_pizza('pepperoni')
pizza.make_pizza('mushrooms', 'green peppers', 'extra cheese')

# --- IMPORTING ----
# (1) import pizza - imports ALL functions
# (2) from pizza import make_pizza - imports this specific function
# (3) from pizza import make_pizza as mp - gives alias to function
# (4) import pizza as p - gives module an alias

# -- CALLING ---
# (1) pizza.make_pizza('xxx')
# (2) make_pizza ('xxx')
# (3) mp('xxx')
# (4) p.make_pizza('xxx')