from flask import Flask, render_template, request, jsonify, session, redirect, url_for


classes_content = {
    'stocks': {
        'module': "basics",
        'title': "What's a Stock?",
        'text_content': 'A stock is like a 🍰 of a company\'s 🎂, representing a share of ownership and a taste of its 💰or losses.',
        'media_content': "video",
        'next_module': "basics",
        'next': "bonds"
    },
    'bonds': {
        'module': "basics",
        'title': "What's a Bond?",
        'text_content': 'A Bond is like a 🍰 of a company\'s 🎂, representing a share of ownership and a taste of its 💰or losses.',
        'media_content': "video",
        'prev': "stocks",
        'prev_module': "classes_content",
        'next': "Risk vs. Reward",
        'next_module': "classes_content",
    },
    'Risk vs. Reward': {
        'module': "classes_content",
        'title': 'Risk vs. Reward Plot',
        'text_content': 'Risk vs Reward, Risk vs Reward, Risk vs Reward, Risk vs Reward, Risk vs Reward',
        'media_content': "video",
        'prev': "bonds",
        'prev_module': "classes_content",
        'next': "Risk vs. Reward Quiz",
        'next_module': "quiz_content",
    },
    'Compounding': {
        'module': "classes_content",
        'title': 'Power of Compounding',
        'text_content': 'Power of Compounding, Power of Compounding, Power of Compounding, Power of Compounding',
        'media_content': "video",
        'prev': "Risk vs. Reward",
        'prev_module': "classes_content",
        'next': "Compounding Quiz",
        'next_module': "quiz_content",
    },
    # Add more classes as needed
}

quiz_content = {
    "pop_quiz": {
        'module': "quiz_content",
        'title': 'Pop Quiz',
        'text_content': 'Company A and Company B have these characteristics',
        'answer_content': ['Apple', 'OpenAI'],
        'solution': 'Apple',
        'next': "Risk vs. Reward",
        'next_module': "classes_content",
    },
    'Risk vs. Reward Quiz': {
        'module': "quiz_content",
        'title': 'Risk vs. Reward Quiz',
        'text_content': 'Company A and Company B have these characteristics',
        'answer_content': ['Apple', 'OpenAI'],
        'solution': 'Apple',
        'prev': "Risk vs. Reward",
        'prev_module': "classes_content",
        'next': "Compounding",
        'next_module': "classes_content",
    },
    'Compounding Quiz': {
        'module': "quiz_content",
        'title': 'Compounding Quiz',
        'text_content': 'Company A and Company B have these characteristics',
        'answer_content': ['Apple', 'OpenAI'],
        'solution': 'Apple',
        'prev': "Compounding",
        'prev_module': "classes_content",
        'next': "Final Quiz",
        'next_module': "quiz_content",
    },
    'Final Quiz': {
        'module': "quiz_content",
        'title': 'Final Quiz',
        'text_content': 'Company A and Company B have these characteristics',
        'answer_content': ['Apple', 'OpenAI'],
        'solution': 'Apple',
        'next': "results",
        'next_module': "results.html",
    },
}
score = {
    'Risk vs. Reward Quiz': 0,
    'Compounding Quiz': 0,
    'Final Quiz': 0,

}

score_to_class = {
    'Risk vs. Reward Quiz': 'Risk vs. Reward',
    'Compounding Quiz': 'Compounding',
    'Final Quiz': 'stocks',
}



app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/class/<class_name>')
def class_info(class_name):
    content = classes_content.get(class_name, None)
    if content:
        return render_template('class.html', content=content, class_name=class_name)
    else:
        return "Class not found", 404

from flask import request, session

@app.route('/quiz/<quiz_name>', methods=['GET', 'POST'])
def quiz_info(quiz_name):
    content = quiz_content.get(quiz_name, None)
    if not content:
        return "Quiz not found", 404
    # Normal GET request handling
    return render_template('quiz.html', content=content, quiz_name=quiz_name)

@app.route('/submit_quiz/<quiz_name>', methods=['POST'])
def submit_quiz(quiz_name):
    submitted_answer = request.form.get('selected_answer')

    correct_answer = quiz_content[quiz_name]['solution']

    # Check if the answer is correct
    if submitted_answer == correct_answer:
        # Update the score for the quiz_name if the answer is correct
        score[quiz_name] = 1
    print(f"submit quiz route report:\n submitted answer = {submitted_answer}\n"
          f"correct answer = {correct_answer}\n score dict: {score}")
    # No need to return anything as per the requirements
    return '', 204  # HTTP 204 No Content response


@app.route('/results')
def results():
    user_score = sum(score.values())/len(score.keys())*100
    return render_template('results.html', results=score, score=user_score, score_class=score_to_class)



if __name__ == '__main__':
    app.run(debug=True)