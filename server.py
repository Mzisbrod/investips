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
pop_quiz_content = {
    'Investment Basics Pop Quiz': {
        'module': "pop_quiz_content",
        'title': 'Investment Basics Pop Quiz',
        'text_content': 'Would you rather have a tiny piece of a big, successful company or own a big chunk of a '
                        'tiny, unknown company?',
        'answer_content': [
            {'option': 'Tiny piece of a big company', 'explanation': '🛡️ Safe Bet! Like buying into a blockbuster '
                                                                     'franchise—less drama, more steady returns. Big '
                                                                     'companies = big stability.'},
            {'option': 'Own big chunk of a tiny company', 'explanation': '🚀 High-Risk, High-Reward! Like backing an '
                                                                         'indie film that could hit big or miss hard.'
                                                                         ' It\'s riskier, but if it pops off, '
                                                                         'you\'re set!'}
        ]
    },
    'Risk vs Reward Pop Quiz': {
        'module': "pop_quiz_content",
        'title': 'Risk vs Reward Pop Quiz',
        'text_content': 'Would you rather win $50 for sure or flip a coin for a chance to win $100?',
        'answer_content': [
            {'option': 'Take the $50', 'explanation': '🎉 Guaranteed Cash! Like scoring a guaranteed VIP concert '
                                                      'ticket. It\'s not the front row, but you’re definitely in the '
                                                      'party!'},
            {'option': 'Flip the coin', 'explanation': '🎲 Double or Nothing! Like entering a dance battle—win and '
                                                       'you’re the star, lose and it’s just a cool story. Big gamble, '
                                                       'big glory!'}
        ]
    },
    'Power of Compounding Pop Quiz': {
        'module': "pop_quiz_content",
        'title': 'Power of Compounding Pop Quiz',
        'text_content': 'Would you want your money to grow just by what you add each year, or each dollar earned '
                        'brings in more dollars over time?',
        'answer_content': [
            {'option': 'Just my additions', 'explanation': '🔄 Consistent Adds! Like keeping your social media feed '
                                                           'fresh by only your posts. Steady and totally under your '
                                                           'control!'},
            {'option': 'Money making more money', 'explanation': '💸 Money Multiplier! Like your video going viral '
                                                                 'and pulling more views on its own. Each view drags '
                                                                 'in more, growing your fame without extra clips!'}
        ]
    }
}

