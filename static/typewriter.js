const descriptionText = "Auto-generate custom cover letters according to your resume and target job description. Tailor your cover letter to each requirement in the job description, and stand out from the crowd.";
const typewriterElement = document.getElementById("typewriter");
let i = 0;

// Function to start the typewriter effect with an initial delay
function startTypewriterWithDelay() {
    setTimeout(typeDescription, 800); // 800 ms initial delay
}


function typeDescription() {
    if (i < descriptionText.length) {
        typewriterElement.innerHTML += descriptionText.charAt(i);
        i++;
        setTimeout(typeDescription, 20); // Adjust the speed here in ms
    }
}

// typeDescription();


// Start the typewriter effect with the initial delay
startTypewriterWithDelay();