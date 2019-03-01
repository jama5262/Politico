class Fetch {
  constructor(url, method="GET", data={}, authenticate=true) {
    this.baseUrl = "https://politico-andela-37.herokuapp.com/api/v2";
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
          token = await readFromDatabase();
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
        console.log(jsonObj);
      } catch (error) {
        console.log(error);
        reject(error)
      }
    });
  }
}