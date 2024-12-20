import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}:")

# Get the temperature/sky data
if place:
    try:
        filtered_data = get_data(place, days)
        # Create a temperature plot
        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]

            # Set how many images we want per row
            images_per_row = 4
            num_rows = len(image_paths) // images_per_row + (1 if len(image_paths) % images_per_row > 0 else 0)

            # Display images in rows
            for row in range(num_rows):
                start_idx = row * images_per_row
                end_idx = start_idx + images_per_row
                row_images = image_paths[start_idx:end_idx]

                # Create columns for the current row
                cols = st.columns(len(row_images))

                # Display each image in its corresponding column
                for i, img in enumerate(row_images):
                    cols[i].image(img, width=115)
    except KeyError:
        st.error("Oh you entered a non-existing place!")