quiz_content = {
    'Investment Basics Quiz': {
        'module': "quiz_content",
        'title': 'Investment Basics Quiz',
        'questions': [
            {
                'question_text': "What does buying shares in a company make you?",
                'options': ['A) A customer', 'B) An employee', 'C) An owner', 'D) A creditor'],
                'solution': 'C) An owner'
            },
            {
                'question_text': "If you lend money to the government by buying bonds, what do you usually get in return?",
                'options': ['A) Shares in the government', 'B) Regular interest payments',
                            'C) Free government services', 'D) Company stock'],
                'solution': 'B) Regular interest payments'
            },
            {
                'question_text': "Which of these is likely the safest investment?",
                'options': ['A) Cryptocurrency', 'B) Bonds', 'C) Stocks', 'D) Starting your own business'],
                'solution': 'B) Bonds'
            }
        ],
        'next': "Risk vs. Reward",
        'next_module': "classes_content",
    },
    'Risk vs. Reward Quiz': {
        'module': "quiz_content",
        'title': 'Risk vs Reward Quiz',
        'questions': [
            {
                'question_text': "What does a high-risk investment typically offer?",
                'options': ['A) Lower returns', 'B) Higher returns', 'C) More stability', 'D) Less excitement'],
                'solution': 'B) Higher returns'
            },
            {
                'question_text': "If a friend offers you a part in their startup, which is true?",
                'options': ['A) It’s totally safe', 'B) It could make you rich', 'C) You’ll definitely lose money',
                            'D) B & C'],
                'solution': 'D) B & C'
            },
            {
                'question_text': "What should you consider when choosing an investment?",
                'options': ['A) Color of the logo', 'B) Risk and your comfort with it', 'C) If your friends like it',
                            'D) The weather'],
                'solution': 'B) Risk and your comfort with it'
            }
        ],
        'prev': "Risk vs. Reward",
        'prev_module': "classes_content",
        'next': "Compounding",
        'next_module': "classes_content",
    },
    'Compounding Quiz': {
        'module': "quiz_content",
        'title': 'Power of Compounding Quiz',
        'questions': [
            {
                'question_text': "What happens to your money in a compounding interest scenario?",
                'options': ['A) It decreases over time', 'B) It stays the same',
                            'C) It grows by earning interest on interest', 'D) It gets taxed more'],
                'solution': 'C) It grows by earning interest on interest'
            },
            {
                'question_text': "What's the best strategy for taking advantage of compounding?",
                'options': ['A) Invest once and never again', 'B) Withdraw profits every year', 'C) Reinvest earnings',
                            'D) Ignore market trends'],
                'solution': 'C) Reinvest earnings'
            },
            {
                'question_text': "When is the best time to start investing for compound interest to really show its magic?",
                'options': ['A) At age 50', 'B) As soon as possible', 'C) After retirement',
                            'D) When the stock market is down'],
                'solution': 'B) As soon as possible'
            }
        ],
        'prev': "Compounding",
        'prev_module': "classes_content",
        'next': "Final Quiz",
        'next_module': "quiz_content",
    },
    'Final Quiz': {
        'module': "quiz_content",
        'title': 'Final Quiz',
        'questions': [
            {
                'question_text': "Which type of investment makes you a part-owner of a company?",
                'options': ['A) Bonds', 'B) Stocks', 'C) Mutual Funds', 'D) ETFs'],
                'solution': 'B) Stocks'
            },
            {
                'question_text': "Which investment type traditionally offers fixed returns?",
                'options': ['A) Real estate', 'B) Cryptocurrency', 'C) Bonds', 'D) Commodities'],
                'solution': 'C) Bonds'
            },
            {
                'question_text': "How can diversification help your investment portfolio?",
                'options': ['A) Increases risk', 'B) Decreases risk', 'C) No impact',
                            'D) Only beneficial in short term'],
                'solution': 'B) Decreases risk'
            }
        ],
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
    class_data = classes_content.get(class_name)
    if not class_data:
        return "Class not found", 404

    # Determine the related quiz name for the sidebar link, based on the 'next' key in class_data
    quiz_name = class_data.get('next')

    return render_template('class.html', content=class_data, class_name=class_name, quiz_name=quiz_name)


from flask import request, session


@app.route('/quiz/<quiz_name>', methods=['GET', 'POST'])
def quiz_info(quiz_name):
    content = quiz_content.get(quiz_name, None)
    if not content:
        return "Quiz not found", 404
    # Normal GET request handling
    return render_template('quiz.html', content=content, class_name=quiz_name, quiz_name=quiz_name)


@app.route('/submit_quiz/<quiz_name>', methods=['POST'])
def submit_quiz(quiz_name):
    quiz = quiz_content.get(quiz_name)
    if not quiz:
        return "Quiz not found", 404

    total_score = 0
    total_questions = len(quiz['questions'])
    for i in range(total_questions):
        # Construct the input name based on the index
        input_name = f'selected_answer{i}'
        submitted_answer = request.form.get(input_name)
        correct_answer = quiz['questions'][i]['solution']

        if submitted_answer == correct_answer:
            total_score += 1

    # Continue to process the score as needed
    return jsonify(score=total_score, total=total_questions), 200


@app.route('/results')
def results():
    user_score = sum(score.values()) / len(score.keys()) * 100
    return render_template('results.html', results=score, score=user_score, score_class=score_to_class)


@app.route('/pop_quiz/<quiz_name>', methods=['GET'])
def pop_quiz_info(quiz_name):
    content = pop_quiz_content.get(quiz_name, None)
    if not content:
        return "Pop Quiz not found", 404
    return render_template('pop_quiz.html', content=content, quiz_name=quiz_name)


@app.route('/submit_pop_quiz/<quiz_name>', methods=['POST'])
def submit_pop_quiz(quiz_name):
    selected_option = int(request.form.get('selected_option'))
    content = pop_quiz_content.get(quiz_name, None)
    explanation = content['answer_content'][selected_option]['explanation'] if content else "No explanation available."
    return jsonify({'explanation': explanation})


if __name__ == '__main__':
    app.run(debug=True)
