import pandas as pd
import numpy as np

#takes advent fuel data and calculates fuel used and fuel used by extra weight of fuel
df = pd.read_csv('advent_day1.csv',header=None)
df['fuel'] = (df[0]//3)-2
fuel = list(df.fuel)
add_fuel = []
for t in fuel:

    fuel_to_add = t
    # stores total fuel needed due to extra weight of fuel
    total_extra = 0

    while fuel_to_add > 0:
        fuel_to_add = fuel_to_add//3-2

        #only adding numbers to total_extra that are above 0
        if fuel_to_add > 0:
            total_extra += fuel_to_add
        # decrementing t until 0.
        t -= fuel_to_add
    add_fuel.append(total_extra)