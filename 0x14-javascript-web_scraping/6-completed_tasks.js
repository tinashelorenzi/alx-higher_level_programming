// 6-completed_tasks.js

const request = require('request');

// Function to compute the number of completed tasks for each user
function countCompletedTasks(apiUrl) {
  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    // Create an object to store the counts for each user
    const completedTasksCount = {};

    // Loop through the tasks and count the completed ones for each user
    for (const task of body) {
      if (task.completed) {
        if (completedTasksCount[task.userId]) {
          completedTasksCount[task.userId]++;
        } else {
          completedTasksCount[task.userId] = 1;
        }
      }
    }

    console.log(completedTasksCount);
  });
}

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Call the function to compute and print the completed tasks count
countCompletedTasks(apiUrl);
