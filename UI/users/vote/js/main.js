window.onload = () => {
  class Votes {
    constructor() {
      this.officeHolder = document.getElementsByClassName("main-container")[0];
      // this.candidateHolder = document.getElementsByClassName("candidate-holder-index");
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    populate(data) {
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
            <div>
              <button class="button-design">vote</button>
            </div>
          </div>
        `
        if (data[i].candidates == "No candidates are running for this office") {
          candidateHolderBody = `
          <div style="padding: 10px 0 20px 0;">
            ${ data[i].candidates }
          </div>
          `
        } else {
          for (var j = 0; j < data[i].candidates.length; j++) {
            let result = `
              <div class="candidate-index">
                <div style="background-image: url('${ data[i].candidates[j].candidateUrl }');" class="candidate-profile-image-index"></div>
                <div class="candidate-info-index">
                  <h4>${ data[i].candidates[j].candidateName }</h4>
                  <h6>${ data[i].candidates[j].partyName }</h6>
                  <div style = "padding-bottom: 10px;" class="vote-for-candidate-index">
                    <input type="radio" name="name" id="">
                  </div>
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
        let offices = await this.getAllOffices();
        for (var i = 0; i < offices.length; i++) {
          let candidates = await this.getAllCandidates(offices[i].id);
          if (candidates == "The candidate was not found") {
            offices[i]["candidates"] = "No candidates are running for this office";
          } else {
            offices[i]["candidates"] = candidates;
            for (var j = 0; j < candidates.length; j++) {
              let party = await this.getParty(candidates[j].party);
              candidates[j]["partyName"] = party[0].name;
              let user = await this.getUser(candidates[j].candidate);
              candidates[j]["candidateName"] = user[0].first_name + " " + user[0].last_name;
              candidates[j]["candidateUrl"] = user[0].passport_url;
            }
          }
        }
        console.log(offices);
        this.populate(offices);
        this.main().loading(false);
      } catch (error) {
        this.main().loading(false);
      }
    }
    getAllOffices() {
      return new Promise(async (resolve, reject) => {
        try {
          let data = await this.main().performFetch("/offices");
          resolve(data.data.data)
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

  let votesInstance = new Votes();
  votesInstance.main().navInstance("../parties/index.html", "../petitions/index.html", "index.html", "../../assets/images/profile_image.jpg", "index.html", "../myVotes/index.html", "../../index.html").showNav();

  let logout = document.getElementById("logout");
  logout.addEventListener("click", () => {
    votesInstance.main().navInstance().logout();
  });

  votesInstance.generateData();
}