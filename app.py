from flask import Flask, render_template
import random

app = Flask(__name__)

# Sample jokes
jokes = [
    "How do you comfort a JavaScript bug? You console it.",

"Why did the programmer go broke? Because he used up all his cache.",

"How many programmers does it take to change a light bulb? None; it's a hardware problem.",

"Why do Java developers wear glasses? Because they don't C#.",

"Why don't programmers like nature? It has too many bugs.",

"Why do programmers prefer iOS development over Android development? Because on iOS, you don't have to deal with 'fragmentation.',"

"Why did the programmer quit his job? Because he didn't get arrays.",

"What's a programmer's favorite hangout place? Foo Bar.",

"Why do Python programmers prefer snake_case? Because they don't like Java.",

"What do you call a programmer from Finland? Nerdic.",

"Why was the math book sad? Because it had too many problems.",

"Why did the programmer bring a ladder to the bar? Because he wanted to access the high-level drinks.",

"What do you get when you cross a programmer with a detective? A codebreaker."
]

@app.route('/')
def index():
    # Get a random joke from the list
    random_joke = random.choice(jokes)
    return render_template('index.html', joke=random_joke)

if __name__ == '__main__':
    app.run(debug=True)
