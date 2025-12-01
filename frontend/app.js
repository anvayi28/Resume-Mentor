async function uploadFile() {
    const fileInput = document.getElementById("resumeFile");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload a resume file!");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    displayResult(data);
}

function displayResult(data) {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = `
        <div class="card">
            <h2>${data.predicted_career} (${data.confidence}%)</h2>
            <h3>Skills Found:</h3>
            <p class="found">${data.skills_found.join(", ")}</p>
            <h3>Missing Skills:</h3>
            <p class="missing">${data.missing_skills.join(", ")}</p>
            <h3>Recommendations:</h3>
            <ul>
                ${data.recommendations.map(r => `<li>${r}</li>`).join("")}
            </ul>
        </div>
    `;
}
