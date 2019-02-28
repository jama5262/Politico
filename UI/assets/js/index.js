window.onload = () => {
  let loginBtn = document.getElementById("loginBtn");
  loginBtn.addEventListener("click", () => {
    performFetch('/parties')
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.log(error);
    })
  })
}