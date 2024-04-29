from flask import Flask, render_template, request, jsonify, session, redirect, url_for

classes_content = {
    'stocks': {
        'module': "basics",
        'title': "What's a Stock?",
        'text_content': 'A stock is like a 🍰 of a company\'s 🎂, representing a share of ownership and a taste of '
                        'its 💰or losses.',
        'media_content': 'https://www.youtube.com/embed/CF_bij95mAA',
        'next_module': "basics",
        'next': "bonds"
    },
    'bonds': {
        'module': "basics",
        'title': "What's a Bond?",
        'text_content': 'Imagine lending money to your high school for a new skate park. They promise to pay you back '
                        'with interest. Safe, steady, but not gonna make you rich quick.',
        'media_content': "https://www.youtube.com/embed/PKjy5j9VNdE",
        'prev': "stocks",
        'prev_module': "classes_content",
        'next': "Basics Quiz",
        'next_module': "quiz_content",
    },
    'Risk vs. Reward': {
        'module': "classes_content",
        'title': 'Risk vs. Reward',
        'text_content': 'This concept like the seesaw in the playground. If one side goes up, the other comes '
                        'down. In investing, if you take bigger risks, the potential for big rewards goes up. But so '
                        'does the chance of taking a hit.',
        'media_content': "https://www.youtube.com/embed/j1TioBRFvwo",
        'prev': "bonds",
        'prev_module': "classes_content",
        'next': "Risk vs. Reward 2",
        'next_module': "classes_content",
    },
    'Risk vs. Reward 2': {
        'module': "classes_content",
        'title': 'Risk vs. Reward',
        'text_content': '<Add content here>',
        'media_content': "https://www.youtube.com/embed/O-QwiAGtu88",
        'prev': "Risk vs. Reward",
        'prev_module': "classes_content",
        'next': "Risk vs. Reward Quiz",
        'next_module': "quiz_content",
    },
    'Compounding': {
        'module': "classes_content",
        'title': 'Power of Compounding',
        'text_content': 'Think of compounding as the ultimate collab on TikTok. You post a video that does well, '
                        'so it starts earning likes and shares. But here’s the kicker—each new like and share can '
                        'lead to even more likes and shares. It’s like a snowball rolling down a hill, growing bigger '
                        'and faster as it goes. That’s your investment growing!',
        'media_content': "https://www.youtube.com/embed/G2ruiumT8xc",
        'prev': "Risk vs. Reward",
        'prev_module': "classes_content",
        'next': "Compounding 2",
        'next_module': "classes_content",
    },
    'Compounding 2': {
        'module': "classes_content",
        'title': 'Compounding',
        'text_content': '<Add content here>',
        'media_content': "https://www.youtube.com/embed/V7WLYoQNu80",
        'prev': "Compounding",
        'prev_module': "classes_content",
        'next': "Compounding Quiz",
        'next_module': "quiz_content",
    }
}

