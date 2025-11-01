document.getElementById("detectBtn").addEventListener("click", async () => {
  const text = document.getElementById("userText").value.trim();
  const resultDiv = document.getElementById("result");
  const emotionText = document.getElementById("emotionText");
  const emojiDisplay = document.getElementById("emojiDisplay");

  if (!text) {
    alert("Please enter a sentence!");
    return;
  }

  emotionText.textContent = "Detecting...";
  emojiDisplay.textContent = "🤔";
  resultDiv.classList.remove("hidden");

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();

    if (data.error) {
      emotionText.textContent = data.error;
      emojiDisplay.textContent = "⚠️";
      return;
    }

    // Extract emotion (e.g. "Anger (0.97)")
    const emotionLabel = data.emotion.split(" ")[0].toLowerCase();

    let emoji = "😐";
    switch (emotionLabel) {
      case "joy":
        emoji = "😄";
        break;
      case "sadness":
        emoji = "😢";
        break;
      case "anger":
        emoji = "😠";
        break;
      case "fear":
        emoji = "😨";
        break;
      case "surprise":
        emoji = "😲";
        break;
      case "love":
        emoji = "🥰";
        break;
      default:
        emoji = "😐";
    }

    emotionText.textContent = data.emotion;
    emojiDisplay.textContent = emoji;
  } catch (error) {
    console.error("Error:", error);
    emotionText.textContent = "Error connecting to server!";
    emojiDisplay.textContent = "⚠️";
  }
});
