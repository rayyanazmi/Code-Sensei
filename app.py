import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={

    'Content-Type':'application/json'
}
history=[]

def generate_response(Prompt):
    history.append(Prompt)
    final_prompt="\n".join(history)

    data={
        "model":"codesensei",
        "Prompt":final_prompt,
        "stream":False
    }
    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)

interface = gr.Interface(
    fn=generate_response,  # Function to be called for prediction
    inputs=gr.Textbox(lines=2, placeholder="Enter your Prompt"),  # Input textbox
    outputs="text",  # Output display
    title="CodeSensei",  # Title of the interface
    description='''CodeSensei is an A.I. assistant designed to help you with coding tasks and questions.        ggi
    Just enter your code or query in the textbox above, and CodeSensei will provide you with helpful responses and insights.''',  # Description of the interface
    theme="HaleyCH/HaleyCH_Theme",  # Theme for better visualization
)
interface.launch()