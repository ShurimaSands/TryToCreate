from transformers import GPTJForCausalLM, AutoTokenizer

# Descargar y cargar el tokenizador
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

# Descargar y cargar el modelo
model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
