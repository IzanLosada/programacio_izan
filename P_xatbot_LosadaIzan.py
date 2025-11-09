from openai import OpenAI
client = OpenAI(api_key="")
rol = input("Que rol debe tener el chat? ")

def chat_gpt(peticio):
    respuesta = client.chat.completions.create (
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": rol},
            {"role": "user", "content": peticio}
        ]
    )

    texto = respuesta.choices[0].message.content
    return texto

pregunta = ""

while pregunta.lower() != "salir":
    pregunta = input("\n💬 Escribe tu pregunta (o 'salir' para terminar): ")

    if pregunta.lower() != "salir":
        print("\n🤖 ChatGPT responde:")
        print(chat_gpt(pregunta))
    else:
        print("Hasta luego!")
