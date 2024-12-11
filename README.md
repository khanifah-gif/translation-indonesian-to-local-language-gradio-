# Translation Indonesian to Local Language Demo

## Prerequisites:
- Python 3.10.13

## How to Run
### Setup

- Copy `.env.example` to `.env`
```sh
cp .env.example .env
```

- Set up machine learning configuration in `.env` file

```
# Path for your model directory
MODEL=<MODEL>
```

- Download the model in the huggingface repository and replace it into your model directory. In this case I'm using type of Q2_K gguf. Feel free to change the type of gguf model, depend on your storage & core memory. The differences in the type of gguf model may affect the quality of the results.

```sh
wget "https://huggingface.co/gmonsoon/gemma2-9b-cpt-sahabatai-v1-instruct-GGUF/resolve/main/gemma2-9b-cpt-sahabatai-v1-instruct.Q2_K.gguf?download=true" -O your_model_path/gemma2-9b-cpt-sahabatai-v1-instruct.Q2_K.gguf
```

- Install all dependency / python modules. It's better using virtual environment.

```sh
(translation-indonesian-to-local-language) $ pip install -r requirements.txt
```

### Run app

```sh
(translation-indonesian-to-local-language) $ python app.py
```