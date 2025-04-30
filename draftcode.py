# -*- coding: utf-8 -*-
"""DRAFTCODE


"""

import pandas as pd
import streamlit as st



st.markdown(
    """
    <h1 style="display: inline;">This is the Total Cost of Ownership for a 2005 Columbia Freightliner</h1>
    <img src="https://mma.prnewswire.com/media/2409166/ISS_Logo.jpg?p=facebook" width="250" style="vertical-align: middle; margin-left: 10px;">
    """,
    unsafe_allow_html=True
)



st.write("**Cost Inputs**")
st.write("All of these values are initialized to account for initial data given by Industrial Service Solutions. Adjust if needed")
driver_wages = st.number_input("Please enter your driver wages per hour (fully burdened, includes benefits) : ", value = 24)

initial_purchase_cost = st.number_input("Please enter the initial purchase cost of the vehicle: ", value = 60000)

useful_life = st.number_input("Please enter the number of years the vehicle has been in use: ", value = 20)

average_monthly_driven_miles = st.number_input("Please enter the number of miles the vehicle is used per month: ", value = 2625)

fuel_efficiency = st.number_input("Please enter the fuel efficiency of this vehicle in miles per gallon: ", value = 8.8)

fuel_price = st.number_input("Please enter the fuel price per gallon at this current moment: ", value = 3.52)

monthly_maintenance_cost = st.number_input("Please enter the monthly maintenance cost of this vehicle: ", value = 1000)

st.write("These are the insurance costs for the vehicle")
registration_fee = st.number_input("Please enter the monthly registration fee for this vehicle: ", value = 91.67)

permit_costs = st.number_input("Please enter the monthly permit costs for this vehicle: ", value = 80)
st.divider()

try:
    purchase_cost_per_month = initial_purchase_cost / (useful_life * 12)
    fuel_cost_per_month = (average_monthly_driven_miles / fuel_efficiency) * fuel_price
    total_driver_wages_per_month = driver_wages * 4.33 * 50

    total_maintenance_cost_per_month = monthly_maintenance_cost
    total_licensing_permits_cost_per_month = registration_fee + permit_costs

    total_cost_of_owning_vehicle_per_month = total_driver_wages_per_month + purchase_cost_per_month + fuel_cost_per_month + total_maintenance_cost_per_month + total_licensing_permits_cost_per_month
except ZeroDivisionError:
  
    st.error("An error occurred: Division by zero is not allowed.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")


columns = ['Total Driver Wage Costs Per Month', 'Total Purchase Costs Per Month', 'Total Fuel Costs Per Month','Total Maintenance Costs Per Month', 'Total Insurance Costs Per Month', 'Total Costs Per Month']
costs = [total_driver_wages_per_month, purchase_cost_per_month, fuel_cost_per_month, total_maintenance_cost_per_month,total_licensing_permits_cost_per_month, total_cost_of_owning_vehicle_per_month ]
df = pd.DataFrame({'Type of Costs': columns, 'Costs': costs})
df['Costs'] = df['Costs'].apply(lambda x: f"${x:,.2f}")


def highlight_total(row):
    return ['font-weight: bold' if row['Type of Costs'] == 'Total Costs Per Month' else '' for _ in row]
styled_df = df.style.apply(highlight_total, axis = 1)    
st.write('### Monthly Cost Quantitative Breakdown')
st.dataframe(styled_df)


dollar_per_mile_calculation = (total_driver_wages_per_month/average_monthly_driven_miles) + (purchase_cost_per_month/average_monthly_driven_miles) + (fuel_cost_per_month/average_monthly_driven_miles) + (total_maintenance_cost_per_month/average_monthly_driven_miles) + (total_licensing_permits_cost_per_month/average_monthly_driven_miles)

if 'show_chart' not in st.session_state:
    st.session_state.show_chart = False


if st.button("Show/Hide Cost Breakdown Chart"):
    st.session_state.show_chart = not st.session_state.show_chart

# Show chart if toggled
if st.session_state.show_chart:
    df = pd.DataFrame({'Cost ($)': costs}, index=columns)
    st.bar_chart(df)
st.markdown(f"<p style='font-size: 30px;'><b>The dollar per mile calculation is: ${dollar_per_mile_calculation:.2f}</b></p>", unsafe_allow_html=True)


third_party_delivery_costs = st.number_input("Please enter the dollar per mile cost of a 3rd party delivery method: ", value = 2.54)


st.markdown("""
### Enter Maximum Percent Premium

This is the **maximum additional percentage** your company is willing to pay for a product or service when features like quality, reputation, or customer support are especially important.

💡 **Example:**  
If a product typically costs 100 dollars and you're comfortable paying 120 dollars because it offers better quality or reliability, that’s a **20% premium** — so you would enter **0.20** below.
""")

PercentPremium = st.number_input("Enter the percent premium as a decimal (e.g., 0.20 for 20%)", min_value=0.0, max_value=1.0, step=0.01, value = 0.20)


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


    
Current_Premium = (dollar_per_mile_calculation - third_party_delivery_costs) / dollar_per_mile_calculation



Cost_Threshold = (st.session_state.slider_val / 10) * PercentPremium



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
        f"<p><strong>Recommendation:</strong> You should use the third-party delivery because the premium you are paying per mile is <strong>${Current_Premium_Value:.2f}</strong>, which is higher than the threshold cost per mile of <strong>${New:.2f}</strong>.</p>",
        unsafe_allow_html=True
    )










