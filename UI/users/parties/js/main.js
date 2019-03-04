window.onload = () => {
  let allParites = document.getElementsByClassName("party-card-holder-index")[0];
  let mainCont = document.getElementsByClassName("main-container")[0]
  let specificParty = document.getElementsByClassName("party-members-holder-party")[0];
  class Parites {
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    populateAllParties(data) {
      for (var i = 0; i < data.length; i++) {
        let partyEl = `
        <div class="party-card-index card-design">
          <div style="background-image: url('${ data[i].logo_url }');" class="party-image-holder-index"></div>
          <div class="party-content-holder-index">
            <h3>${ data[i].name } (${ data[i].abbr })</h3>
          </div>
          <div class="party-button-holder-index">
            <a href="party.html?partyID=${ data[i].id }"><button class="button-design">View Party</button></a>
          </div>
        </div>
      `
        allParites.insertAdjacentHTML('beforeend', partyEl);
      }
    }
    populateSpecificParty(data) {
      let partyInfo = `
        <div style="margin-top: 45px;">
          <h1 class="text-color-design-primary">${ data.name }</h1>
        </div>
        <div class="party-info-holder-party card-design">
          <div style="background-image: url('${ data.logo_url }');" class="party-image-holder-party"></div>
          <div class="party-info-party">
            <ul>
              <li><h3>Abbreviation: ${ data.abbr }</h3></li>
              <li><h3>Head Quarters: ${ data.hq_address }</h3></li>
            </ul>
          </div>
        </div>
      `
      mainCont.insertAdjacentHTML('afterbegin', partyInfo);
    }
    populateMembers(members) {
      for (var i = 0; i < members.length; i++) {
        let partyMember = `
        <div class="party-member-party card-design">
          <div style="background-image: url('${ members[i].passport_url }');" class="party-profile-image-holder-party"></div>
          <div class="party-content-holder-party">
            <h4>${ members[i].first_name } ${ members[i].last_name }</h4>
            <h6>Running for ${ members[i].office.name }</h6>
            <h6>Type: ${ members[i].office.type }</h6>
          </div>
        </div>
      `
      specificParty.insertAdjacentHTML('beforeend', partyMember);
      }
    }
    getPartyMembers(partyMembers) {
      return new Promise(async (resolve, reject) => {
        try {
          let users = [];
          for (var i = 0; i < partyMembers.length; i++) {
            let user = await this.main().performFetch(`/user/${ partyMembers[i].candidate }`);
            let office = await this.main().performFetch(`/offices/${ partyMembers[i].office }`)
            user.data.data[0]["office"] = office.data.data[0]
            users.push(user.data.data[0]);
          }
          resolve(users);
        } catch (error) {
          reject(error);
        }
      });
    }
    async getAllParites() {
      try {
        this.main().loading();
        let data = await this.main().performFetch("/parties")
        this.main().alertInstance(data.data.msg);
        this.populateAllParties(data.data.data);
        this.main().loading(false);
      } catch (error) {
        if (error != null && (error == "Your session has expired" || error == "No access token")) {
          await this.main().alertInstance(error + ", please login to continue", true);
          this.main().navInstance().logout();
        }
        console.log(error);
        this.main().loading(false);
      }
    }
    async getSpecificParty(partyID) {
      try {
        this.main().loading();
        let party = await this.main().performFetch(`/parties/${ partyID }`);
        this.populateSpecificParty(party.data.data[0]);
        let partyMembers = await this.main().performFetch(`/user/candidate/${ partyID }`)
        let users = await this.getPartyMembers(partyMembers.data.data);
        this.populateMembers(users);
        this.main().loading(false);
      } catch (error) {
        console.log(error.error || error.message);
        this.main().alertInstance(error.error, true);
        if (error.error != null && (error.error == "Your session has expired" || error.error == "No access token")) {
          await this.main().alertInstance(error + ", please login to continue", true);
          this.main().navInstance().logout();
        }
        this.main().loading(false);
      }
    }
  }

  let partiesInstance = new Parites();
  partiesInstance.main().navInstance("index.html", "../petitions/index.html", "index.html", "../../assets/images/profile_image.jpg", "../vote/index.html", "../myVotes/index.html", "../../index.html").showNav();

  if (allParites != null) {
    partiesInstance.getAllParites();
  } else {
    let partyID = new URL(window.location.href).searchParams.get("partyID");
    partiesInstance.getSpecificParty(partyID);
  }

  let logout = document.getElementById("logout");
  logout.addEventListener("click", () => {
    partiesInstance.main().navInstance().logout();
  })
}