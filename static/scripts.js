$(document).ready(function() {
    // Handle submissions for scored quizzes
    $('#quizForm').on('submit', function(e) {
        e.preventDefault();  // Prevent default form submission behavior
        var formData = $(this).serialize();  // Serialize the form data for sending
        var actionUrl = $(this).attr('action');  // Get the action URL from the form attribute

        $.ajax({
            type: "POST",
            url: actionUrl,
            data: formData,
            success: function(response) {
                alert('Your answer has been submitted successfully!');
                console.log('Response:', response);
                // Optionally update UI or transition to another page
            },
            error: function(xhr, status, error) {
                alert('Error submitting your answer. Please try again.');
                console.error('Error:', xhr.responseText);
            }
        });
    });

    // Handle submissions for pop quizzes
    $('#popQuizForm').submit(function(e) {
        e.preventDefault();  // Prevent default form submission behavior
        var formData = $(this).serialize();  // Serialize the form data for sending
        var actionUrl = $(this).attr('action');  // Get the action URL from the form attribute

        $.ajax({
            type: "POST",
            url: actionUrl,
            data: formData,
            success: function(response) {
                $('#explanation').text(response.explanation);  // Display the explanation in the 'explanation' element
                alert('Your response has been recorded!');
            },
            error: function(xhr) {
                alert('Error submitting your response. Please try again.');
                console.error('Error:', xhr.responseText);
            }
        });
    });
});
function checkAnswer(selectedOption, correctOption, element, isPopQuiz, questionId) {
    const parent = element.parentNode;
    const feedbackElement = parent.nextElementSibling; // Assumes feedback div follows the options div

    console.log(element.getAttribute('data-explanation')); // Debug: Log the explanation attribute

    /*element.style.backgroundColor = 'lightblue'; // Highlight the selected option*/


    // Display explanation for both correct and incorrect answers in pop quizzes
    if (isPopQuiz === 'true') {
        feedbackElement.innerHTML = element.getAttribute('data-explanation');
        feedbackElement.style.color = 'dodgerblue'
    } else {
        if (selectedOption === correctOption) {
            feedbackElement.innerHTML = 'Correct! ' + element.getAttribute('data-explanation');
            feedbackElement.style.color = 'green'


            console.log(questionId)

            $.ajax({
            type: "POST",
            url: '/submit_answer/' + questionId, // Suggest changing URL to reflect score updating
            data: {
                quizName: '{{ content.title }}',
                questionId: questionId, // Passing question ID to server
                correct: true // Indicating this was a correct answer
            },
            success: function(response) {
                // Update the score display based on server response
                console.log("sent to backend")
                updateScoreDisplay(response.updatedScore);
            },
            error: function(xhr) {
                console.error('Error:', xhr.responseText);
                feedbackElement.innerHTML = 'Error updating score. Please try again.';
                feedbackElement.style.color = 'red';
            }
        });
        } else {
            feedbackElement.innerHTML = 'Not correct: ' + element.getAttribute('data-explanation');
            feedbackElement.style.color = 'red'
        }
    }

    // Disable all options after one is selected to prevent multiple selections
    Array.from(parent.children).forEach(child => {
        if (child.tagName === 'BUTTON') {  // Ensure only buttons are disabled
            child.disabled = true;
        }
    });
}
