class Loading {
  constructor() {
    this.bodyEl = document.body;
    this.navEl = document.getElementsByTagName("nav")[0];
    this.elements = {
      alertEl: `
      <div style = "display: none" id="alert">
        <div style = "display: none" id="loader"></div>
      </div>`
    }
    this.states = {
      success: "",
      error: ""
    }
  }
  addtoBody() {
    this.bodyEl.insertAdjacentHTML('afterbegin', this.elements.alertEl);
  }
  showLoading() {
    this.addtoBody();
    document.getElementById("alert").style.display = "block";
    document.getElementById("loader").style.display = "block";
  }
  dismissAlert() {
    document.getElementById("alert").remove()
  }
}

class Navigation {
  constructor(home, petitions, results, profileImage, vote, myVotes, logout) {
    this.bodyEl = document.body;
    this.navLinks = {
      home: home,
      petitions: petitions,
      results: results,
      profileImage: profileImage,
      vote: vote,
      myVotes: myVotes,
      logout: logout
    }
    this.elements = {
      navEl: `
      <nav class="background-color-design">
        <div class="text-color-design-secondary">
          <h1 class="politico-letter">Politico</h1>
        </div>
        <div class="link-container-2">
          <a class="a-tag-nav" href="${ this.navLinks.home }">Home</a>
          <a class="a-tag-nav" href="${ this.navLinks.petitions }">Petitions</a>
          <a class="a-tag-nav" href="${ this.navLinks.results }">Results</a>
        </div>
        <div class="link-container-3">
          <a href="${ this.navLinks.vote }"><button class="button-design-secondary">vote</button></a>
          <div class="dropdown">
            <img src="${ this.navLinks.profileImage }" alt="" class="profile-image-icon-small">
            <div class="dropdown-content">
              <a href="${ this.navLinks.myVotes }">My Votes</a>
              <a id="logout" href="${ this.navLinks.logout }">Logout</a>
            </div>
          </div>
        </div>
      </nav>`
    }
  }
  showNav() {
    this.bodyEl.insertAdjacentHTML('afterbegin', this.elements.navEl);
  }
}

class AdminNavigation {
  constructor(home, gov, logout) {
    this.bodyEl = document.body;
    this.navLinks = {
      home: home,
      gov: gov,
      logout: logout
    }
    this.elements = {
      navEl: `
      <nav style="padding: 10px 0" class="background-color-design">
        <div class="text-color-design-secondary">
          <h1 class="politico-letter">Politico</h1>
        </div>
        <div class="link-container-2">
          <a class="a-tag-nav" href="${ this.navLinks.home }">Home</a>
          <a class="a-tag-nav" href="${ this.navLinks.gov }">Gov Offices</a>
        </div>
        <div class="link-container-3">
          <a class="a-tag-nav" href="${ this.navLinks.logout }">Logout</a>
        </div>
      </nav>`
    }
  }
  showNav() {
    this.bodyEl.insertAdjacentHTML('afterbegin', this.elements.navEl);
  }
}