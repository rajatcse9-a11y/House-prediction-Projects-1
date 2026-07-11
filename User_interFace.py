import streamlit as st
import joblib
import pandas as pd

# page config
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# load model
model = joblib.load("model.pkl")


# CSS
st.markdown("""
<style>

.main{
    background-color:#f5f9ff;
}

.title{
    text-align:center;
    font-size:45px;
    font-weight:700;
    color:#123b73;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#54657d;
}

.card{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0 4px 15px rgba(0,0,0,0.1);
}

.result{
    background:#e9f7ef;
    padding:25px;
    border-radius:20px;
    font-size:25px;
    color:#1e7e34;
}

.stButton>button{
    width:250px;
    height:55px;
    border-radius:15px;
    font-size:20px;
    background:#1769ff;
    color:white;
}

</style>
""", unsafe_allow_html=True)



# Header

st.markdown(
"""
<div class="title">
🏠 House Price Prediction
</div>

<div class="subtitle">
Find out the estimated price of your dream home
</div>
""",
unsafe_allow_html=True
)


st.write("")


# Form card

st.markdown('<div class="card">', unsafe_allow_html=True)


st.subheader("🏡 Enter House Details")


col1,col2,col3,col4 = st.columns(4)


with col1:
    area_type = st.selectbox(
        "Area Type",
        [
        "Super built-up  Area",
        "Built-up  Area",
        "Plot  Area"
        ]
    )


with col2:
    availability = st.selectbox(
        "Availability",
        [
        "Ready To Move",
        "19-Dec"
        ]
    )


with col3:
    location = st.selectbox(
        "Location",
        [
        'Electronic City Phase II',
        'Chikka Tirupathi', 'Uttarahalli',
        '12th cross srinivas nagar banshankari 3rd stage',
        'Havanur extension', 'Abshot Layout'
        ]
    )


with col4:
    size = st.selectbox(
        "Size",
        [
        "1 BHK",
        "2 BHK",
        "3 BHK",
        "4 BHK"
        ]
    )



col5,col6,col7 = st.columns(3)


with col5:
    total_sqft = st.number_input(
        "Total Sqft",
        min_value=300
    )


with col6:
    bath = st.number_input(
        "Bathroom",
        min_value=1
    )


with col7:
    balcony = st.number_input(
        "Balcony",
        min_value=0
    )



st.markdown("</div>", unsafe_allow_html=True)



st.write("")


# Prediction

if st.button("🏠 Predict Price"):


    input_data = pd.DataFrame(
        [[
            area_type,
            availability,
            location,
            size,
            total_sqft,
            bath,
            balcony
        ]],
        columns=[
            'area_type',
            'availability',
            'location',
            'size',
            'total_sqft',
            'bath',
            'balcony'
        ]
    )


    prediction = model.predict(input_data)


    st.markdown(
    f"""
    <div class="result">
    🏠 Estimated Price<br><br>
    ₹ {prediction[0]:,.2f}
    </div>
    """,
    unsafe_allow_html=True
    )