window.onload = () => {
  class MyVotes {
    constructor() {
      this.mainEl = document.getElementsByClassName("main-container")[0];
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
    populateUserInfo(data) {
      let profileInfoEl = `
        <div class=" card-design user-profile-info-holder-imdex">
          <div>
            <h2 class="text-color-design-primary">Profile Info</h2>
          </div>
          <div class="user-profile-info">
            <div style="height: 100px; width: 100px; background-image: url('${ data.url }');" class="candidate-profile-image-index"></div>
            <p>Names: ${ data.fname } ${ data.lname }</p>
            <p>Email: ${ data.email }</p>
            <p>Phone: ${ data.phone }</p>
          </div>
        </div>
      `
      this.mainEl.insertAdjacentHTML("afterbegin", profileInfoEl);
    }
    async getUserInfo() {
      try {
        let userInfo = await this.main().readFromDatabase();
        this.populateUserInfo(userInfo);
      } catch (error) {
        console.log(error);
      }
    }
  }

  (async () => {
    let myVotesInstance = new MyVotes();
    let profile_image = await myVotesInstance.main().readFromDatabase();
    myVotesInstance.main().navInstance("../parties/index.html", "../petitions/index.html", "index.html", profile_image.url, "../vote/index.html", "index.html", "../../index.html").showNav();

    myVotesInstance.getUserInfo();

    let logout = document.getElementById("logout");
    logout.addEventListener("click", () => {
      votesInstance.main().navInstance().logout();
    });
  })()
}