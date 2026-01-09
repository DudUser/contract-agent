let currentMode = "single";

/* ---------- UI ---------- */

function showStatus(message, type) {
  const box = document.getElementById("statusBox");
  const text = document.getElementById("statusText");
  const spinner = document.getElementById("spinner");

  box.className = "status-box " + type;
  text.innerText = message;

  spinner.style.display = type === "loading" ? "block" : "none";
  box.style.display = "block";
}


function hideStatus() {
  document.getElementById("statusBox").classList.add("hidden");
}

function showResult(text) {
  document.getElementById("resultText").textContent = text;
  document.getElementById("resultContainer").classList.remove("hidden");
}

function clearResult() {
  document.getElementById("resultContainer").classList.add("hidden");
  hideStatus();
}

/* ---------- MODE SWITCH ---------- */

function setMode(mode) {
  if (mode === currentMode) return;

  currentMode = mode;

  const singleBox = document.getElementById("singleBox");
  const compareBox = document.getElementById("compareBox");

  document.getElementById("btnSingle").classList.toggle("active", mode === "single");
  document.getElementById("btnCompare").classList.toggle("active", mode === "compare");

  singleBox.classList.toggle("hidden", mode !== "single");
  compareBox.classList.toggle("hidden", mode !== "compare");

  clearResult();
}

/* ---------- API ---------- */

async function analyzeSingle() {
  const file = document.getElementById("singleFile").files[0];
  if (!file) {
    showStatus("❌ Selecione um contrato.");
    return;
  }

  showStatus("⏳ Analisando contrato...");

  const data = new FormData();
  data.append("file", file);

  try {
    const res = await fetch("http://localhost:8000/contracts/upload", {
      method: "POST",
      body: data
    });

    const json = await res.json();
    showResult(json.summary);
    showStatus("✅ Resumo gerado com sucesso.");

  } catch {
    showStatus("⚠️ Erro ao analisar contrato.");
  }
}

async function compareContracts() {
  const a = document.getElementById("fileA").files[0];
  const b = document.getElementById("fileB").files[0];

  if (!a || !b) {
    showStatus("❌ Selecione os dois contratos.");
    return;
  }

  showStatus("⏳ Comparando contratos...");

  const data = new FormData();
  data.append("file_a", a);
  data.append("file_b", b);

  try {
    const res = await fetch("http://localhost:8000/contracts/compare", {
      method: "POST",
      body: data
    });

    const json = await res.json();
    showResult(json.comparison);
    showStatus("✅ Comparação concluída.");

  } catch {
    showStatus("⚠️ Erro ao comparar contratos.");
  }
}