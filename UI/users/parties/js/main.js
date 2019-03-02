window.onload = () => {  
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
      let navInstance = new Navigation("index.html", "../../assets/images/profile_image.jpg", "../vote/index.html", "./myVotes/index.html", "../../index.html");
      navInstance.showNav();
    }
    populate(data) {
      let partyHolderEl = document.getElementsByClassName("party-card-holder-index")[0];
      for (var i = 0; i < data.length; i++) {
        let partyEl = `
        <div class="party-card-index card-design">
          <div style="background-image: url('${ data[i].logo_url }');" class="party-image-holder-index"></div>
          <div class="party-content-holder-index">
            <h3>${ data[i].name } (${ data[i].abbr })</h3>
          </div>
          <div class="party-button-holder-index">
            <a href="party.html"><button class="button-design">View Party</button></a>
          </div>
        </div>
      `
        partyHolderEl.insertAdjacentHTML('beforeend', partyEl);
      }
    }
    async getAllParites() {
      try {
        this.loading()
        let fetchInstance = new Fetch("/parties");
        let data = await fetchInstance.performFetch();
        this.populate(data.data.data);
        this.loading(false);
      } catch (error) {
        console.log(error.error || error.message);
        this.loading(false);
      }
    }
  }

  let partiesInstance = new Parites();
  partiesInstance.setNav();
  partiesInstance.getAllParites();
}