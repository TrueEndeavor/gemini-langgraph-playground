# gemini-langgraph-playground
A simple playground to experiment with Google Gemini models and LangGraph in Python.
This repository is for 
- learning
- testing small ideas and
- building basic AI workflows step-by-step

## Project 1: 'gemini-hello.py' (Completed) ✅
    My first gemini API integration

### Learnings:
    - How to use Gemini API, Models
    - Error handling
    - Reading from external file

### How to use:
    ```bash
    export GEMINI_API_KEY="key-here"
    echo "What is <question>?" > prompt.txt
    python gemini-hello.py
    ```

## Project 2: 'flashcard-gen.py' (In progress) 🚧

Building a flashcard generator to learn multi-step AI workflows.

    The Flow
        Topic (from prompt.txt)
        ↓
        Generate Questions (Phase 2 - TODO)
        ↓
        Generate Answers (Phase 3 - TODO)
        ↓
        Save Flashcards (Phase 4 - TODO)

### Learnings:
    - Manual workflow orchestration (the hard way!)
    - Will learn: Why LangGraph exists (after feeling the pain)

### Current Status:
    - ✅ Phase 1: Basic structure & file reading
    - ✅ Phase 2: Generate questions (next)
    - ✅ Phase 3: Generate answers
    - ✅ Phase 4: Save flashcards

### How to use:
    ```bash
    export GEMINI_API_KEY="key-here"
    echo "Photosynthesis" > prompt.txt
    python flashcard-gen.py
    ```
