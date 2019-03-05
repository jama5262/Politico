window.onload = () => {
  class AdminCandidates {
    constructor() {
      this.users = document.getElementById("user");
      this.parties = document.getElementById("party");
      this.offices = document.getElementById("office");
      this.errorMessage = document.getElementById("errorMessage");
    }
    errorMessageFunc(text, type) {
      this.errorMessage.style.display = type;
      this.errorMessage.innerHTML = text;
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    async registerCandidate() {
      try {
        this.errorMessageFunc("", "none");
        this.main().loading();
        let offices = parseInt(this.offices.options[this.offices.selectedIndex].value);
        let users = parseInt(this.users.options[this.users.selectedIndex].value);
        let parties = parseInt(this.parties.options[this.parties.selectedIndex].value);
        if (users == 0) {
          this.errorMessageFunc("Please select a user, in which you want to create a petition for", "block")
        } else if (parties == 0) {
          this.errorMessageFunc("Please select a party, in which you want to create a petition for", "block")
        } else if (offices == 0) {
          this.errorMessageFunc("Please select an office, in which you want to create a petition for", "block")
        } else {
          let data = await this.main().performFetch("/offices/register", "POST", {
          candidate: users,
          office: offices,
          party: parties,
        });
        this.main().alertInstance(data.data.msg);
        }
        this.main().loading(false);
      } catch (error) {
        this.main().alertInstance(error.error, true);
        this.main().loading(false);
      }
    }
    populateSelect(data) {
      for (var i = 0; i < data.users.length; i++) {
        let options = `
          <option value="${ data.users[i].id }">${ data.users[i].first_name} ${ data.users[i].last_name }</option>
        `
        this.users.insertAdjacentHTML('beforeend', options);
      }
      for (var i = 0; i < data.parties.length; i++) {
        let options = `
          <option value="${ data.parties[i].id }">${ data.parties[i].name }</option>
        `
        this.parties.insertAdjacentHTML('beforeend', options);
      }
      for (var i = 0; i < data.offices.length; i++) {
        let options = `
          <option value="${ data.offices[i].id }">${ data.offices[i].name }</option>
        `
        this.offices.insertAdjacentHTML('beforeend', options);
      }
    }
    async populate() {
      try {
        this.main().loading();
        let users = await this.getAllUsers();
        let parties = await this.getAllParites();
        let offices = await this.getAllOffices();
        this.populateSelect({
          users,
          parties,
          offices
        });
        this.main().loading(false);
      } catch (error) {
        console.log(error);
        if (error != null && (error == "Your session has expired" || error == "No access token")) {
          await this.main().alertInstance(error + ", please login to continue", true);
          this.main().navInstance().logout();
        }else {
          this.main().alertInstance(error, true);
        }
        this.main().loading(false);
      }
    }
    async getAllParites() {
      return new Promise(async (resolve, reject) => {
        try {
          let data = await this.main().performFetch("/parties");
          resolve(data.data.data);
        } catch (error) {
          console.log(error);
          reject(error.error);
        }
      });
    }
    async getAllOffices() {
      return new Promise(async (resolve, reject) => {
        try {
          let data = await this.main().performFetch("/offices");
          resolve(data.data.data)
        } catch (error) {
          console.log(error);
          reject(error.error)
        }
      });
    }
    async getAllUsers() {
      return new Promise(async (resolve, reject) => {
        try {
          let data = await this.main().performFetch("/user");
          resolve(data.data.data);
        } catch (error) {
          reject(error.error);
        }
      });
    }
  }

  let candidateInstance = new AdminCandidates();
  candidateInstance.main().adminNavInstance("index.html", "../adminGovOffices/index.html", "index.html", "../../index.html").showNav();

  candidateInstance.populate();

  let registerCandidate = document.getElementById("registerCandidate");
  registerCandidate.addEventListener("click", () => {
    candidateInstance.registerCandidate();
  })

  let logout = document.getElementById("logout");
  logout.addEventListener("click", () => {
    candidateInstance.main().adminNavInstance().logout();
  })

  let goBack = document.getElementById("goBack");
  if (goBack != null) {
    goBack.addEventListener("click", () => {
      window.history.back();
    });
  }
}