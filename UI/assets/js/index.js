window.onload = () => {
  let loginBtn = document.getElementById("loginBtn");
  loginBtn.addEventListener("click", () => {
    performFetch('/parties');
  })
}