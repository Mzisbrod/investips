
console.log("HELLO! class_quiz.js");


function updateQuizScore(quizName) {
    $.ajax({
        type: "POST",
        url: "/update_quiz_score",
        data: JSON.stringify({ quiz_name: quizName, new_score: 1 }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(response) {
            if(response.success) {
                alert("Score updated successfully!");
            } else {
                alert("Failed to update score.");
            }
        },
        error: function(err) {
            console.log(err);
        }
    });
}