window.onload = () => {
  class AdminParties {
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
      let navInstance = new AdminNavigation("index.html", "../adminGovOffices/index.html", "../../index.html");
      navInstance.showNav();
    }
    populate(data) {
      let tableBody = document.getElementsByTagName("tbody")[0];
      for (var i = 0; i < data.length; i++) {
        let tableRow = `
          <tr>
            <td>
              <div style="background-image: url('${ data[i].logo_url }');" class="party-image-index"></div>
            </td>
            <td>${ data[i].name }</td>
            <td>${ data[i].abbr }</td>
            <td>
              <div style="display: flex">
                <a href="./editParty.html"><button class="button-design-edit">edit</button></a>
                <button class="button-design-delete">delete</button>
              </div>
            </td>
          </tr>
        `
        tableBody.insertAdjacentHTML('beforeend', tableRow);
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

  let partiesInstance = new AdminParties();
  partiesInstance.setNav();
  partiesInstance.getAllParites();
}