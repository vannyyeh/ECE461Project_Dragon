// set the innerHTML of the span element to the stored name
let storedUsername = localStorage.getItem('username');
document.getElementById('username').innerHTML = storedUsername;


function storeName() {
        // get the value of the input element
        let usernameInput = document.getElementById('username-input').value;

        // store the value in localStorage
        localStorage.setItem('username', usernameInput);
      }

function checkInput() {
        let nameInput1 = document.getElementById('username-input').value;
        let nameInput2 = document.getElementById('password-input').value;
        let errorMessage1 = document.getElementById('username-error-message');
        let errorMessage2 = document.getElementById('password-error-message');

        // check if the input is valid
        if (nameInput1.trim() === '') {
          // display the error message
          errorMessage1.style.display = 'block';

        }
        else if (nameInput2.trim() === '') {
          // display the error message
          errorMessage2.style.display = 'block';

        }
        else {
          // hide the error message
          errorMessage1.style.display = 'none';
          errorMessage2.style.display = 'none';
          // navigate to the next page
          window.location.href = 'userPortal.html';
        }
      }

