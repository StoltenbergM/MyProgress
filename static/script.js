function incrementProgress(goalId) {
    // Send an AJAX request to your Flask server to increment the progress of the goal with the given ID
    // You can use libraries like jQuery for AJAX requests or native JavaScript methods like fetch
    fetch(`/increment_progress/${goalId}`, {
        method: 'POST'
    })
    .then(response => {
        // Handle the response if needed
        console.log('Increment progress successful');
    })
    .catch(error => {
        // Handle any errors
        console.error('Error incrementing progress:', error);
    });
}

function decrementProgress(goalId) {
    // Send an AJAX request to your Flask server to decrement the progress of the goal with the given ID
    fetch(`/decrement_progress/${goalId}`, {
        method: 'POST'
    })
    .then(response => {
        // Handle the response if needed
        console.log('Decrement progress successful');
    })
    .catch(error => {
        // Handle any errors
        console.error('Error decrementing progress:', error);
    });
}
