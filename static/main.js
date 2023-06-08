// TODO variables
const translateForm = document.querySelector(".translateForm");

const inputSelect = document.querySelector("#inputLang");
const outputSelect = document.querySelector("#outputLang");
const shuffleBtn = document.querySelector(".suffleBtn");
console.log(shuffleBtn);

// TODO EventListener
translateForm.addEventListener("submit", (e) => {
  e.preventDefault();
});

shuffleBtn.addEventListener("click", () => {
  let inputSelect_value = inputSelect.value;
  let outputSelect_value = outputSelect.value;

  // console.log(inputSelect_value, outputSelect_value);

  inputSelect.value = outputSelect_value;
  outputSelect.value = inputSelect_value;
});
