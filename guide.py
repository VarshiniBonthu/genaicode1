import streamlit as st
import google.generativeai as genai
import json

# Set page title
st.title("Get your tour guidance")

def generate_tour(place, days, budget):
    

    try:
        # Configure API key
        genai.configure(api_key="AIzaSyDltlA-mkVR_k8SjmTa7joJND5f6VYmJ1o")

        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are an GenExplorer. You should act as tour guide and make a plan according to the place, days, and the given budget.",
        )

        # Construct the prompt
        prompt = f"Create a complete tour based upon {place}, {days} and according to the {budget}"
        # Generate the recipe
        response = model.generate_content(prompt)
        tourguide_text = response.text

        # Basic recipe formatting (you can enhance this)
        tour_dict = {"places to visit": [], "instructions": []}
        current_section = "places to visit"
        for line in tourguide_text.split("\n"):
            if line.startswith("places to visit:"):
                current_section = "places to visit"
            elif line.startswith("Instructions:"):
                current_section = "instructions"
            else:
                tour_dict[current_section].append(line)

        return tour_dict

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Create input fields
place = st.text_input("Enter your destination:")
days = st.text_input("Enter the number of days for the tour:")
budget = st.text_input("Enter your budget for the tour:")

# Create a button to generate the tour plan
if st.button("Generate Tour Plan"):
    output = generate_tour(place, days, budget)
    if output:
        st.write("Tour Plan:")
        st.write(output)
    else:
        st.write("Failed to generate tour plan.")