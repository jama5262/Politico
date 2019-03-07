window.onload = () => {
  let signupBtn = document.getElementById("signupBtn");
  let resetBtn = document.getElementById("submit");
  let emaiEl = document.getElementById("email-container");
  let message = document.getElementById("message");
  let passwordEl = document.getElementById("password-container");
  let goBack = document.getElementById("goBack");

  console.log(emaiEl);
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
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    async signup() {
      this.main().loading();
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
        await fetchInstance.performFetch();
        this.main().loading(false);
        await this.main().alertInstance("You will be redirected to the login page");
        window.location.href = document.getElementById("successSignup").getAttribute("href");
      } catch (error) {
        console.log(error);
        this.errorMessageFunc(error.error || "An error occured, please try again later", "block");
        this.main().loading(false);
      }
    }

    async resetEmail() {
      try {
        this.main().loading();
        this.errorMessageFunc("", "none");
        let user = await this.main().performFetch(`/auth/${ this.email.value }`)
        this.main().alertInstance(`${ user.data.msg } to ${ user.data.data.email }`);
        this.main().loading(false);
      } catch (error) {
        this.main().loading(false);
        this.errorMessageFunc(error.error, "block");
      }
    }

    
    async resetPassword(token) {
      try {
        this.main().loading();
        this.errorMessageFunc("", "none");
        await this.main().writeToDatabase({
          token: token
        });
        
      } catch (error) {
        console.log(error.error || error.message);
        this.main().alertInstance(error.error, true);
        if (error.error != null && (error.error == "Your session has expired" || error.error == "No access token")) {
          await this.main().alertInstance(error + ", please request for another reset link", true);
          window.location.href = document.getElementById("logoutUrl").getAttribute("href");
        }
        this.main().loading(false);
      }
    }
  }

  if (signupBtn != null) {
    signupBtn.addEventListener("click", () => {
      let instance = new SignUp();
      instance.signup();
    });
  }

  if (resetBtn != null) {
    resetBtn.addEventListener("click", () => {
      let instance = new SignUp();
      instance.resetEmail();
    });
  }

  goBack.addEventListener("click", () => {
    window.history.back();
  })

  let token = new URL(window.location.href).searchParams.get("token");
  if (token == null) {
    emaiEl.style.display = "flex";
    message.innerHTML = "Input your email to reset your password"
  } else {
    passwordEl.style.display = "flex";
    message.innerHTML = "Reset you password"
  }
}