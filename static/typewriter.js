const descriptionText = "Auto-generate custom cover letters according to your resume and target job description. Tailor your cover letter to each requirement in the job description, and stand out from the crowd.";
const typewriterElement = document.getElementById("typewriter");
let i = 0;

function typeDescription() {
    if (i < descriptionText.length) {
        typewriterElement.innerHTML += descriptionText.charAt(i);
        i++;
        setTimeout(typeDescription, 15); // Adjust the speed here (e.g., 50 milliseconds)
    }
}

typeDescription();
