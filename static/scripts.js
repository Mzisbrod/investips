$(document).ready(function() {
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
                // You can add any additional actions to perform on success here
            },
            error: function(xhr, status, error) {
                alert('Error submitting your answer. Please try again.');
                console.error('Error:', xhr.responseText);
            }
        });
    });
});
