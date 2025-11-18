import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

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

if __name__ == "__main__":
	user_prompt = "What is photosynthesis"
	answer = ask_gemini(user_prompt)
	
	print("PROMPT: ", user_prompt)
	print("GEMINI'S ANSWER: ", answer)