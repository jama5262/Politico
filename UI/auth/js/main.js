window.onload = () => {
  let signupBtn = document.getElementById("signupBtn");
  let errorMessage = document.getElementById("errorMessage");
  let fName = document.getElementById("fNameSignUp");
  let lName = document.getElementById("lNameSignUp");
  let oName = document.getElementById("oNameSignUp");
  let email = document.getElementById("emailSignUp");
  let password = document.getElementById("passwordSignUp");
  let phoneNumber = document.getElementById("phoneSignUp");
  let passport = document.getElementById("pportSignUp");

  let errorMessageFunc = (text, type) => {
    errorMessage.style.display = type;
    errorMessage.innerHTML = text;
  }

  signupBtn.addEventListener("click", () => {
    errorMessageFunc("", "none");
    userData = {
      first_name: fName.value,
      last_name: lName.value,
      email: email.value,
      password: password.value,
      other_name: oName.value,
      passport_url: passport.value,
      phone_number: phoneNumber.value
    }

    performFetch("/auth/signup", "POST", userData, false)
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
        window.location.href = document.getElementById("successSignup").getAttribute("href");
      } else {
        console.log("Authentication error")
      }
    })
    .catch((error) => {
      console.log(error);
    })
  });

  let goBack = document.getElementById("goBack");
  goBack.addEventListener("click", () => {
    window.history.back();
  });  
}