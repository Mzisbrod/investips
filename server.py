from flask import Flask, render_template, request, jsonify


classes_content = {
    'basics': {
        'title': 'Basics',
        'text_content': 'HTML is the standard markup language for creating Web pages.',
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
        'text_content': 'HTML is the standard markup language for creating Web pages.',
        'video_content': 'https://www.example.com/html_intro_video'
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
        return render_template('quiz.html', content=content)
    else:
        return "Class not found", 404

if __name__ == '__main__':
    app.run(debug=True)