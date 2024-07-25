import google.generativeai as genai
import json

def generate_tour(place,days,budget):
    """It acts as a tour guide for the person.To make their work.

    Args:
        food: The type of food.
        profession: The target user's profession.

    Returns:
        A dictionary containing the recipe, or None if an error occurs.
    """

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
            system_instruction="You are an GenExplorer.you should act as tourguide and you should make a plan according the place,days and the given budget.",
        )

        # Construct the prompt
        prompt = f"Create a complete tour based upon {place},{days} and  according to the {budget}"
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
                    tour_dict [current_section].append(line)

        return tour_dict 

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
place = str(input())
days = str(input())
budget=str(input())

output = generate_tour(place,days,budget)
print(output)