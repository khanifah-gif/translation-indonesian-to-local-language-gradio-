import gradio as gr
from llama_cpp import Llama

model = Llama(
    model_path="resources/gemma2-9b-cpt-sahabatai-v1-instruct.Q2_K.gguf"
)

langs = ["javanese", "sundanese"]

def translate(text, lang):
    prompts = {
        "javanese": "Translate the following text into Javanese.",
        "sundanese": "Translate the following text into Sundanese."
    }
    prompt = prompts.get(lang, "Translate the following text.")
    messages = [
        {"role": "system", "content": f"{prompt}"},
        {"role": "user", "content": f"{text}"}
    ]
    output = model.create_chat_completion(messages=messages)
    return output["choices"][0]["message"]["content"]

sample_text = [
    ["Saya mau beli gudegnya dua porsi ya Bu."],
    ["Kalau saya mau naik andong, harus menunggu di mana?"]
]

demo = gr.Interface(
    fn=translate,
    inputs=[
        gr.components.Textbox(label="Text"),
        gr.components.Dropdown(label="Target Language", choices=langs)
    ],
    outputs=gr.Textbox(label="Translated Text"),
    examples=sample_text,
    cache_examples=False,
    title="Translation of Indonesian to Local Language",
)

demo.launch()