quiz_content = {
    'Basics Quiz': {
        'prev': "bonds",
        'module': "quiz_content",
        'title': 'Investment Basics Quiz',
        'questions': [
            {
                "questionId": "01",
                'question_text': "Would you rather have a tiny piece of a big, successful company or own a big chunk "
                                 "of a tiny, unknown company?",
                'options': ['Tiny piece of a big company', 'Own big chunk of a tiny company'],
                'explanation': {
                    'Tiny piece of a big company': '🛡️ Safe Bet! Like buying into a blockbuster franchise—less '
                                                   'drama, more steady returns. Big companies = big stability.',
                    'Own big chunk of a tiny company': '🚀 High-Risk, High-Reward! Like backing an indie film that '
                                                       'could hit big or miss hard. It\'s riskier, but if it pops '
                                                       'off, you\'re set!'
                },
                'is_pop_quiz': True
            },
            {
                "questionId": "02",
                'question_text': "What does buying shares in a company make you?",
                'options': ['A) A customer', 'B) An employee', 'C) An owner', 'D) A creditor'],
                'solution': 'C) An owner',
                'explanation': {
                        'A) A customer': '🛍️ Shopper Alert! Buying shares doesn’t mean shopping, it means owning a '
                                         'slice of the company pie.',
                        'B) An employee': '👔 No badge required. Buying shares makes you an owner, not a staff member.',
                        'C) An owner': '🏢 Part-owner vibes! Shareholders own a piece of the company, influencing it '
                                       'through votes.',
                        'D) A creditor': '💸 Not quite. Creditors lend money, shareholders buy ownership.'
                    },
            },
            {
                "questionId": "03",
                'question_text': "If you lend money to the government by buying bonds, what do you usually get in return?",
                'options': ['A) Shares in the government', 'B) Regular interest payments',
                            'C) Free government services', 'D) Company stock'],
                'solution': 'B) Regular interest payments',
                'explanation': {
                        'A) Shares in the government': '🚫 No equity here! Government bonds don’t give shares.',
                        'B) Regular interest payments': '💵 Income Stream! Bonds pay you back with regular interest—like getting a rent check.',
                        'C) Free government services': '🆓 No freebies. Buying bonds doesn’t cover your taxes or fees.',
                        'D) Company stock': '🏢 Wrong aisle! Bonds are loans, not stock investments.'
                    }
            },
            {
                "questionId": "04",
                'question_text': "Which of these is likely the safest investment?",
                'options': ['A) Cryptocurrency', 'B) Bonds', 'C) Stocks', 'D) Starting your own business'],
                'solution': 'B) Bonds',
                'explanation': {
                        'A) Cryptocurrency': '🎢 Ride the rollercoaster! Crypto is exciting but not safe.',
                        'B) Bonds': '🛡️ Safety First! Bonds offer more stability and predictable returns.',
                        'C) Stocks': '📈 Ups and downs. Stocks can grow wealth but come with volatility.',
                        'D) Starting your own business': '🚀 High risk, high reward. Thrilling but risky.'
                    }
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
                "questionId": "05",
                'question_text': "Would you rather win $50 for sure or flip a coin for a chance to win $100?",
                'options': ['Take the $50', 'Flip the coin'],
                'explanation': {
                    'Take the $50': '🎉 Guaranteed Cash! Like scoring a guaranteed VIP concert ticket. It\'s not the front row, but you’re definitely in the party!',
                    'Flip the coin': '🎲 Double or Nothing! Like entering a dance battle—win and you’re the star, lose and it’s just a cool story. Big gamble, big glory!'
                },
                'is_pop_quiz': True
            },
            {
                "questionId": "06",
                'question_text': "What does a high-risk investment typically offer?",
                'options': ['A) Lower returns', 'B) Higher returns', 'C) More stability', 'D) Less excitement'],
                'solution': 'B) Higher returns',
                'explanation': {
                    'A) Lower returns': '📉 Not necessarily. High risk often aims for high returns, not low.',
                    'B) Higher returns': '🚀 Potential Profit! High risk could mean big rewards if things go well.',
                    'C) More stability': '🔍 Opposite day? High risk means more ups and downs.',
                    'D) Less excitement': '😂 Guess again! High risk is the thriller genre of investing.'
                }
            },
            {
                "questionId": "07",
                'question_text': "If a friend offers you a part in their startup, which is true?",
                'options': ['A) It’s totally safe', 'B) It could make you rich', 'C) You’ll definitely lose money',
                            'D) B & C'],
                'solution': 'B) It could make you rich',
                'explanation': {
                    'A) It’s totally safe': '🛑 Misleading! Startups are risky business ventures.',
                    'B) It could make you rich': '💰 Potential jackpot! If the startup succeeds, the payoff can be huge.',
                    'C) You’ll definitely lose money': '💸 Risky, but not a guarantee. Startups can fail or flourish.',
                    'D) B & C': '🔄 Mixed bag! It’s a gamble with possibilities of riches or rags.'
                }
            },
            {
                "questionId": "08",
                'question_text': "What should you consider when choosing an investment?",
                'options': ['A) Color of the logo', 'B) Risk and your comfort with it', 'C) If your friends like it',
                            'D) The weather'],
                'solution': 'B) Risk and your comfort with it',
                'explanation': {
                    'A) Color of the logo': '🌈 Not the best strategy! Looks aren’t everything in investments.',
                    'B) Risk and your comfort with it': '🤔 Personal fit! Align investments with your risk tolerance and goals.',
                    'C) If your friends like it': '👥 Friend-approved? Nice, but not a financial strategy.',
                    'D) The weather': '☀️🌧️ Irrelevant! Market climates, not weather forecasts, matter here.'
                }
            }
        ],
        'prev': "Risk vs. Reward 2",
        'prev_module': "classes_content",
        'next': "Compounding",
        'next_module': "classes_content",
    },
    'Compounding Quiz': {
        'module': "quiz_content",
        'title': 'Power of Compounding Quiz',
        'questions': [
            {
                "questionId": "09",
                'question_text': "Would you want your money to grow just by what you add each year, or each dollar earned brings in more dollars over time?",
                'options': ['Just my additions', 'Money making more money'],
                'explanation': {
                    'Just my additions': '🔄 Consistent Adds! Like keeping your social media feed fresh by only your posts. Steady and totally under your control!',
                    'Money making more money': '💸 Money Multiplier! Like your video going viral and pulling more views on its own. Each view drags in more, growing your fame without extra clips!'
                },
                'is_pop_quiz': True
            },
            {
                "questionId": "10",
                'question_text': "What happens to your money in a compounding interest scenario?",
                'options': ['A) It decreases over time', 'B) It stays the same',
                            'C) It grows by earning interest on interest', 'D) It gets taxed more'],
                'solution': 'C) It grows by earning interest on interest',
                'explanation': {
                    'A) It decreases over time': '📉 Not here! Compounding means growth, not shrinkage.',
                    'B) It stays the same': '❌ No change? Missed the magic of compounding!',
                    'C) It grows by earning interest on interest': '🪄 Magic Money! Your investment grows exponentially over time.',
                    'D) It gets taxed more': '🏦 Tax happens, but that’s not the focus of compounding.'
                }
            },
            {
                "questionId": "11",
                'question_text': "What's the best strategy for taking advantage of compounding?",
                'options': ['A) Invest once and never again', 'B) Withdraw profits every year', 'C) Reinvest earnings',
                            'D) Ignore market trends'],
                'solution': 'C) Reinvest earnings',
                'explanation': {
                    'A) Invest once and never again': '🔄 Missing out! Reinvesting fuels the compounding engine.',
                    'B) Withdraw profits every year': '💸 Slows the growth. Leaving earnings in plays into compounding’s strengths.',
                    'C) Reinvest earnings': '🔄 Power move! Reinvest to maximize the compounding effect.',
                    'D) Ignore market trends': '👀 Wise to watch, but compounding works independently of trends.'
                }
            },
            {
                "questionId": "12",
                'question_text': "When is the best time to start investing for compound interest to really show its magic?",
                'options': ['A) At age 50', 'B) As soon as possible', 'C) After retirement',
                            'D) When the stock market is down'],
                'solution': 'B) As soon as possible',
                'explanation': {
                    'A) At age 50': '🕰️ Better late than never, but earlier is better.',
                    'B) As soon as possible': '⏳ The sooner, the better! Compounding loves time.',
                    'C) After retirement': '🚶‍♂️ Late start! Earlier investments have more time to grow.',
                    'D) When the stock market is down': '📉 Market conditions vary, but starting early always pays off.'
                }
            }
        ],
        'prev': "Compounding 2",
        'prev_module': "classes_content",
        'next': "Final Quiz",
        'next_module': "quiz_content",
    },
    'Final Quiz': {
        'module': "quiz_content",
        'title': 'Final Quiz',
        'questions': [
            {
                "questionId": "13",
                'question_text': "Which type of investment makes you a part-owner of a company?",
                'options': ['A) Bonds', 'B) Stocks', 'C) Mutual Funds', 'D) ETFs'],
                'solution': 'B) Stocks',
                'explanation': {
                    'A) Bonds': '💵 Lender, not owner. Bonds are about debt, not equity.',
                    'B) Stocks': '📈 Shareholder alert! Owning stocks means owning part of a company.',
                    'C) Mutual Funds': '🔄 Mix and match! Funds may include stocks but offer diversified holdings.',
                    'D) ETFs': '🌐 Broad spectrum. ETFs might hold stocks but you own shares of the fund, not the companies directly.'
                }
            },
            {
                "questionId": "14",
                'question_text': "Which investment type traditionally offers fixed returns?",
                'options': ['A) Real estate', 'B) Cryptocurrency', 'C) Bonds', 'D) Commodities'],
                'solution': 'C) Bonds',
                'explanation': {
                    'A) Real estate': '🏠 Variable! Real estate can fluctuate greatly in value.',
                    'B) Cryptocurrency': '🎢 Wild ride! Crypto is anything but predictable.',
                    'C) Bonds': '💵 Steady as she goes! Bonds typically offer fixed returns.',
                    'D) Commodities': '📊 Prices swing! Commodities are subject to market fluctuations.'
                }
            },
            {
                "questionId": "15",
                'question_text': "How can diversification help your investment portfolio?",
                'options': ['A) Increases risk', 'B) Decreases risk', 'C) No impact',
                            'D) Only beneficial in short term'],
                'solution': 'B) Decreases risk',
                'explanation': {
                    'A) Increases risk': '🚫 Not quite! Diversification is about spreading risk.',
                    'B) Decreases risk': '🛡️ Risk spreader! Diversifying can protect against losses in any one area.',
                    'C) No impact': '⚖️ Incorrect! Diversification aims to balance and mitigate risks.',
                    'D) Only beneficial in short term': '📅 Misconception! It’s a long-term safety strategy.'
                }
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


@app.route('/submit_answer/<question_id>', methods=['POST'])
def submit_answer(question_id):
    quiz_name = request.form['quizName']
    print(quiz_name)
    selected_option = request.form['selectedOption']
    print(selected_option)
    quiz = quiz_content.get(quiz_name)
    print(quiz)

    if not quiz:
        return jsonify({"error": "Quiz not found"}), 404

    question = next((q for q in quiz['questions'] if q['id'] == question_id), None)
    if question:
        correct = selected_option == question['solution']
        # Update the score logic here, for example using session or database
        return jsonify(correct=correct), 200
    else:
        return jsonify({"error": "Question not found"}), 404


@app.route('/results')
def results():
    user_score = sum(score.values()) / len(score.keys()) * 100
    return render_template('results.html', results=score, score=user_score, score_class=score_to_class)


if __name__ == '__main__':
    app.run(debug=True)
