document.addEventListener("DOMContentLoaded", function () {
    // Get the button by its id
    const copyButton = document.getElementById("copyToClipboardButton");

    // Add an event listener to the button
    copyButton.addEventListener("click", function () {
        // Access the 'data-text' attribute to get the text
        const textToCopy = copyButton.getAttribute("data-text");

        // Create a temporary input element
        const tempInput = document.createElement("input");
        tempInput.value = textToCopy;
        document.body.appendChild(tempInput);

        // Select and copy the text inside the input element
        tempInput.select();
        document.execCommand("copy");

        // Remove the temporary input element
        document.body.removeChild(tempInput);

        alert("Cover Letter Copied to Clipboard");
    });
});
