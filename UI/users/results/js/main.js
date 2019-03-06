window.onload = () => {
  class Results {
    constructor() {
      
    }
    main() {
      let mainInstance = new Main();
      return mainInstance;
    }
  }

  (async () => {
    let resultsInstance = new Results();
    let profile_image = await resultsInstance.main().readFromDatabase();
    resultsInstance.main().navInstance("../parties/index.html", "../petitions/index.html", "index.html", profile_image.url, "../vote/index.html", "../myVotes/index.html", "../../index.html").showNav();
  })()
}