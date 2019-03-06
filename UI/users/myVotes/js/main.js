window.onload = () => {
  class MyVotes {
    constructor() {
      this.mainEl = document.getElementsByClassName("main-container")[0];
      this.votesEl = document.getElementsByClassName("user-votes")[0];
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
      this.getUserVotes();
    }
    populateUserVotes(data) {
      for (var i = 0; i < data.length; i++) {
        let votesEl = `
          <div class="vote">
            <h3 class="text-color-design-primary">${ data[i].officeName }</h3>
            <div class="candidate-index">
                <div style="background-image: url('${ data[i].candidateUrl }');" class="candidate-profile-image-index"></div>
                <div class="candidate-info-index">
                  <h3>${ data[i].candidateName }</h3>
                </div>
            </div>
          </div>
        `
        this.votesEl.insertAdjacentHTML("afterbegin", votesEl);
      }
    }
    populateNoUserVotes() {
      let votesEl = `
        <div class="vote">
          <div class="candidate-index">
              <div class="candidate-info-index">
                <h3>You have no votes</h3>
              </div>
          </div>
        </div>
      `
      this.votesEl.insertAdjacentHTML("afterbegin", votesEl);
    }
    async getUserVotes() {
      try {
        this.main().loading();
        let user = await this.main().readFromDatabase();
        console.log(user.id);
        let votes = await this.main().performFetch(`/votes/${ user.id }`);
        for (var i = 0; i < votes.data.data.length; i++) {
          if (user.id == votes.data.data[i].created_by) {
            let candidate = await this.main().performFetch(`/user/${ votes.data.data[i].candidate }`)
            votes.data.data[i]["candidateName"] = candidate.data.data[0].first_name + " " + candidate.data.data[0].last_name
            votes.data.data[i]["candidateUrl"] = candidate.data.data[0].passport_url
            let office = await this.main().performFetch(`/offices/${ votes.data.data[i].office }`)
            votes.data.data[i]["officeName"] = office.data.data[0].name
          }
        }
        this.main().loading(false);
        this.populateUserVotes(votes.data.data);
        console.log(votes.data.data);
      } catch (error) {
        this.main().loading(false);
        console.log(error.error);
        if (error.error != null && error.error == "The vote was not found") {
          this.populateNoUserVotes();
        }
      }
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
      myVotesInstance.main().navInstance().logout();
    });
  })()
}