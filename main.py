import re

# Regras do chatbot
responses = {
    r'qual o seu nome\??|nome': "Meu nome é chatbot, poxa!",
    r'(me conta uma curiosidade)': "Sabia que o primeiro bug na computação foi um inseto preso no computador?",
    r'(olá|oi|bom dia|boa tarde)': "Olá! Como posso ajudar você?",
    r'(você gosta de pizza\?|pizza)': "Claro! Minha favorita é a de dados binários. 🍕",
    r'(me conta uma piada)': "Por que o programador foi ao médico? Porque ele tinha um bug no sistema! 😂",
    r'(estou cansado)': "Entendo... Talvez um cafézinho ajude? ☕",
    r'(feliz natal|natal)': "Ho ho ho! Espero que você ganhe muitos presentes... Ass: Nicola Noel",
    r'(canta uma música)': "Desculpe, sou meio desafinado... Mas posso tentar: You are my fire, The one desire, Believe when I say, I WANT IT THAT WAY!",
    r'tchau|adeus|sair|bye': "Até logo! Se precisar, estarei aqui."
}

def chatbot_response(user_input):
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "Desculpe, não entendi. Pode reformular sua pergunta?"

# Loop de interação
def start_chatbot():
    print("Chatbot: Olá! Sou um chatbot simples. Como posso ajudar?")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['sair', 'tchau', 'adeus']:
            print("Chatbot: Até logo! Foi um prazer ajudar.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Executar chatbot
if __name__ == "__main__":
    start_chatbot()
