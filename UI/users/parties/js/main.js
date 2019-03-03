window.onload = () => {
  let allParites = document.getElementsByClassName("party-card-holder-index")[0];
  let mainCont = document.getElementsByClassName("main-container")[0]
  let specificParty = document.getElementsByClassName("party-members-holder-party")[0];
  class Parites {
    constructor() {
      
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
      let navInstance = new Navigation("index.html", "index.html", "index.html", "../../assets/images/profile_image.jpg", "../vote/index.html", "./myVotes/index.html", "../../index.html");
      navInstance.showNav();
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
      console.log(mainCont);
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
            let fetchInstance = new Fetch(`/user/${ partyMembers[i].candidate }`);
            let user = await fetchInstance.performFetch();
            fetchInstance = new Fetch(`/offices/${ partyMembers[i].office }`);
            let office = await fetchInstance.performFetch();
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
        this.loading()
        let fetchInstance = new Fetch("/parties");
        let data = await fetchInstance.performFetch();
        this.populateAllParties(data.data.data);
        this.loading(false);
      } catch (error) {
        console.log(error.error || error.message);
        this.loading(false);
      }
    }
    async getSpecificParty(partyID) {
      try {
        this.loading()
        let fetchInstance = new Fetch(`/parties/${ partyID }`);
        let party = await fetchInstance.performFetch();
        this.populateSpecificParty(party.data.data[0]);
        fetchInstance = new Fetch(`/user/candidate/${ partyID }`);
        let partyMembers = await fetchInstance.performFetch();
        let users = await this.getPartyMembers(partyMembers.data.data);
        this.populateMembers(users);
        this.loading(false);
      } catch (error) {
        console.log(error.error || error.message);
        if (error.error != null && error.error == "Your session has expired") {
          window.location.href = document.getElementById("logout").getAttribute("href");
        }
        this.loading(false);
      }
    }
  }

  let partiesInstance = new Parites();
  partiesInstance.setNav();

  if (allParites != null) {
    partiesInstance.getAllParites();
  } else {
    let partyID = new URL(window.location.href).searchParams.get("partyID");
    partiesInstance.getSpecificParty(partyID);
  }
}