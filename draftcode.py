# -*- coding: utf-8 -*-
"""DRAFTCODE


"""

import pandas as pd
import streamlit as st



#st.title("This is the Total Cost of Ownership for a 2005 Columbia Freightliner\n")

#st.image("https://mma.prnewswire.com/media/2409166/ISS_Logo.jpg?p=facebook", width = 200)
#Operational Costs
st.markdown(
    """
    <h1 style="display: inline;">This is the Total Cost of Ownership for a 2005 Columbia Freightliner</h1>
    <img src="https://mma.prnewswire.com/media/2409166/ISS_Logo.jpg?p=facebook" width="250" style="vertical-align: middle; margin-left: 10px;">
    """,
    unsafe_allow_html=True
)


#while True:
#  try:
st.write("**Cost Inputs**")
st.write("All of these values are initialized to account for initial data given by Industrial Service Solutions. Adjust if needed")
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
fuel_price = st.number_input("Please enter the fuel price per gallon at this current moment: ", value = 3.52)
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
st.divider()
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
columns = ['Total Driver Wage Costs Per Month', 'Total Purchase Costs Per Month', 'Total Fuel Costs Per Month','Total Maintenance Costs Per Month', 'Total Licensing/Permit Costs Per Month', 'Total Costs Per Month']
costs = [total_driver_wages_per_month, purchase_cost_per_month, fuel_cost_per_month, total_maintenance_cost_per_month,total_licensing_permits_cost_per_month, total_cost_of_owning_vehicle_per_month ]
df = pd.DataFrame({'Type of Costs': columns, 'Costs': costs})
df['Costs'] = df['Costs'].apply(lambda x: f"${x:,.2f}")


def highlight_total(row):
    return ['font-weight: bold' if row['Type of Costs'] == 'Total Costs Per Month' else '' for _ in row]
styled_df = df.style.apply(highlight_total, axis = 1)    
st.write('### Monthly Cost Quantitative Breakdown')
st.dataframe(styled_df)

#st.write(f"The total driver wage costs per month is: ${total_driver_wages_per_month:.2f}\n")
#st.write(f"The total purchase cost per month is: ${purchase_cost_per_month:.2f}\n")
#st.write(f"The total fuel cost per month is: ${fuel_cost_per_month:.2f}\n")
#st.write(f"The total maintenance cost per month is: ${total_maintenance_cost_per_month:.2f}\n")
#st.write(f"The total licensing and permits cost per month is: ${total_licensing_permits_cost_per_month:.2f}\n")

#st.write(f"The total cost of owning the vehicle per month is: ${total_cost_of_owning_vehicle_per_month:.2f}\n")

dollar_per_mile_calculation = (total_driver_wages_per_month/average_monthly_driven_miles) + (purchase_cost_per_month/average_monthly_driven_miles) + (fuel_cost_per_month/average_monthly_driven_miles) + (total_maintenance_cost_per_month/average_monthly_driven_miles) + (total_licensing_permits_cost_per_month/average_monthly_driven_miles)
# Initialize toggle state
if 'show_chart' not in st.session_state:
    st.session_state.show_chart = False

# Toggle button
if st.button("Show/Hide Cost Breakdown Chart"):
    st.session_state.show_chart = not st.session_state.show_chart

# Show chart if toggled
if st.session_state.show_chart:
    df = pd.DataFrame({'Cost ($)': costs}, index=columns)
    st.bar_chart(df)
st.markdown(f"<p style='font-size: 30px;'><b>The dollar per mile calculation is: ${dollar_per_mile_calculation:.2f}</b></p>", unsafe_allow_html=True)

#3rd party delivery costs

#while True:
#  try:
third_party_delivery_costs = st.number_input("Please enter the dollar per mile cost of a 3rd party delivery method: ", value = 2.54)
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
#st.markdown("This percent premium value is the **MAXIMUM** premium when the qualitative aspects are of the greatest importance for the customer")

