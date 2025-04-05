from google import genai

prompt = """I am in Manchester, I have budget of 50 pounds, and I like arcade games and clubbing. Give me a plan of what should I do. Make sure the plan contains minimum travel between locations.

Give your response only using the JSON schema:

Plan = {Location 1: str, 'opening time': str, 'estimated spending': int, short description: str},
        {Location 2: 'location_2': str, 'opening time': str, 'estimated spending': int, short description: str},
        ...}
Return: list[Recipe]"""

client = genai.Client(api_key="AIzaSyA64UDrH42FCnZUmsxEdpJwY1EMwXKaQ-I")

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=prompt,
)

# Use the response as a JSON string.
print(response.text)

