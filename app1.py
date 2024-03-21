import streamlit as st
from PIL import Image
import re


st.title("My First Web App")
st.subheader("Tenancy Application eligibility check")

st.text_input("Full Name")

def validate_email(email):
    # Regular expression for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Input email address
email = st.text_input("Email Address")

# Validate email address
if email:
    if validate_email(email):
        st.write("") # displays nothing if email is valid
    else:
        st.write("Invalid email address, Please provide a valid email address")

phone_number_str = st.text_input("Phone Number", value="", max_chars=11)

if phone_number_str:  # Check if the input is not empty
    if not phone_number_str.isdigit() or len(phone_number_str) != 11:
        st.warning("Please enter a valid phone number with 11 digits consisting only of digits (0-9).")
        phone_number = None  # Set phone_number to None if input is invalid
    else:
        phone_number = int(phone_number_str)
else:
    phone_number = None

# Only proceed if the phone number is valid
if phone_number is not None:
    # Further processing or actions can be performed here
    pass


st.text_input("Current Address")

# List of cities in the UK
uk_cities = [
    "London", "Birmingham", "Manchester", "Glasgow", "Liverpool", 
    "Leeds", "Newcastle", "Sheffield", "Bristol", "Belfast", 
    "Cardiff", "Edinburgh", "Leicester", "Belfast", "Nottingham", 
    "Southampton", "Brighton", "Portsmouth", "Aberdeen", "Cambridge"
]

# Create a searchable dropdown list
selected_city = st.selectbox("Select a city", uk_cities)
# Display the selected city
# st.write("You selected:", selected_city)

st.selectbox("Age",["18 - 24","25 - 34","35 -50", "51 and above"])

st.radio("Gender",["Male","Female","Prefer Not to say"])

st.date_input("Proposed move in date")

st.selectbox("Contract length",["6 months","1 year"])

st.markdown("####")

st.write("Please read and accept the following terms & conditions: The information given will be shared with our partners and subject to credit checks before any application is granted")
if st.checkbox("Click to accept terms & Conditions"):
    st.success("Condition Accepted")

st.markdown("##")

st.button("Submit Form")
st.write("Please confirm all details provided are correct before clicking submit")
         
img = Image.open("Capture.JPG")
st.sidebar.image(img)

st.sidebar.header("Tenancy Eligibility Checker")

st.markdown("##")

x = st.sidebar.number_input("Your annual salary (£)", step = 0)
y = st.sidebar.number_input("Your spouse annual salary (£)", step = 0)
z = st.sidebar.number_input("Annual Rent (£)", step = 0)

annual_salary_total = x + y
rent_threshold = 2.5 * z

if st.sidebar.button("Check Eligibility"):
    if  annual_salary_total > rent_threshold:
        st.sidebar.success("Eligible to rent")
    else:
        st.sidebar.error("Not Eligible to rent")




