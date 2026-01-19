document.getElementById("analyzeBtn").onclick = async () => {
  const fileInput = document.getElementById("referenceVideo");
  if (!fileInput.files.length) {
    alert("Upload a reference video");
    return;
  }

  const formData = new FormData();
  formData.append("reference", fileInput.files[0]);

  document.getElementById("output").innerText = "Analyzing...";

  const res = await fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("output").innerText = data.feedback;
};
