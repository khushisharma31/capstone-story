from flask import Flask, render_template, request, session
from transformers import pipeline

app = Flask(__name__)
app.secret_key = 'angoorbandar'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    genre = request.form['genre']
    prompt = request.form['prompt']
    story_length = int(request.form['story_length'])

    session['genre'] = genre
    session['prompt'] = prompt
    session['story_length'] = story_length

    generated_story = generate_story_text(genre, prompt, story_length)

    return render_template('index.html', generated_story=generated_story)

def generate_story_text(genre, prompt, story_length):
    story_generator = pipeline("text-generation", f"pranavpsv/gpt2-genre-story-generator")
    story = story_generator(f"<BOS> <{genre}> {prompt}", max_length=story_length)

    return story[0]["generated_text"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
