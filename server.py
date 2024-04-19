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
        'next': "risk_vs_reward_quiz",
        'next_module': "quiz_content",
    },
    'Compounding': {
        'module': "classes_content",
        'title': 'Power of Compounding',
        'text_content': 'Power of Compounding, Power of Compounding, Power of Compounding, Power of Compounding',
        'media_content': "video",
        'prev': "Risk vs. Reward",
        'prev_module': "classes_content",
        'next': "compounding_quiz",
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
    'risk_vs_reward_quiz': {
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
    'compounding_quiz': {
        'module': "quiz_content",
        'title': 'Compounding Quiz',
        'text_content': 'Company A and Company B have these characteristics',
        'answer_content': ['Apple', 'OpenAI'],
        'solution': 'Apple',
        'prev': "Compounding",
        'prev_module': "classes_content",
        'next': "final_quiz",
        'next_module': "quiz_content",
    },
    'final_quiz': {
        'module': "quiz_content",
        'title': 'Final Quiz',
        'text_content': 'Company A and Company B have these characteristics',
        'answer_content': ['Apple', 'OpenAI'],
        'solution': 'Apple',
        'next': "results",
        'next_module': "results.html",
    },
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

@app.route('/quiz/<quiz_name>')
def quiz_info(quiz_name):
    content = quiz_content.get(quiz_name, None)
    if content:
        # if quiz_name == 'risk_vs_reward':
        #     session['start_time'] = datetime.utcnow().isoformat()
        #     session['answers'] = {}
        return render_template('quiz.html', content=content, quiz_name=quiz_name)
    else:
        return "Quiz not found", 404

@app.route('/record_quiz_answer', methods=['POST'])
def record_quiz_answer():
    quiz_name = request.form['quiz_name']
    answer = request.form['answer']
    correct_answer = quiz_content[quiz_name]['pop_quiz']['correct_answer']

    # Record the answer and check if it's correct
    session['answers'][quiz_name] = answer
    is_correct = answer == correct_answer

    return jsonify(success=True, correct=is_correct)

    

@app.route('/class/<class_name>/class_quiz')
def class_quiz(class_name):
    class_content = class_quizzes_content.get(class_name)  
    
    return render_template('class_quiz.html', content=class_content)

@app.route('/update_quiz_score', methods=['POST'])
def update_quiz_score():
    data = request.get_json()
    quiz_name = data['quiz_name']

    print("BEFORE:   \n", class_quizzes_content[quiz_name])

    # Check if the quiz exists in the class_quizzes_content dictionary
    if quiz_name in class_quizzes_content:
        class_quizzes_content[quiz_name]['score'] = "1"

        print("AFTER:   \n", class_quizzes_content[quiz_name])
        return jsonify(success=True, message="Score updated successfully")
    else:
        return jsonify(success=False, message="Quiz not found"), 404
    
@app.route('/results')
def results():
    total_score = sum(int(quiz['score']) for quiz in class_quizzes_content.values() if 'score' in quiz)
    # Assuming you also want to display a title or other content
    content = {
        'title': 'Quiz Results',
        'total_score': total_score
    }
    return render_template('results.html', content=content)




    







if __name__ == '__main__':
    app.run(debug=True)