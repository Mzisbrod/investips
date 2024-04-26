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
function checkAnswer(selectedOption, correctOption, element, isPopQuiz) {
    const parent = element.parentNode;
    const feedbackElement = parent.nextElementSibling; // Assumes feedback div follows the options div

    if (isPopQuiz === 'true') {
        // Display the explanation regardless of the selected option
        element.style.backgroundColor = 'lightblue'; // Highlight the selected option
        feedbackElement.innerHTML = element.getAttribute('data-explanation');
    } else {
        // Standard quiz logic for non-pop quiz questions
        if (selectedOption === correctOption) {
            element.style.backgroundColor = 'lightgreen'; // Correct answer
            feedbackElement.innerHTML = 'Correct!';
        } else {
            element.style.backgroundColor = 'salmon'; // Incorrect answer
            feedbackElement.innerHTML = 'Not correct, learn why';
        }
    }

    // Disable all options after one is selected to prevent multiple selections
    Array.from(parent.children).forEach(child => {
        if (child.tagName === 'BUTTON') {  // Ensure only buttons are disabled
            child.disabled = true;
        }
    });
}
