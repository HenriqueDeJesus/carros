import openai

openai.api_key = 'sk-proj-iJENGxxtMLlE4vrmsTigT3BlbkFJe7W6Ufa8S8MHnqIiQyMn'

def get_car_ai_bio(model, brand, year):
    message = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = openai.ChatCompletion.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message['content']
