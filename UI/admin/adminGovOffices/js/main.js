window.onload = () => {
  let officeHolder = document.getElementsByClassName("office-table-holder")[0];
  let tableBody = document.getElementsByTagName("tbody")[0];
  class AdminOffices {
    constructor() {
      this.name = document.getElementById("name");
      this.type = document.getElementById("type");
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
            <td>${ data[i].name }</td>
            <td>${ data[i].type }</td>
            <td>
              <div style="display: flex">
                <a href="./editOffice.html?officeID=${ data[i].id }"><button class="button-design-edit">edit</button></a>
                <button id="${ data[i].id }" class="button-design-delete">delete</button>
              </div>
            </td>
          </tr>
        `
        result = result + tableRow;
      }
      tableBody.insertAdjacentHTML('afterbegin', result);
    }
    async createOffice() {
      this.errorMessageFunc("", "none");
      try {
        this.main().loading();
        let data = await this.main().performFetch("/offices", "POST", {
          name: this.name.value,
          type: this.type.value
        });
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
    async editOffice() {
      try {
        let officeID = new URL(window.location.href).searchParams.get("officeID");
        this.main().loading();
        let data = await this.main().performFetch(`/offices/${ officeID }`, "PATCH", {
          name: this.name.value,
          type: this.type.value
        });
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
    async deleteOffice(officeID) {
      try {
        this.main().loading();
        let data = await this.main().performFetch(`/offices/${ officeID }`, "DELETE");
        console.log(data);
        this.main().loading(false);
        location.reload();
      } catch (error) {
        this.main().alertInstance(error.error || "An error occured, please try again later", true);
        this.main().loading(false);
      }
    }
    async getSpecificOffice(partyID) {
      return new Promise(async (resolve, reject) => {
        try {
          this.main().loading();
          let office = await this.main().performFetch(`/offices/${ partyID }`);
          resolve(office.data.data[0]);
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
    async populateOfficeToInput() {
      try {
        let officeID = new URL(window.location.href).searchParams.get("officeID");
        let office = await officesInstance.getSpecificOffice(officeID)
        this.name.value = office.name;
        this.type.value = office.type;
      } catch (error) {
        // this.main().alertInstance(error + ", please login to continue", true);
      }
    }
    async getAllOffices() {
      try {
        this.main().loading();
        let data = await this.main().performFetch("/offices");
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

  let officesInstance = new AdminOffices();
  officesInstance.main().adminNavInstance("../adminParties/index.html", "../adminGovOffices/index.html", "../../index.html").showNav();

  let logout = document.getElementById("logout");
  logout.addEventListener("click", () => {
    officesInstance.main().adminNavInstance().logout();
  })

  let createOffice = document.getElementById("createOffice");
  if (createOffice != null) {
    createOffice.addEventListener("click", () => {
      officesInstance.createOffice();
    });
  }

  let editOffice = document.getElementById("editOffice");
  if (editOffice != null) {
    editOffice.addEventListener("click", () => {
      officesInstance.editOffice();
    });
  }
  
  let tableEl = document.getElementsByClassName("office-table-holder")[0];
  if (tableEl != null) {
    tableEl.addEventListener("click", (event) => {
      if (event.target.attributes.id != null) {
        officesInstance.deleteOffice(event.target.attributes.id.nodeValue)
      }
    })
  }

  if (officeHolder != null) {
    officesInstance.getAllOffices();
  } else if (createOffice != null) {
    
  } else {
    console.log("editing");
    officesInstance.populateOfficeToInput();
  }

  let goBack = document.getElementById("goBack");
  if (goBack != null) {
    goBack.addEventListener("click", () => {
      window.history.back();
    });
  }
}