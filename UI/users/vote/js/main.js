window.onload = () => {
  class Votes {
    constructor() {
      // this.officeHolder = ;
      // this.candidateHolde = ;
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    populate(data) {
      
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

  votesInstance.generateData();
}