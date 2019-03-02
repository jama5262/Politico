window.onload = () => {
  let signupBtn = document.getElementById("signupBtn");
  let goBack = document.getElementById("goBack");
  class SignUp {
    constructor() {
      this.errorMessage = document.getElementById("errorMessage");
      this.fName = document.getElementById("fNameSignUp");
      this.lName = document.getElementById("lNameSignUp");
      this.oName = document.getElementById("oNameSignUp");
      this.email = document.getElementById("emailSignUp");
      this.password = document.getElementById("passwordSignUp");
      this.phoneNumber = document.getElementById("phoneSignUp");
      this.passport = document.getElementById("pportSignUp");
    }
    errorMessageFunc(text, type) {
      this.errorMessage.style.display = type;
      this.errorMessage.innerHTML = text;
    }
    loading(load) {
      let instance = new Loading();
      if (load) {
        instance.showLoading();
      } else {
        instance.dismissAlert()
      }
    }
    async signup() {
      this.loading(true);
      this.errorMessageFunc("", "none");
      try {
        let fetchInstance = new Fetch('/auth/signup', "POST", {
          first_name: this.fName.value,
          last_name: this.lName.value,
          email: this.email.value,
          password: this.password.value,
          other_name: this.oName.value,
          passport_url: this.passport.value,
          phone_number: this.phoneNumber.value
        }, false)
        let data = await fetchInstance.performFetch();
        let dbInstance = new Indexeddb();
        await dbInstance.writeToDatabase({
          "user": "1",
          token: data.data.token
        });
        this.loading(false);
        window.location.href = document.getElementById("successSignup").getAttribute("href");
      } catch (error) {
        console.log(error);
        this.errorMessageFunc(error.error || "An error occured, please try again later", "block");
        this.loading(false)
      }
    }
  }

  signupBtn.addEventListener("click", () => {
    let instance = new SignUp();
    instance.signup();
  });

  goBack.addEventListener("click", () => {
    window.history.back();
  })
}