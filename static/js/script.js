// This file contains the JavaScript code for the AJAX request to the server
$(document).ready(function() {
  // AJAX function to handle clicking on the "View Recipe" button
  $(".recipe-button").click(function(e) {
    e.preventDefault(); // Prevent the default behavior of the button
    var index = $(this).data('index'); // Get the index from the button's data attribute

    $.ajax({
      url: '/next-page', // URL of the next page
      type: 'GET',
      data: {'index': index}, // Pass the index as a parameter
      success: function(response) {
        // Handle the success response from the server, if needed
        console.log("Index sent successfully!");
        // Redirect to the next page if needed
        window.location.href = '/next-page?index=' + index;
      },
      error: function(xhr, errmsg, err) {
        // Handle errors, if any
        console.log("Error occurred!");
      }
    });
  });
});