window.onload = () => {
  class Results {
    constructor() {
      this.officeHolder = document.getElementsByClassName("main-container")[0];
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    populate(data) {
      this.main().alertInstance("Election results retrieved");
      for (var i = 0; i < data.length; i++) {
        let officeHolderHead = `
          <div class="gov-office-holder card-design">
            <div>
              <h2 class="text-color-design-primary">${ data[i].name }</h2>
            </div>
            <div class="candidate-holder-index">
        `
        let candidateHolderBody = "";
        let officeHolderTail = `
            </div>
          </div>
        `
        if (data[i].candidatesResults == "There are no votes for this office") {
          candidateHolderBody = `
          <div style="padding: 10px 0 20px 0;">
            ${ data[i].candidatesResults }
          </div>
          `
        } else {
          for (var j = 0; j < data[i].candidatesResults.length; j++) {
            let result = `
              <div class="candidate-index">
                <div style="background-image: url('${ data[i].candidatesResults[j].url }');" class="candidate-profile-image-index"></div>
                <div class="candidate-info-index">
                  <h4>${ data[i].candidatesResults[j].name }</h4>
                  <h3 style="margin-top: 10px;">${ data[i].candidatesResults[j].result } Votes</h3>
                </div>
              </div>        
            `
            candidateHolderBody = candidateHolderBody + result;
          }
        }
        this.officeHolder.insertAdjacentHTML('beforeend', officeHolderHead + candidateHolderBody + officeHolderTail);
      }
    }
    async generateData() {
      try {
        this.main().loading();
        this.main().alertInstance("Please wait, fetching all election results");
        let offices = await this.getAllOffices();
        for (var i = 0; i < offices.length; i++) {
          let officeResult = await this.getOfficeResult(offices[i].id);
          if (officeResult == "The office you are lookng for does not exist") {
            offices[i]["candidatesResults"] = "There are no votes for this office";
          } else {
            offices[i]["candidatesResults"] = officeResult.data;
            // console.log(officeResult.data);
            for (var j = 0; j < officeResult.data.length; j++) {
              let user =  await this.getUser(officeResult.data[j].candidate);
              offices[i]["candidatesResults"][j]["name"] = user[0].first_name + " " + user[0]
              .last_name
              offices[i]["candidatesResults"][j]["url"] = user[0].passport_url
            }
          }
        }
        console.log(offices);
        this.populate(offices);
        this.main().loading(false);
      } catch (error) {
        this.main().loading(false);
        console.log(error);
      }
    }
    getAllOffices() {
      return new Promise(async (resolve) => {
        try {
          let data = await this.main().performFetch("/offices");
          resolve(data.data.data)
        } catch (error) {
          resolve(error.error)
        }
      });
    }
    getOfficeResult(officeID) {
      return new Promise(async (resolve) => {
        try {
          let data = await this.main().performFetch(`/offices/${ officeID }/result`);
          resolve(data.data)
        } catch (error) {
          resolve(error.error)
        }
      });
    }
    getAllCandidates(officeID) {
      return new Promise(async (resolve) => {
        try {
          let data = await this.main().performFetch(`/user/candidate/office/${ officeID }`);
          resolve(data.data.data)
        } catch (error) {
          resolve(error.error)
        }
      });
    }
    getParty(partyID) {
      return new Promise(async (resolve, reject) => {
        try {
          let data = await this.main().performFetch(`/parties/${ partyID }`);
          resolve(data.data.data)
        } catch (error) {
          console.log(error);
          reject(error.error)
        }
      });
    }
    getUser(userID) {
      return new Promise(async (resolve, reject) => {
        try {
          let data = await this.main().performFetch(`/user/${ userID }`);
          resolve(data.data.data)
        } catch (error) {
          console.log(error);
          reject(error.error)
        }
      });
    }
  }

  (async () => {
    let resultsInstance = new Results();
    let profile_image = await resultsInstance.main().readFromDatabase();
    resultsInstance.main().navInstance("../parties/index.html", "../petitions/index.html", "index.html", profile_image.url, "../vote/index.html", "../myVotes/index.html", "../../index.html").showNav();

    resultsInstance.generateData();

    let logout = document.getElementById("logout");
    logout.addEventListener("click", () => {
      resultsInstance.main().navInstance().logout();
    });
  })()
}