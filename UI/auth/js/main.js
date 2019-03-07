window.onload = () => {
  let signupBtn = document.getElementById("signupBtn");
  let resetBtn = document.getElementById("submit");
  let emaiEl = document.getElementById("email-container");
  let message = document.getElementById("message");
  let passwordEl = document.getElementById("password-container");
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
        await this.main().alertInstance("You will be redirected to the login page");
        window.location.href = document.getElementById("successSignup").getAttribute("href");
        this.main().loading(false);
      } catch (error) {
        console.log(error);
        this.errorMessageFunc(error.error || "An error occured, please try again later", "block");
        this.main().loading(false);
      }
    }
  }

  class Reset {
    constructor() {
      this.errorMessage = document.getElementById("errorMessage");
      this.email = document.getElementById("emailReset");
      this.newPassword = document.getElementById("nPassWordReset");
      this.confPassword = document.getElementById("rPassWordReset");
    }
    errorMessageFunc(text, type) {
      this.errorMessage.style.display = type;
      this.errorMessage.innerHTML = text;
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }    
    async resetEmail() {
      try {
        this.main().loading();
        this.errorMessageFunc("", "none");
        let user = await this.main().performFetch(`/auth/${ this.email.value }`, "GET", {}, false)
        this.main().alertInstance(`${ user.data.msg } to ${ user.data.data.email }, IF YOU CAN'T FIND IT PLEASE CHECK YOUR SPAM FOLDER`);
        this.errorMessageFunc(`Password reset link sent to your email, ${ user.data.data.email }, if you can find it please check you spam folder`, "block");
        this.main().loading(false);
      } catch (error) {
        this.main().loading(false);
        console.log(error);
        this.errorMessageFunc(error.error, "block");
      }
    }

    validate() {
      if (this.newPassword.value === "") {
        this.errorMessageFunc("Please fill in the details", "block")
        return false;
      }
      if (this.newPassword.value.length < 6) {
        this.errorMessageFunc("Your new password should be more than 6 characters", "block")
        return false;
      }
      if (this.newPassword.value != this.confPassword.value) {
        this.errorMessageFunc("Please make sure you passwords match", "block")
        return false;
      }
      return true;
    }
    
    async resetPassword(token, id) {
      try {
        this.errorMessageFunc("", "none");
        console.log("ok");
        if (this.validate()) {
          this.main().loading();
          this.errorMessageFunc("", "none");
          await this.main().writeToDatabase({
            user: "1",
            token: token
          });
          let user = await this.main().performFetch(`/auth/reset/${ id }`, "PATCH", {
            password: this.newPassword.value
          });
          await this.main().alertInstance(`${ user.data.msg }, you will be redirected to login page`);
          window.location.href = document.getElementById("user").getAttribute("href");
          this.main().loading(false);
        }
      } catch (error) {
        console.log(error.error || error.message);
        if (error.error != null && ((error.error == "Your session has expired" || error.error == "No access token") || error.error == "You have an invalid token, please login or signup to get a valid token")) {
          await this.main().alertInstance(error.error + ", please request for another reset link", true);
          window.location.href = document.getElementById("logoutUrl").getAttribute("href");
        } else {
          this.main().alertInstance(error.error || error.message, true);
        }
        this.main().loading(false);
      }
    }
  }

  (async () => {
    
    let resetInstance = new Reset();
    let signupInstance = new SignUp();

    if (signupBtn != null) {
      signupBtn.addEventListener("click", () => {
        signupInstance.signup();
      });
    }

    let token = new URL(window.location.href).searchParams.get("token");
    let id = new URL(window.location.href).searchParams.get("id");
    if (resetBtn != null) {
      if (token == null) {
        resetBtn.addEventListener("click", () => {
          resetInstance.resetEmail();
        });
        emaiEl.style.display = "flex";
        message.innerHTML = "Input your email to reset your password"
        goBack.addEventListener("click", () => {
          window.history.back();
        })
      } else {
        resetBtn.addEventListener("click", () => {
          resetInstance.resetPassword(token, id);
        });
        passwordEl.style.display = "flex";
        goBack.style.display = "none";
        message.innerHTML = "Reset you password"
      }
    }

  })()
}