import torch
from transformers import GPTJForCausalLM, AutoTokenizer

# Ruta al directorio donde se descargaron los archivos del modelo
model_path = "C:/Users/your_username/.cache/huggingface/hub/models--EleutherAI--gpt-j-6B/snapshots/47e169305d2e8376be1d31e765533382721b2cc1"

# Cargar el tokenizador y el modelo desde el directorio local
print("Cargando el tokenizador y el modelo...")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = GPTJForCausalLM.from_pretrained(model_path)

def generar_respuesta_gptj(pregunta):
    prompt = f"Pregunta: {pregunta}\nRespuesta:"
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    
    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=50,  # Reducir la longitud máxima de la respuesta
            do_sample=True,
            top_p=0.90,  # Ajustar la probabilidad de muestreo
            top_k=50,  # Ajustar el número de mejores opciones consideradas en cada paso
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )
    respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return respuesta

if __name__ == "__main__":
    while True:
        pregunta = input("Ingrese su pregunta: ")
        if pregunta.lower() in ["salir", "exit", "quit"]:
            print("Saliendo...")
            break
        respuesta = generar_respuesta_gptj(pregunta)
        print("GPT-J Responde:", respuesta)
