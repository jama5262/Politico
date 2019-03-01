class Alert {
  constructor() {
    this.bodyEl = document.body;
    this.elements = {
      alertEl: `
      <div style = "display: none" id="alert">
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
    this.bodyEl.insertAdjacentHTML('afterbegin', this.elements.alertEl);
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