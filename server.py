from flask import Flask, render_template, request, jsonify, session


classes_content = {
    'basics': {
        'title': 'Basics',
        'text_content': 'What’s a Stock? A stock is like a 🍰 of a company\'s 🎂, representing a share of ownership and a taste of its 💰or losses.',
        'video_content': 'https://www.example.com/html_intro_video'
    },
    'risk_vs_reward': {
        'title': 'Risk vs. Reward',
        'text_content': 'HTML is the standard markup language for creating Web pages.',
        'video_content': 'https://www.example.com/html_intro_video'
    },
    'compounding': {
        'title': 'Power of Compounding',
        'text_content': 'CSS is a language that describes the style of an HTML document.',
        'video_content': 'https://www.example.com/css_intro_video'
    },
    # Add more classes as needed
}

quizzes_content = {
    'basics': {
        'title': 'Basics',
        'text_content': 'HTML is the standard markup language for creating Web pages.',
        'video_content': 'https://www.example.com/html_intro_video'
    },
    'risk_vs_reward': {
        'title': 'Risk vs. Reward',
        'pop_quiz': {
            'question': "Company A and Company B have these characteristics:",
            'options': {
                'A': "",
                'B': ""
            },
            'correct_answer': 'A',
            'question_id': 'risk_vs_reward_01' 
        },
    },

    'compounding': {
        'title': 'Power of Compounding',
        'text_content': 'CSS is a language that describes the style of an HTML document.',
        'video_content': 'https://www.example.com/css_intro_video'
    },
    'final': {
        'title': 'Final Quiz',
        'text_content': 'CSS is a language that describes the style of an HTML document.',
        'video_content': 'https://www.example.com/css_intro_video'
    },
}

class_quizzes_content = {
    'basics': {
        'title': 'Basics',
        'text_content': 'HTML is the standard markup language for creating Web pages.',
        'video_content': 'https://www.example.com/html_intro_video'
    },
    'risk_vs_reward': {
        'title': 'Risk vs. Reward',
        'class_quiz': {
            'question': "Class Quiz Test 1 ",
            'options': {
                'A': "",
                'B': ""
            },
            'correct_answer': 'A',
            'question_id': 'risk_vs_reward_01' 
        },
    },

    'compounding': {
        'title': 'Power of Compounding',
        'text_content': 'CSS is a language that describes the style of an HTML document.',
        'video_content': 'https://www.example.com/css_intro_video'
    },
    'final': {
        'title': 'Final Quiz',
        'text_content': 'CSS is a language that describes the style of an HTML document.',
        'video_content': 'https://www.example.com/css_intro_video'
    },
    

}

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/record_quiz_answer', methods=['POST'])
def record_quiz_answer():
    quiz_name = request.form['quiz_name']
    answer = request.form['answer']
    correct_answer = quizzes_content[quiz_name]['pop_quiz']['correct_answer']

    # Record the answer and check if it's correct
    session['answers'][quiz_name] = answer
    is_correct = answer == correct_answer

    return jsonify(success=True, correct=is_correct)


@app.route('/class/<class_name>')
def class_info(class_name):
    content = classes_content.get(class_name, None)
    if content:
        return render_template('class.html', content=content)
    else:
        return "Class not found", 404

@app.route('/quiz/<quiz_name>')
def quiz_info(quiz_name):
    content = quizzes_content.get(quiz_name, None)
    if content:
        if quiz_name == 'risk_vs_reward':
            session['start_time'] = datetime.utcnow().isoformat()
            session['answers'] = {}  
        return render_template('quiz.html', content=content, quiz_name=quiz_name)
    else:
        return "Quiz not found", 404
    
@app.route('/class/<class_name>/pop_quiz')
def pop_quiz(class_name):
    class_content = quizzes_content.get(class_name)  
    if class_content and 'pop_quiz' in class_content: 
        return render_template('pop_quiz.html', content=class_content)
    else:
        return "Pop Quiz not found", 404
    
    
@app.route('/lesson/<int:lesson_number>')
def lesson(lesson_number):
    return render_template('lesson.html', lesson_number=lesson_number)

@app.route('/class/<class_name>/class_quiz')
def class_quiz(class_name):
    class_content = class_quizzes_content.get(class_name)  
    
    return render_template('quiz.html', content=class_content)

    







if __name__ == '__main__':
    app.run(debug=True)