##PercentPremium = st.number_input("Please enter the percent premium that the company is willing to pay as a **decimal**: ", value = 0.20)
st.markdown(r"""
### Enter Maximum Percent Premium

This is the <b>highest extra amount (as a percentage)</b> your company is willing to pay for a product or service <b>when things like quality, brand, reliability, or service are most important to the customer</b>.

💡 <b>Example:</b><br>
If a product usually costs $100, and you are okay paying up to $120 because it has better quality or service, that's a <b>20% premium</b> — so you'd enter <b>0.20</b> below.
""", unsafe_allow_html=True)

PercentPremium = st.number_input("Enter the percent premium as a decimal (e.g., 0.20 for 20%)", min_value=0.0, max_value=1.0, step=0.01)


st.markdown("### Qualitative Data Consideration in Analysis")

# Main text with explanations
st.markdown("""
Please select the level of consideration for the **qualitative results** in the analysis:

- **0** means that qualitative data will **not** be considered when making the decision.
- **5** means that you are willing to pay **50%** of the percent premium.
- **10** means that you are willing to pay the full percent premium.

Make your selection based on your willingness to factor in qualitative results alongside the quantitative data.
""")

if "slider_val" not in st.session_state:
    st.session_state.slider_val = 5

# Input widget
new_val = st.slider("Select a value", min_value=0, max_value=10, value=st.session_state.slider_val, step=1)

# Button to apply the update
if st.button("Update"):
    st.session_state.slider_val = new_val

# Display the updated value
st.write("Current selected value:", st.session_state.slider_val)

st.divider()
st.markdown("### Recommendations to ISS")

#Current_Premium = (dollar_per_mile_calculation - third_party_delivery_costs)/dollar_per_mile_calculation
#st.write("Current Premium is equal to ", f"{Current_Premium * 100:.2f}%")

#Cost_Threshold = (st.session_state.slider_val/10)* PercentPremium
#st.write("Cost Threshold is equal to ", f"{Cost_Threshold * 100:.2f}%")

#Current_Premium_Value = dollar_per_mile_calculation - third_party_delivery_costs

#New = Cost_Threshold * dollar_per_mile_calculation

#if (Current_Premium <= Cost_Threshold):
 #   st.write("You should use your own vehicle because the percent premium you are paying per mile is", f"${Current_Premium_Value:.2f}\n")
 #   st.write ("which is lower than the threshold cost per mile of", f"${New:.2f}")

#else:
  #  st.write("You should use the third party delivery because the percent premium you are paying per mile is", f"${Current_Premium_Value:.2f}\n")
 #   st.write ("which is greater than the threshold cost per mile of", f"${New:.2f}")
    
Current_Premium = (dollar_per_mile_calculation - third_party_delivery_costs) / dollar_per_mile_calculation
st.write("**Current Premium is equal to**", f"{Current_Premium * 100:.2f}%")

# Cost Threshold Calculation
Cost_Threshold = (st.session_state.slider_val / 10) * PercentPremium
st.write("**Cost Threshold is equal to**", f"{Cost_Threshold * 100:.2f}%")

# Current Premium Value and New Cost
Current_Premium_Value = dollar_per_mile_calculation - third_party_delivery_costs
New = Cost_Threshold * dollar_per_mile_calculation

# Decision logic
if (Current_Premium <= Cost_Threshold):
    st.markdown(
        f"<p><strong>Recommendation:</strong> You should use your own vehicle because the premium you are paying per mile is <strong>${Current_Premium_Value:.2f}</strong>, which is lower than the threshold cost per mile of <strong>${New:.2f}</strong>.</p>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f"<p><strong>Recommendation:</strong> You should use the third-party delivery because the percent premium you are paying per mile is <strong>${Current_Premium_Value:.2f}</strong>, which is higher than the threshold cost per mile of <strong>${New:.2f}</strong>.</p>",
        unsafe_allow_html=True
    )


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







