from flask import Flask, render_template
import random

app = Flask(__name__)

# Sample jokes
jokes = [
    "Why was the new IT official hospitalized? He accidentally touched the firewall.",
"Why are the insurance and premiums for all app developers enormously high? Because they are always crashing down!",
"There are 10 types of people in the world. Those who understand binary and those who don't.",
"Why are computers bad at boxing? Their barks are always worse than their bytes!",
"Why was the new band '1023 MB' extremely sad? Since their formation, they haven't had a gig yet.",
"Which artist's concert does a computer geek desperately want to attend? It obviously has to be A-Dell.",
"How did the good teacher teach computer programming to the impatient boy? He taught the kid bit by bit.",
"While visiting a zoo, which animal does a computer like watching the most? The RAM.",
"Why was the PowerPoint presentation so desperate to cross the road? Because it badly wanted to go to the other slide.",
"Why did everyone tell the new computer teacher that he was always extremely confused on Twitter? He didn't follow.",
"Why are all the workers who work at the keyboard factory extremely rich? Because they put in huge numbers of shifts.",
"Why is it that cars produced by computer manufacturers don't last long? Because they have hard drives.",
"Why was the amateur spy fired from his company? Because he couldn't hack it.",
"When a computer was seen robbing a bank, what did the eyewitness report to the police? 'It went data way!'",
"Why are humans known to be extremely afraid of computers? Probably, because they byte.",
"As for punishment, where are naughty disk drives sent? They are always sent to a Boot camp.",
"Which animal is the absolute expert in navigating the internet? Spiders. They know all about the web.",
"Why is it impossible to find a single AC in the rooms or offices of computer programmers? Because they love to open Windows all the time!",
"What did the computer do on its much-awaited vacation at the beach? It had a great time surfing the net.",
"What do computers do for fun, and where do they go for parties? Computers love dancing, especially at disc-os.",
"What did the computer programmer say to his professor when he was unable to submit his coding assignment? The student said, 'My dog ate my assignment. However, it did take him a couple of bytes to finish it.'",
"How many computer programmers does it take to change a light bulb? None; that's a hardware problem.",
"Why is it that people who use the metric system of measurement are experts in computers and computer science? Because they are all very good pro-gram-mers!",
"What did the doctor say when a computer couple had a baby? 'The baby was born chord-less!'",
"Why couldn't the computer science student read his textbook? He couldn't find page 404.",
"Why do Java programmers wear glasses? They can't C#.",
"What does a baby computer call his father? 'Data.'",
"Why does a fly never sit on top of a laptop or a computer? Because it is terribly afraid of the World Wide Web.",
"Why do cats love sitting in front of the computer all day long? Because they don't want to let the mouse out of their sight.",
"What kind of money do computer scientists use? Cache.",
"Why was the computer scientist angry when the student cracked a lame computer joke? He did not like it one bit.",
"Why did the computer programming student panic when he entered the class? Because the professor said, 'Welcome to English 101.'",
"There are 10 kinds of people in the world. Those who understand binary and those who don’t.",
"What did the Java Code say to the C code? You’ve got no class.",
"Why do programmers prefer dark mode? Because light attracts bugs.",
"Things aren’t always #000000 and #FFFFFF.",
"Why do Java programmers have to wear glasses? Because they don’t C#.",
"My love for you has no bugs.",
"What is the most used language in programming? Profanity.",
"My mind is like an internet browser, 19 tabs open, 3 of them are frozen, ads popping up everywhere, I have no idea where the music is coming from"
]

@app.route('/')
def index():
    # Get a random joke from the list
    random_joke = random.choice(jokes)
    return render_template('index.html', joke=random_joke)

if __name__ == '__main__':
    app.run(debug=True)
