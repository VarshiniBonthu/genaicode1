import google.generativeai as genai
import json

def generate_recipe(food, profession):
    """Generates a recipe based on given parameters.

    Args:
        food: The type of food.
        profession: The target user's profession.

    Returns:
        A dictionary containing the recipe, or None if an error occurs.
    """

    try:
        # Configure API key
        genai.configure(api_key="AIzaSyCHqUPsZJPk1X6D4nYRlZ9wZ6dWfhwIwSk")

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
            system_instruction="You are an expert chef. Create delicious recipes tailored to the user's needs, including food type and profession.",
        )

        # Construct the prompt
        prompt = f"Create a recipe for a {profession} that features {food}. Include a clear list of ingredients with quantities and detailed instructions."

        # Generate the recipe
        response = model.generate_content(prompt)
        recipe_text = response.text

        # Basic recipe formatting (you can enhance this)
        recipe_dict = {"ingredients": [], "instructions": []}
        current_section = "ingredients"
        for line in recipe_text.split("\n"):
            if line.startswith("Ingredients:"):
                current_section = "ingredients"
            elif line.startswith("Instructions:"):
                current_section = "instructions"
            else:
                recipe_dict[current_section].append(line)

        return recipe_dict

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
food = str(input())
profession = str(input())

recipe = generate_recipe(food, profession)
if recipe:
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print("- " + ingredient)
    print("\nInstructions:")
    for step in recipe["instructions"]:
        print("- " + step)
else:
    print("Failed to generate recipe.")