import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

def ask_gemini(prompt: str)->str:
	model = genai.GenerativeModel(MODEL_NAME)
	result = model.generate_content(prompt)
	return result.text

if __name__ == "__main__":
	user_prompt = "What is photosynthesis"
	answer = ask_gemini(user_prompt)
	
	print("PROMPT: ", user_prompt)
	print("GEMINI'S ANSWER: ", answer)