# -*- coding: utf-8 -*-
"""DRAFTCODE

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hbFBtVrVD_ygdwCutCiQZJc5p5YDORbo
"""



import streamlit as st


st.title("This is the Total Cost of Ownership for a 2005 Columbia Freightliner\n")
print("Industrial Service Solutions ")

#Operational Costs
#while True:
#  try:
driver_wages = st.number_input("Please enter your driver wages per hour: ", value = 24)
#    if driver_wages > 0:
#      break
 #   else:
#      print("Invalid input. Please enter a wage that is greater than 0.")
#  except ValueError:
#    print("Invalid input. Please enter a valid number. ")

#Purchase Costs
#while True:
#  try:
initial_purchase_cost = st.number_input("Please enter the initial purchase cost of the vehicle: ", value = 60000)
 #   if initial_purchase_cost > 0:
 #     break
 #   else:
  #    print("Invalid input. Please enter an initial purchase cost that is greater than 0.")
#  except ValueError:
#    print("Invalid input. Please enter a valid number. ")
#while True:
#  try:
useful_life = st.number_input("Please enter the number of years the vehicle has been in use: ", value = 20)
#    if useful_life > 0:
#      break
#    else:
#      print("Invalid input. Please enter the correct number of years greater than 0.")
#  except ValueError:
#    print("Invalid input. Please enter a valid number. ")
#Fuel Costs:
#while True:
#  try:
average_monthly_driven_miles = st.number_input("Please enter the number of miles that this vehicle drives per month: ", value = 2625)
#    if average_monthly_driven_miles > 0:
#      break
#    else:
#      print("Invalid input. Please enter the correct number of miles greater than 0.")
#  except ValueError:
#    print("Invalid input. Please enter a valid number. ")
# while True:
#  try:
fuel_efficiency = st.number_input("Please enter the fuel efficiency of this vehicle in miles per gallon: ", value = 8.8)
#    if fuel_efficiency > 0:
#      break
#    else:
#      print("Invalid input. Please enter the correct fuel efficiency greater than 0.")
#  except ValueError:
#    print("Invalid input. Please enter a valid number. ")
#while True:
#  try:
fuel_price = st.number_input("Please enter the fuel price per gallon at this current moment: ", value 3.52)
#    if fuel_price > 0:
#      break
#    else:
#      print("Invalid input. Please enter the correct fuel price greater than 0.")
#  except:
#    print("Invalid input. Please enter a valid number. ")

#Maintenance Costs
#while True:
 # try:
monthly_maintenance_cost = st.number_input("Please enter the monthly maintenance cost of this vehicle: ", value = 1000)
#    if monthly_maintenance_cost > 0:
 #     break
#    else:
 #     print("Invalid input. Please enter the correct maintenance cost greater than 0.")
#  except ValueError:
#    print("Invalid input. Please enter a valid number. ")

#Licensing Permits
#while True:
#  try:
registration_fee = st.number_input("Please enter the monthly registration fee for this vehicle: ", value = 91.67)
 #   if registration_fee > 0:
 #     break
#    else:
#      print("Invalid input. Please enter the correct registration fee greater than 0.")
#  except ValueError:
#    print("Invalid input. Please enter a valid number. ")

#while True:
#  try:
permit_costs = st.number_input("Please enter the monthly permit costs for this vehicle: ", value = 80)
#    if permit_costs > 0:
#      break
#    else:
#      print("Invalid input. Please enter the correct permit costs greater than 0.")
#  except ValueError:
#    print("Invalid input. Please enter a valid number. ")

#Calculations
try:
    purchase_cost_per_month = initial_purchase_cost / (useful_life * 12)
    fuel_cost_per_month = (average_monthly_driven_miles / fuel_efficiency) * fuel_price
    total_driver_wages_per_month = driver_wages * 4.33 * 50
#purchase_cost_per_month = initial_purchase_cost / (useful_life * 12)
#fuel_cost_per_month = (average_monthly_driven_miles / fuel_efficiency) * fuel_price
    total_maintenance_cost_per_month = monthly_maintenance_cost
    total_licensing_permits_cost_per_month = registration_fee + permit_costs

    total_cost_of_owning_vehicle_per_month = total_driver_wages_per_month + purchase_cost_per_month + fuel_cost_per_month + total_maintenance_cost_per_month + total_licensing_permits_cost_per_month
