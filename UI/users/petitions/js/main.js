window.onload = () => {
  let petitionHodler = document.getElementsByClassName("petition-table-holder")[0];
  let tableBody = document.getElementsByTagName("tbody")[0];
  class Petitions {
    constructor() {
      this.text = document.getElementById("text");
      this.selectEl = document.getElementsByTagName("select")[0];
      this.errorMessage = document.getElementById("errorMessage");
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    errorMessageFunc(text, type) {
      this.errorMessage.style.display = type;
      this.errorMessage.innerHTML = text;
    }
    populate(data) {
      let result = "";
      for (var i = 0; i < data.length; i++) {
        let tableRow = `
          <tr>
            <td>${ data[i].created_on }</td>
            <td>${ data[i].metaData.user }</td>
            <td>${ data[i].metaData.office }</td>
            <td>${ data[i].text }</td>
          </tr>
        `
        result = result + tableRow;
      }
      tableBody.insertAdjacentHTML('afterbegin', result);
    }
    populatePetition(data) {
      return  new Promise(async (resolve, reject) => {
        try {
          for (var i = 0; i < data.length; i++) {
            let user = await this.main().performFetch(`/user/${ data[i].created_by }`);
            let office = await this.main().performFetch(`/offices/${ data[i].office }`);
            data[i]["metaData"] = {
              user: user.data.data[0].first_name + " " + user.data.data[0].last_name,
              office: office.data.data[0].name
            }
          }
          resolve(data);
        } catch (error) {
          reject(error);
        }
      });
    }
    async createPetition() {
      try {
        this.errorMessageFunc("", "none");
        this.main().loading();
        let user = await this.main().readFromDatabase();
        let office = parseInt(this.selectEl.options[this.selectEl.selectedIndex].value);
        if (office == 0) {
          this.errorMessageFunc("Please select an office, in which you want to create a petition for", "block")
        } else {
          let data = await this.main().performFetch("/petitions", "POST", {
          office: office,
          created_by: user.id,
          text: this.text.value,
        });
        this.main().alertInstance(data.data.msg);
        }
        this.main().loading(false);
      } catch (error) {
        this.errorMessageFunc(error.error, "block");
        this.main().loading(false);
      }
    }
    populateSelect(offices) {
      for (var i = 0; i < offices.length; i++) {
        let options = `
          <option value="${ offices[i].id }">${ offices[i].name }</option>
        `
        this.selectEl.insertAdjacentHTML('beforeend', options);
      }
    }
    async getAllOffices() {
      try {
        this.main().loading();
        let data = await this.main().performFetch("/offices");
        this.populateSelect(data.data.data);
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
    async getAllPetitions() {
      try {
        this.main().loading();
        let data = await this.main().performFetch("/petitions");
        this.main().alertInstance("Please wait, getting all petitions");
        let result = await this.populatePetition(data.data.data);
        this.main().alertInstance(data.data.msg);
        this.populate(result);
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

  (async () => {
    let petitionInstance = new Petitions();
    let profile_image = await petitionInstance.main().readFromDatabase();
    petitionInstance.main().navInstance("../parties/index.html", "index.html", "../results/index.html", profile_image.url, "../vote/index.html", "../myVotes/index.html", "../../index.html").showNav();
  
    if (petitionHodler != null) {
      petitionInstance.getAllPetitions();
    } else {
      petitionInstance.getAllOffices();
    }
  
    let createPetition = document.getElementById("createPetition");
    if (createPetition != null) {
      createPetition.addEventListener("click", () => {
        petitionInstance.createPetition();
      });
    }
  
    let logout = document.getElementById("logout");
    logout.addEventListener("click", () => {
      petitionInstance.main().navInstance().logout();
    });
  
    let goBack = document.getElementById("goBack");
    if (goBack != null) {
      goBack.addEventListener("click", () => {
        window.history.back();
      });
    }
  })()
}