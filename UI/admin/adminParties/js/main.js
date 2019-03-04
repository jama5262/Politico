window.onload = () => {
  let partyHolder = document.getElementsByClassName("party-table-holder")[0];
  let tableBody = document.getElementsByTagName("tbody")[0];
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
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    populate(data) {
      let result = "";
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
              <div id="actions" style="display: flex">
                <a href="./editParty.html?partyID=${ data[i].id }"><button class="button-design-edit">edit</button></a>
                <button id="${ data[i].id }" class="button-design-delete">delete</button>
              </div>
            </td>
          </tr>
        `
        result = result + tableRow;
      }
      tableBody.insertAdjacentHTML('beforebegin', result);
    }
    async createParty() {
      try {
        this.main().loading()
        let fetchInstance = new Fetch("/parties", "POST", {
          name: this.name.value,
          abbr: this.abbr.value,
          logo_url: this.logoUrl.value,
          hq_address: this.hqAddress.value
        });
        let data = await fetchInstance.performFetch();
        this.main().alertInstance(data.data.msg);
        this.main().loading(false);
      } catch (error) {
        if (error != null && (error == "Your session has expired" || error == "No access token")) {
          await this.main().alertInstance(error + ", please login to continue", true);
          this.main().adminNavInstance().logout();
        }
        this.errorMessageFunc(error.error || "An error occured, please try again later", "block");
        this.main().loading(false)
      }
    }
    async editParty() {
      try {
        let partyID = new URL(window.location.href).searchParams.get("partyID");
        this.main().loading()
        let fetchInstance = new Fetch(`/parties/${ partyID }`, "PATCH", {
          name: this.name.value,
          abbr: this.abbr.value,
          logo_url: this.logoUrl.value,
          hq_address: this.hqAddress.value
        });
        let data = await fetchInstance.performFetch();
        this.main().alertInstance(data.data.msg);
        this.main().loading(false);
      } catch (error) {
        if (error != null && (error == "Your session has expired" || error == "No access token")) {
          await this.main().alertInstance(error + ", please login to continue", true);
          this.main().adminNavInstance().logout();
        }
        this.errorMessageFunc(error.error || "An error occured, please try again later", "block");
        this.main().loading(false)
      }
    }
    async deleteParty(partyID) {
      try {
        this.main().loading();
        let fetchInstance = new Fetch(`/parties/${ partyID }`, "DELETE");
        await fetchInstance.performFetch();
        this.main().loading(false);
        document.getElementsByTagName("tbody")[0].remove()
        this.getAllParites();
      } catch (error) {
        this.main().alertInstance(error.error || "An error occured, please try again later", true);
        this.main().loading(false);
      }
    }
    async getSpecificParty(partyID) {
      return new Promise(async (resolve, reject) => {
        try {
          this.main().loading();
          let fetchInstance = new Fetch(`/parties/${ partyID }`);
          let party = await fetchInstance.performFetch();
          resolve(party.data.data[0]);
          this.main().loading(false);
        } catch (error) {
          console.log(error.error || error.message);
          reject(error.error)
          this.main().alertInstance(error.error || "An error occured, please try again later", true);
          if (error.error != null && (error.error == "Your session has expired" || error.error == "No access token")) {
            await this.main().alertInstance(error + ", please login to continue", true);
            this.main().navInstance().logout();
          }
          this.main().loading(false);
        }
      });
    }
    async populatePartyToInput() {
      try {
        let partyID = new URL(window.location.href).searchParams.get("partyID");
        let party = await partiesInstance.getSpecificParty(partyID)
        this.name.value = party.name;
        this.abbr.value = party.abbr;
        this.logoUrl.value = party.logo_url;
        this.hqAddress.value = party.hq_address;
      } catch (error) {
        // this.main().alertInstance(error + ", please login to continue", true);
      }
    }
    async getAllParites() {
      try {
        this.main().loading()
        let fetchInstance = new Fetch("/parties");
        let data = await fetchInstance.performFetch();
        this.main().alertInstance(data.data.msg);
        this.populate(data.data.data);
        this.main().loading(false);
      } catch (error) {
        console.log(error);
        if (error != null && (error == "Your session has expired" || error == "No access token")) {
          await this.main().alertInstance(error + ", please login to continue", true);
          this.main().navInstance().logout();
        }
        this.main().loading(false);
      }
    }
  }

  let partiesInstance = new AdminParties();
  partiesInstance.main().adminNavInstance("index.html", "../adminGovOffices/index.html", "../../index.html").showNav();

  let logout = document.getElementById("logout");
  logout.addEventListener("click", () => {
    partiesInstance.main().adminNavInstance().logout();
  })

  let createParty = document.getElementById("createParty");
  if (createParty != null) {
    createParty.addEventListener("click", () => {
      partiesInstance.createParty();
    });
  }

  let editParty = document.getElementById("editParty");
  if (editParty != null) {
    editParty.addEventListener("click", () => {
      partiesInstance.editParty();
    });
  }
  
  let tableEl = document.getElementsByClassName("party-table-holder")[0];
  if (tableEl != null) {
    tableEl.addEventListener("click", (event) => {
      if (event.target.attributes.id != null) {
        partiesInstance.deleteParty(event.target.attributes.id.nodeValue)
      }
    })
  }

  if (partyHolder != null) {
    partiesInstance.getAllParites();
  } else if (createParty != null) {
    
  } else {
    partiesInstance.populatePartyToInput();
  }

  let goBack = document.getElementById("goBack");
  if (goBack != null) {
    goBack.addEventListener("click", () => {
      window.history.back();
    });
  }
}