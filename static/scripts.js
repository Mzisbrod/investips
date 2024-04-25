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
