window.onload = () => {
  let petitionHodler = document.getElementsByClassName("petition-table-holder")[0];
  let tableBody = document.getElementsByTagName("tbody")[0];
  class Petitions {
    main() {
      let mainInstance = new Main();
      return mainInstance;
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
    async getAllPetitions() {
      try {
        this.main().loading();
        let data = await this.main().performFetch("/petitions");
        this.main().alertInstance(data.data.msg);
        let result = await this.populatePetition(data.data.data);
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

  let petitionInstance = new Petitions();
  petitionInstance.main().navInstance("../parties/index.html", "index.html", "index.html", "../../assets/images/profile_image.jpg", "../vote/index.html", "../myVotes/index.html", "../../index.html").showNav();

  if (petitionHodler != null) {
    petitionInstance.getAllPetitions();
  }

  let logout = document.getElementById("logout");
  logout.addEventListener("click", () => {
    petitionInstance.main().navInstance().logout();
  })
}