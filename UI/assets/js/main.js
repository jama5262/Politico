class Alert {
  constructor() {
    this.bodyEl = document.body;
    this.navEl = document.getElementsByTagName("nav")[0];
    this.elements = {
      alertEl: `
      <div style = "display: none" id="alert">
        <div style = "display: none" id="loader"></div>
        <div style = "display: none" id="alertMessage">This is a message</div>
      </div>`,
      alertEl1: `
      <div style = "display: none" id="alert2">
        <div style = "display: none" id="loader"></div>
        <div style = "display: none" id="alertMessage">This is a message</div>
      </div>`
    }
    this.states = {
      success: "",
      error: ""
    }
  }
  addtoBody() {
    if (this.nav == null) {
      this.bodyEl.insertAdjacentHTML('afterbegin', this.elements.alertEl);
    } else {
      this.bodyEl.insertAdjacentHTML('afterbegin', this.elements.alertEl1);
    }
  }
  showLoading() {
    this.addtoBody();
    document.getElementById("alert").style.display = "block";
    document.getElementById("loader").style.display = "block";
  }
  showSatusMessage() {
    this.addtoBody();
    document.getElementById("alert").style.display = "block";
    document.getElementById("alertMessage").style.display = "block";
  }
  dismissAlert() {
    document.getElementById("alert").remove()
  }
}

class Navigation {
  constructor(home, profileImage, vote, myVotes, logout) {
    this.bodyEl = document.body;
    this.navLinks = {
      home: home,
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
        </div>
        <div class="link-container-3">
          <a href="${ this.navLinks.vote }"><button class="button-design-secondary">vote</button></a>
          <div class="dropdown">
            <img src="${ this.navLinks.profileImage }" alt="" class="profile-image-icon-small">
            <div class="dropdown-content">
              <a href="${ this.navLinks.myVotes }">My Votes</a>
              <a href="${ this.navLinks.logout }">Logout</a>
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