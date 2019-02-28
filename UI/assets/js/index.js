window.onload = () => {
  let loginBtn = document.getElementById("loginBtn");
  let email = document.getElementById("emailLogin");
  let password = document.getElementById("passwordLogin");
  errorMessage = document.getElementById("errorMessage");

  let errorMessageFunc = (text, type) => {
    errorMessage.style.display = type;
    errorMessage.innerHTML = text;
  }

  loginBtn.addEventListener("click", () => {
    errorMessageFunc("", "none");
    userData = {
      email: email.value,
      password: password.value
    }
    performFetch('/auth/login', "POST", userData, false)
    .then((data) => {
      if (data.status == 200) {
        console.log(data);
        return writeToDatabase({
          user: "1",
          token: data.data.token
        });
      } else {
        errorMessageFunc(data.error, "unset");
      }
    })
    .then((data) => {
      if (data != null) {
        window.open("../../../UI/users/parties/index.html", "_self")
      } else {
        console.log("Authentication error")
      }
    })
    .catch((error) => {
      console.log(error);
    })
  });
}