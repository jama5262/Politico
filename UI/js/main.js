window.onload = () => {
  let goBack = document.getElementById("goBack");
  goBack.addEventListener("click", () => {
    window.history.back();
  })
}