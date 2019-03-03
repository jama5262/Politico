window.onload = () => {
  let loginBtn = document.getElementById("loginBtn");

  class Login {
    constructor() {
      this.email = document.getElementById("emailLogin");
      this.password = document.getElementById("passwordLogin");
      this.errorMessage = document.getElementById("errorMessage");
    }
    errorMessageFunc(text, type) {
      this.errorMessage.style.display = type;
      this.errorMessage.innerHTML = text;
    }
    loading(load=true) {
      let alertInstance = new Loading();
      if (load) {
        alertInstance.showLoading();
      } else {
        alertInstance.dismissAlert()
      }
    }
    async login() {
      this.loading();
      this.errorMessageFunc("", "none");
      try {
        let fetchInstance = new Fetch('/auth/login', "POST", {
          email: this.email.value,
          password: this.password.value
        }, false)
        let data = await fetchInstance.performFetch();
        let dbInstance = new Indexeddb();
        await dbInstance.writeToDatabase({
          "user": "1",
          token: data.data.token
        });
        this.loading(false);
        if (data.data.user.is_admin) {
          window.location.href = document.getElementById("admin").getAttribute("href");
        } else {
          window.location.href = document.getElementById("user").getAttribute("href");
        }
      } catch (error) {
        console.log(error);
        this.errorMessageFunc(error.error || "An error occured, please try again later", "block");
        this.loading(false)
      }
    }
  }

  loginBtn.addEventListener("click", () => {
    let instance = new Login();
    instance.login();
  });
}