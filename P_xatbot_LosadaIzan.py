from openai import OpenAI

client = OpenAI(api_key="") 
rol = input("Que rol debe tener el chat? ")

COLOR_USUARIO = "\033[94m"   
COLOR_CHATGPT = "\033[92m"   
COLOR_RESET = "\033[0m"      

def chat_gpt(peticio):
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": rol},
            {"role": "user", "content": peticio}
        ]
    )

    texto = respuesta.choices[0].message.content
    return texto

pregunta = ""

while pregunta.lower() != "salir":
    pregunta = input(f"{COLOR_USUARIO}💬 Escribe tu pregunta (o 'salir' para terminar): {COLOR_RESET}")

    if pregunta.lower() != "salir":
        print(f"\n{COLOR_CHATGPT}🤖 ChatGPT responde:{COLOR_RESET}")
        print(f"{COLOR_CHATGPT}{chat_gpt(pregunta)}{COLOR_RESET}")
    else:
        print("Hasta luego!")