except ZeroDivisionError:
  
    st.error("An error occurred: Division by zero is not allowed.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

#total_driver_wages_per_month = driver_wages * 4.33 * 50
#purchase_cost_per_month = initial_purchase_cost / (useful_life * 12)
#fuel_cost_per_month = (average_monthly_driven_miles / fuel_efficiency) * fuel_price
#total_maintenance_cost_per_month = monthly_maintenance_cost
#total_licensing_permits_cost_per_month = registration_fee + permit_costs

#total_cost_of_owning_vehicle_per_month = total_driver_wages_per_month + purchase_cost_per_month + fuel_cost_per_month + total_maintenance_cost_per_month + total_licensing_permits_cost_per_month

st.write(f"The total driver wage costs per month is: ${total_driver_wages_per_month:.2f}\n")
st.write(f"The total purchase cost per month is: ${purchase_cost_per_month:.2f}\n")
st.write(f"The total fuel cost per month is: ${fuel_cost_per_month:.2f}\n")
st.write(f"The total maintenance cost per month is: ${total_maintenance_cost_per_month:.2f}\n")
st.write(f"The total licensing and permits cost per month is: ${total_licensing_permits_cost_per_month:.2f}\n")

st.write(f"The total cost of owning the vehicle per month is: ${total_cost_of_owning_vehicle_per_month:.2f}\n")

dollar_per_mile_calculation = (total_driver_wages_per_month/average_monthly_driven_miles) + (purchase_cost_per_month/average_monthly_driven_miles) + (fuel_cost_per_month/average_monthly_driven_miles) + (total_maintenance_cost_per_month/average_monthly_driven_miles) + (total_licensing_permits_cost_per_month/average_monthly_driven_miles)

st.write(f"The dollar per mile calculation is: ${dollar_per_mile_calculation:.2f}\n")

#3rd party delivery costs

#while True:
#  try:
third_party_delivery_costs = st.number_input("Please enter the dollar per mile cost of a 3rd party delivery method: ")
#    if third_party_delivery_costs > 0:
 #     break
#    else:
  #    print("Invalid input. Please enter a value greater than 0.")
 # except ValueError:
#    print("Invalid input. Please enter a valid number. ")
#
#import ipywidgets as widgets
#from IPython.display import display

# Define the slider
#impact_slider = widgets.IntSlider(
#    value=1,
#    min=0,
#    max=2,
#    step=1,
#    description='Impact:',
#    style={'description_width': 'initial'}
#)

# Define the label
#impact_label = widgets.Label()

# Update function
#def update_label(change):
#   levels = {
 #       0: "No Impact",
  #      1: "Medium Impact",
#       2: "High Impact"
 #   }
#    impact_label.value = f"Qualitative Impact: {levels[impact_slider.value]} ({impact_slider.value})"

# Connect the slider to the update function
#impact_slider.observe(update_label, names='value')

# Initial label update
#update_label(None)

# Display the slider and label
#display(impact_slider, impact_label)

#import ipywidgets as widgets
#from IPython.display import display

st.write("Please select whether to consider the qualitative results in the analysis\n")
st.write("0 means that qualitative data will not be considered when making the decision\n")
st.write("1 means that qualitative data and quantitative data are equally considered when recommending the decision\n")
st.write("2 means that only qualitative data is considered when making the decision\n")

# Define the slider
#impact_slider = widgets.IntSlider(
  #  value=1,
 #   min=0,
#    max=2,
 #   step=1,
 #   description='Impact:',
 #  style={'description_width': 'initial'}
#)

# Define the label to show the result
#impact_label = widgets.Label()

# Button to confirm or update the selection
#update_button = widgets.Button(description="Update Selection")

# Store the last value (initially none)
#last_value = None

# Function that calculates costs based on slider value
#def calculate_costs(value):
#    if value == 0:
 #       return "No impact on costs."
#    elif value == 1:
#        return "Medium impact on costs."
#    elif value == 2:
#        return "High impact on costs."

# Function to handle button click and show result
#def on_button_click(b):
#    global last_value
 #   if last_value != impact_slider.value:
#        last_value = impact_slider.value  # Update the last confirmed value
   #     result = calculate_costs(last_value)
   #     impact_label.value = f"Qualitative Impact: {result}"
  #  else:
 #       impact_label.value = f"Qualitative Impact: No change made."
#
# Attach the button click function to the button
#update_button.on_click(on_button_click)

# Display the slider, update button, and result label
#display(impact_slider, update_button, impact_label)







