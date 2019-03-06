window.onload = () => {
  class Votes {
    constructor() {
      this.officeHolder = document.getElementsByClassName("main-container")[0];
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    populate(data) {
      this.main().alertInstance("Candidates retrieved");
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
              <button id="vote" office="${ data[i].id }" officeName="${ data[i].name }" class="button-design">vote</button>
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
                    <input type="radio" value="${ data[i].candidates[j].candidateName }" name="${ data[i].id }" id="${ data[i].candidates[j].candidate }">
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
    async vote(office) {
      let candidate = document.querySelector(`input[name="${ office.officeID }"]:checked`);
      try {
        if (candidate == null) {
          return this.main().alertInstance(`Please choose a candidate to vote for ${ office.officeName }`, true);
        }
        this.main().loading();
        let userId = await this.main().readFromDatabase();
        let data = await this.main().performFetch("/votes", "POST", {
          office: parseInt(office.officeID),
          candidate: parseInt(candidate.id),
          created_by: parseInt(userId.id)
        });
        console.log(data);
        this.main().loading(false);
        this.main().alertInstance(`${ data.data.msg }, you have voted for ${ candidate.value }`);
      } catch (error) {
        console.log(error);
        this.main().loading(false);
        if (error.error.indexOf("already exists") !== -1) {
          this.main().alertInstance("You cannot vote twice for the same candidate or office", true);
        } else {
          this.main().alertInstance(error.error, true);
        }
      }
    }
    async generateData() {
      try {
        this.main().loading();
        this.main().alertInstance("Please wait, fetching all candidates");
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
    let votesInstance = new Votes();
    let profile_image = await votesInstance.main().readFromDatabase();
    votesInstance.main().navInstance("../parties/index.html", "../petitions/index.html", "../results/index.html", profile_image.url, "index.html", "../myVotes/index.html", "../../index.html").showNav();
      
    votesInstance.generateData();

    let mainEl = document.getElementsByClassName("main-container")[0];
    if (mainEl != null) {
      mainEl.addEventListener("click", (event) => {
        if (event.target.id == "vote") {
          votesInstance.vote({
            officeID: event.target.attributes.office.nodeValue,
            officeName: event.target.attributes.officeName.nodeValue
          });
        }
      })
    }

    let logout = document.getElementById("logout");
    logout.addEventListener("click", () => {
      votesInstance.main().navInstance().logout();
    });
   })();
}