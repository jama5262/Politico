window.onload = () => {  
  class Parites {
    constructor() {
      
    }
    loading(load=true) {
      let alertInstance = new Alert();
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
    async getAllParites() {
      try {
        this.loading()
        let fetchInstance = new Fetch("/parties");
        let data = await fetchInstance.performFetch();
        // this.loading(false);
      } catch (error) {
        console.log(error.error || error.message);
        // this.loading(false);
      }
    }
  }

  let partiesInstance = new Parites();
  partiesInstance.setNav();
  partiesInstance.getAllParites();
}