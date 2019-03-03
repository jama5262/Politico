window.onload = () => {
  let navInstance = new AdminNavigation("index.html", "../adminGovOffices/index.html", "../../index.html");
  let partyHolder = document.getElementsByClassName("party-table-holder")[0];
  class AdminParties {
    constructor() {
      this.name = document.getElementById("pName");
      this.abbr = document.getElementById("abb");
      this.logoUrl = document.getElementById("logUrl");
      this.hqAddress = document.getElementById("hq");
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
    setNav() {
      navInstance.showNav();
    }
    logout() {
      navInstance.logout();
    }
    populate(data) {
      let tableBody = document.getElementsByTagName("tbody")[0];
      for (var i = 0; i < data.length; i++) {
        let tableRow = `
          <tr>
            <td>
              <div style="background-image: url('${ data[i].logo_url }');" class="party-image-index"></div>
            </td>
            <td>${ data[i].name }</td>
            <td>${ data[i].abbr }</td>
            <td>${ data[i].hq_address }</td>
            <td>
              <div style="display: flex">
                <a href="./editParty.html"><button class="button-design-edit">edit</button></a>
                <button class="button-design-delete">delete</button>
              </div>
            </td>
          </tr>
        `
        tableBody.insertAdjacentHTML('beforeend', tableRow);
      }
    }
    async createParty() {
      try {
        this.loading()
        let fetchInstance = new Fetch("/parties", "POST", {
          name: this.name.value,
          abbr: this.abbr.value,
          logo_url: this.logoUrl.value,
          hq_address: this.hqAddress.value
        });
        let data = await fetchInstance.performFetch();
        let alertInstance = new Alert(data.data.msg);
        alertInstance.showAlertMessage();
        this.loading(false);
      } catch (error) {
        if (error != null && (error == "Your session has expired" || error == "No access token")) {
          let alertInstance = new Alert(error + ", please login to continue", true);
          await alertInstance.showAlertMessage();
          this.logout();
        }
        this.errorMessageFunc(error.error || "An error occured, please try again later", "block");
        this.loading(false)
      }
    }
    async getAllParites() {
      try {
        this.loading()
        let fetchInstance = new Fetch("/parties");
        let data = await fetchInstance.performFetch();
        let alertInstance = new Alert(data.data.msg);
        alertInstance.showAlertMessage();
        console.log(data.data.msg);
        this.populate(data.data.data);
        this.loading(false);
      } catch (error) {
        console.log(error);
        if (error == "No access token") {
          let alertInstance = new Alert(error + ", please login to continue", true);
          await alertInstance.showAlertMessage();
          this.logout();
        }
        this.loading(false);
      }
    }
  }

  let partiesInstance = new AdminParties();
  partiesInstance.setNav();

  if (partyHolder != null) {
    partiesInstance.getAllParites();
  }

  let logout = document.getElementById("logout");
  logout.addEventListener("click", () => {
    partiesInstance.logout();
  })

  let createParty = document.getElementById("createParty");
  if (createParty != null) {
    createParty.addEventListener("click", () => {
      partiesInstance.createParty();
    });
  }

  let goBack = document.getElementById("goBack");
  if (goBack != null) {
    goBack.addEventListener("click", () => {
      window.history.back();
    });
  }
}