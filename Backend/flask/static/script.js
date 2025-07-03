document.getElementById("submitButton").addEventListener("click", function() {
    const inputField = document.getElementById("inputField");
    const inputValue = inputField.value.trim();
    if (inputValue) {
        // Simulate a successful submission
        alert("Form submitted successfully with value: " + inputValue);
        inputField.value = ""; // Clear the input field
    } else {
        alert("Please enter a value before submitting.");
    }
});