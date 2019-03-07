class Fetch {
  constructor(url, method="GET", data={}, authenticate=true) {
    this.baseUrl = "http://127.0.0.1:5000/api/v2";
    this.url = url;
    this.method = method;
    this.data = data;
    this.authenticate = authenticate;
  }
  performFetch() {
    return new Promise(async (resolve, reject) => {
      try {
        let token = "";
        if (this.authenticate) {
          let indexeddbInstance = new Indexeddb();
          let data = await indexeddbInstance.readFromDatabase();
          token = data.token;
        }
        let fetchData = {
          method: this.method,
          headers: {
              "Content-Type": "application/json",
              "Authorization": "Bearer " + token
          },
          body: JSON.stringify(this.data)
        }
        if (this.method == "GET" || this.method == "DELETE") {
          delete fetchData.body;
        }
        let response = await fetch(this.baseUrl + this.url, fetchData);
        let jsonObj = await response.json();
        if (jsonObj.status != 200) {
          reject(jsonObj)
        }
        resolve(jsonObj)
      } catch (error) {
        console.log(error);
        reject(error)
      }
    });
  }
}