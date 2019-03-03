class Loading {
  constructor() {
    this.bodyEl = document.body;
    this.navEl = document.getElementsByTagName("nav")[0];
    this.alertEl = `
      <div style = "display: none" id="alert">
        <div style = "display: none" id="loader"></div>
      </div>
    `
    this.states = {
      success: "",
      error: ""
    }
  }
  addtoBody() {
    this.bodyEl.insertAdjacentHTML('afterbegin', this.alertEl);
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

class Alert {
  constructor(alertMessage=null, color=false, timer=false) {
    this.mainEl = document.getElementsByClassName("main-container")[0];
    if (color == false) {
      this.color = "#66BB6A"
    } else {
      this.color = "#EF5350"
    }
    this.timer = timer;
    this.alertMessageEl = `
      <div style='display = none; background-color: ${ this.color };' id="alertMessage" class="card-design">
        ${ alertMessage }
      </div>
    `
  }
  addToMain() {
    this.mainEl.insertAdjacentHTML('afterbegin', this.alertMessageEl);
  }
  async showAlertMessage(){
    return new Promise((resolve) => {
      this.addToMain();
      document.getElementById("alertMessage").style.display = "block";
      setTimeout(function () {
        document.getElementById("alertMessage").remove();
        resolve();
      }, 3000);
    });
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
          </script>
              <a href="${ this.navLinks.myVotes }">My Votes</a>
              <a style="display: none;" id="logoutUrl" href="${ this.navLinks.logout }">Logout</a>
              <a id="logout" style="cursor: pointer;">Logout</a>
            </div>
          </div>
        </div>
      </nav>`
    }
  }
  showNav() {
    this.bodyEl.insertAdjacentHTML('afterbegin', this.elements.navEl);
  }
  async logout() {
    let dbInstance = new Indexeddb();
    await dbInstance.deleteFromDatabase();
    window.location.href = document.getElementById("logoutUrl").getAttribute("href");
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
          <a style="display: none;" id="logoutUrl" href="${ this.navLinks.logout }">Logout</a>
          <a class="a-tag-nav" id="logout" style="cursor: pointer;">Logout</a>
        </div>
      </nav>`
    }
  }
  showNav() {
    this.bodyEl.insertAdjacentHTML('afterbegin', this.elements.navEl);
  }
  async logout() {
    let dbInstance = new Indexeddb();
    await dbInstance.deleteFromDatabase();
    window.location.href = document.getElementById("logoutUrl").getAttribute("href");
  }
}