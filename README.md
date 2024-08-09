# CodeSensei

CodeSensei is an AI-powered coding assistant designed to help you with coding tasks, questions, and queries. Built using Python, Gradio, and the Ollama CodeLlama model, CodeSensei is equipped to provide you with coding solutions, explanations, and insights to help you improve your coding skills.

## Features

- **AI-Powered Code Assistance:** Get help with your coding tasks, whether you're a beginner or an experienced developer.
- **Natural Language Processing:** Understands natural language prompts, allowing you to ask questions in plain English.
- **Multiple Programming Languages:** Supports a variety of programming languages and provides feedback and solutions accordingly.
- **User-Friendly Interface:** Simple and intuitive interface built using Gradio, making it easy to interact with the assistant.

## How It Works

1. **User Input:** The user inputs a coding task or question into the prompt box.
2. **Pre-Processing:** The input is pre-processed, which may involve cleaning, tokenizing, or normalizing the user's input.
3. **Task Analysis:** The assistant determines if the task is code-related. If not, it provides general assistance.
4. **Keyword Extraction:** If code-related, keywords or context are extracted from the input.
5. **Language Detection:** The assistant identifies the programming language used.
6. **Code Analysis:** The assistant analyzes the code structure and logic.
7. **Feedback:** Finally, the assistant provides code feedback, suggestions, or answers to the coding queries.

## Code Explanation

### Key Sections of the Code

```python
import requests
import json
import gradio as gr

# Set the URL for the API endpoint
url="http://localhost:11434/api/generate"

# Define headers for the API request
headers = {
    'Content-Type': 'application/json'
}

# Initialize an empty list to store the conversation history
history = []

def generate_response(Prompt):
    # Append the current prompt to the history
    history.append(Prompt)
    final_prompt = "\n".join(history)

    # Prepare the data to send to the API
    data = {
        "model": "codesensei",
        "Prompt": final_prompt,
        "stream": False
    }

    # Send a POST request to the API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("error:", response.text)

# Setup Gradio interface
interface = gr.Interface(
    fn=generate_response,  # Function to be called for prediction
    inputs=gr.Textbox(lines=2, placeholder="Enter your Prompt"),  # Input textbox
    outputs="text",  # Output display
    title="CodeSensei",  # Title of the interface
    description="CodeSensei is an AI assistant designed to help you with coding tasks and questions. Just enter your code or query in the textbox above, and CodeSensei will provide you with helpful responses and insights.",  # Description of the interface
    theme="HaleyCH/HaleyCH_Theme",  # Theme for better visualization
)

# Launch the interface
interface.launch()
```

### Explanation:

- **Import Statements:** The necessary libraries are imported, including `requests` for making API calls, `json` for handling JSON data, and `gradio` for creating the user interface.
- **URL and Headers:** The URL and headers are set up for making POST requests to the API that powers CodeSensei.
- **Conversation History:** A list named `history` is initialized to store the conversation context, which helps maintain continuity in the dialogue.
- **Generate Response Function:** This function handles the user's prompt, sends it to the API, and processes the response to display it back to the user.
- **Gradio Interface:** The user interface is set up with Gradio, defining the input and output components and setting the title and description.

## Screenshots

### CodeSensei Interface - Initial Prompt


![Screenshot 2024-08-09 235513](https://github.com/user-attachments/assets/84a680b2-4711-49a5-ae93-8f556aa48c17)

*In this screenshot, the user has greeted CodeSensei with "Hello!" and the assistant responds by offering its help for any programming-related tasks.*

### CodeSensei Interface - Coding Assistance

![Screenshot 2024-08-10 000022](https://github.com/user-attachments/assets/3c8385f7-bc16-4a43-9d69-e5b3c3c226c2)

*Here, the user has asked CodeSensei for guidance on creating a portfolio website, and the assistant provides a step-by-step guide on how to get started.*

## Installation

To run CodeSensei locally, follow these steps:

1. Clone the repository.
   ```bash
   git clone https://github.com/yourusername/codesensei.git
   ```
2. Navigate to the project directory.
   ```bash
   cd codesensei
   ```
3. Install the required packages.
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application.
   ```bash
   python codesensei.py
   ```
   
### Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.
