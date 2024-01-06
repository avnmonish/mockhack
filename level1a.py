'''
Problem statement
Steve has worked as Chef in many star hotels in multiple continents. Steve aspires 
to set up a chain of restaurants in his hometown Coimbatore. Steve figures starting 
with a cloud kitchen might be the first logical step. Steve after talking to his friends 
has identified three areas as potential places to start his business - RS Puram, 
Saibaba Colony and Peelamedu. Steve has hired a consultant to help narrow down 
to location and also type of food / restaurant business to start. Steve is very excited 
to start a Pastry based Restaurant.

Level 1a
Steve after walking thru the location is confident about prospects of pastry 
business in Saibaba colony and has finalized the location of Pastry cloud kitchen. 
Steve is very risk averse so Steve advertised pre-order for Pastry to be delivered 
as evening snack. Steve has hired one delivery person and has a scooter with a 
modified carrier. Based on the day's orders he wants to communicate the delivery 
slots to his customers. Since the scooter carrier has finite capacity and customers 
may order cupcakes, birthday cake, bread etc We are tasked with writing a 
program that will allow Steve to enter all orders for the day and we create different 
slots. We want to make sure we can fill the scooter carrier to max possible capacity 
and also conserve petrol by making each drop slot cover a minimum distance. 
Goal is reduce number trips and total distance traveled
'''

import json

# Reading
with open('level1a.json', 'r') as file :
    code = json.load(file)  # Gives a dict.

# Neighbourhood Distances :
r0 = code['restaurants']['r0']['neighbourhood_distance']

n0 = code['neighbourhoods']['n0']['distances']
n1 = code['neighbourhoods']['n1']['distances']
n2 = code['neighbourhoods']['n2']['distances']
n3 = code['neighbourhoods']['n3']['distances']
n4 = code['neighbourhoods']['n4']['distances']

n5 = code['neighbourhoods']['n5']['distances']
n6 = code['neighbourhoods']['n6']['distances']
n7 = code['neighbourhoods']['n7']['distances']
n8 = code['neighbourhoods']['n8']['distances']
n9 = code['neighbourhoods']['n9']['distances']

n10 = code['neighbourhoods']['n10']['distances']
n11 = code['neighbourhoods']['n11']['distances']
n12 = code['neighbourhoods']['n12']['distances']
n13 = code['neighbourhoods']['n13']['distances']
n14 = code['neighbourhoods']['n14']['distances']

n15 = code['neighbourhoods']['n15']['distances']
n16 = code['neighbourhoods']['n16']['distances']
n17 = code['neighbourhoods']['n17']['distances']
n18 = code['neighbourhoods']['n18']['distances']
n19 = code['neighbourhoods']['n19']['distances']

# Distance matrix :
dist = [n0, n1, n2, n3, n4,
        n5, n6, n7, n8, n9,
        n10, n11, n12, n13, n14,
        n15, n16, n17, n18, n19]

# Capacity of scooter.
cap = code['vehicles']['v0']['capacity']

q0 = code['neighbourhoods']['n0']['order_quantity']
q1 = code['neighbourhoods']['n1']['order_quantity']
q2 = code['neighbourhoods']['n2']['order_quantity']
q3 = code['neighbourhoods']['n3']['order_quantity']
q4 = code['neighbourhoods']['n4']['order_quantity']

q5 = code['neighbourhoods']['n5']['order_quantity']
q6 = code['neighbourhoods']['n6']['order_quantity']
q7 = code['neighbourhoods']['n7']['order_quantity']
q8 = code['neighbourhoods']['n8']['order_quantity']
q9 = code['neighbourhoods']['n9']['order_quantity']

q10 = code['neighbourhoods']['n10']['order_quantity']
q11 = code['neighbourhoods']['n11']['order_quantity']
q12 = code['neighbourhoods']['n12']['order_quantity']
q13 = code['neighbourhoods']['n13']['order_quantity']
q14 = code['neighbourhoods']['n14']['order_quantity']

q15 = code['neighbourhoods']['n15']['order_quantity']
q16 = code['neighbourhoods']['n16']['order_quantity']
q17 = code['neighbourhoods']['n17']['order_quantity']
q18 = code['neighbourhoods']['n18']['order_quantity']
q19 = code['neighbourhoods']['n19']['order_quantity']

print(q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19)
