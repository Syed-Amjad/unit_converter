import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Streamlit UI
st.title("Google Unit Converter 🌍")

# Dropdown options
categories = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "cup", "fluid_ounce"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"]
}

# Select category
category = st.selectbox("Select a category:", list(categories.keys()))

# Select units
from_unit = st.selectbox("From:", categories[category])
to_unit = st.selectbox("To:", categories[category])

# Input value
value = st.number_input("Enter value:", min_value=0.0, format="%.6f")

# Convert button
if st.button("Convert"):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.6f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion Error: {e}")
