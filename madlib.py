from flask import Flask, render_template, request
from app import Story

# Create a Flask app instance
app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# Define a route for the homepage
@app.route("/")
def index():
    # Get the prompts from the story
    prompts = story.prompts
    # Render the form template with the prompts
    return render_template("form.html", prompts=prompts)

# Define a route for the madlibs story
@app.route("/story")
def generate_story():
    # Get the answers from the form
    answers = {}
    for prompt in story.prompts:
        answers[prompt] = request.args.get(prompt)
    # Generate the story using the Story class
    generated_story = story.generate(answers)
    # Render the story template with the generated story
    return render_template("story.html", story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)