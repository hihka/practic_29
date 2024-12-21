from flask import Flask, render_template, request
from g4f.client import Client

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    gift_name = None 
    user_input = None

    if request.method == 'POST':
        user_input = request.form['description']

        client = Client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"""Придумай по описанию человека подарок на новый год. 
            Вот описание '{user_input}'. Ты должна только название подарка. 
            Используй по максимому описания, также можешь предложить несколько вариантов подарка"""}]
        )

        gift_name = response.choices[0].message.content
        return render_template('index.html', gift_name=gift_name, user_input=user_input)
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)

