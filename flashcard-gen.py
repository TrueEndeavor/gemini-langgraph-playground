import os
import sys
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

# GENERIC function to ask gemini anything
def ask_gemini(prompt: str)->str:
	if not os.environ.get("GEMINI_API_KEY"):
		raise ValueError(
			"GEMINI_API_KEY not found."
			"Set it in the env: export GEMINI_API_KEY='api-key'"
		)
	try:
		model = genai.GenerativeModel(MODEL_NAME)
		result = model.generate_content(prompt)
		return result.text
	except Exception as e:
		print(f"\nERROR: {str(e)}")

		if "404" in str(e):
			print(f"ERROR: Model '{MODEL_NAME}' not found. Correct the model name")
		if "429" in str(e):
			print(f"ERROR: You've hit the rate limit of Gemini")
		raise

# FLASHCARD GENERATOR
# Step 1: Generate Questions
def generate_questions(topic: str) -> list:
	prompt = f"""
	Generate 5 study questions of one-word answers about {topic}

	Requirements:
	- Test understanding
	- Mix difficulty levels
	- Return ONLY questions, numbered 1-5
	- One per line

	Example:
	1. What is [topic]?
	"""

	print(f"Generating questions about '{topic}...")
	response = ask_gemini(prompt)

	print("Raw Response")
	print(response)

	return []

# Main function
if __name__ == "__main__":
	try:
		with open("prompt.txt", "r") as f:
			user_prompt = f.read().strip()
		print(f"Reading from prompt.txt")
	except FileNotFoundError:
		print("ERROR: prompt.txt not found")
		print("Create prompt.txt with your question and try again")
		sys.exit(1)

	if not user_prompt:
		print("ERROR: prompt.txt is empty")
		sys.exit(1)
		
	#answer = ask_gemini(user_prompt)
	
	#print("GEMINI'S ANSWER: ", answer)

	print("Basic Flashcard Generator")
	print("PROMPT: ", user_prompt)
	questions = generate_questions(user_prompt)
	# TODO: Generate Answers
	# TODO: Save flashcards in file

	print("\nDone")