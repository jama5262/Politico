window.onload = () => {
  let goBack = document.getElementById("goBack");
  if (goBack != null) {
    goBack.addEventListener("click", () => {
      window.history.back();
    })
  }
}