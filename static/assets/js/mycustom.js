
/// Function to toggle the modal display
function toggleModal() {
    var modal = document.getElementById("regForm");
    if (modal.style.display === "block") {
        modal.style.display = "none";
    } else {
        modal.style.display = "block";
        showTab(currentTab);
    }
}

// Close the modal when the user clicks outside of it
window.onclick = function(event) {
    var modal = document.getElementById("regForm");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

    var currentTab = 0; // Current tab is set to be the first tab (0)

    function openModal() {
        var regForm = document.getElementById("regForm");
        regForm.style.display = "block"; // Display the form
        showTab(currentTab); // Show the current tab
    }

    function showTab(n) {
        // This function will display the specified tab of the form...
        var x = document.getElementsByClassName("tab");
        x[n].style.display = "block";
        //... and fix the Previous/Next buttons:
        if (n == 0) {
            document.getElementById("prevBtn").style.display = "none";
        } else {
            document.getElementById("prevBtn").style.display = "inline";
        }
        if (n == (x.length - 1)) {
            document.getElementById("nextBtn").innerHTML = "Submit";
        } else {
            document.getElementById("nextBtn").innerHTML = "Next";
        }
        //... and run a function that will display the correct step indicator:
        fixStepIndicator(n);
    }

    function nextPrev(n) {
        // This function will figure out which tab to display
        var x = document.getElementsByClassName("tab");
        // Exit the function if any field in the current tab is invalid:
        if (n == 1 && !validateForm()) return false;
        // Hide the current tab:
        x[currentTab].style.display = "none";
        // Increase or decrease the current tab by 1:
        currentTab = currentTab + n;
        // if you have reached the end of the form...
        if (currentTab >= x.length) {
            // ... the form gets submitted:
            document.getElementById("regForm").submit();
            return false;
        }
        // Otherwise, display the correct tab:
        showTab(currentTab);
    }

    function validateForm() {
        // This function deals with validation of the form fields
        var x, y, i, valid = true;
        x = document.getElementsByClassName("tab");
        y = x[currentTab].getElementsByTagName("input");
        // A loop that checks every input field in the current tab:
        for (i = 0; i < y.length; i++) {
            // If a field is empty...
            if (y[i].value == "") {
                // add an "invalid" class to the field:
                y[i].className += " invalid";
                // and set the current valid status to false
                valid = false;
            }
        }
        // If the valid status is true, mark the step as finished and valid:
        if (valid) {
            document.getElementsByClassName("step")[currentTab].className += " finish";
        }
        return valid; // return the valid status
    }

    function fixStepIndicator(n) {
        // This function removes the "active" class of all steps...
        var i, x = document.getElementsByClassName("step");
        for (i = 0; i < x.length; i++) {
            x[i].className = x[i].className.replace(" active", "");
        }
        //... and adds the "active" class on the current step:
        x[n].className += " active";
    }

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("openModalBtn");

// Get the <span> element that closes the modal
var span = document.querySelector(".custom-modal .close");

// When the user clicks the button, open the modal with fade-in effect
btn.onclick = function() {
  modal.style.display = "block";
  modal.classList.add("fade-in");
}

// When the user clicks on <span> (x), close the modal with fade-out effect
span.onclick = function() {
  modal.classList.remove("fade-in");
  modal.classList.add("fade-out");
  setTimeout(function() {
    modal.style.display = "none";
    modal.classList.remove("fade-out");
  }, 500); // Adjust the time to match the duration of the fade-out animation
}

// When the user clicks anywhere outside of the modal, close it with fade-out effect
window.onclick = function(event) {
  if (event.target == modal) {
    modal.classList.remove("fade-in");
    modal.classList.add("fade-out");
    setTimeout(function() {
      modal.style.display = "none";
      modal.classList.remove("fade-out");
    }, 500); // Adjust the time to match the duration of the fade-out animation
  }
}

function openAddressModal() {
    // Show the address modal
    document.getElementById("addressModal").style.display = "block";
}

function closeAddressModal() {
    // Hide the address modal
    document.getElementById("addressModal").style.display = "none";
}