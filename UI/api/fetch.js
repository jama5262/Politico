let baseUrl = "https://politico-andela-37.herokuapp.com/api/v2"

let performFetch = (url, method="GET", data={}, authenticate=true) => {
  return new Promise(async (resolve, reject) => {
    let token = "";
    if (authenticate == true) {
      try {
        token = await readFromDatabase();
      } catch (error) {
        console.log(error);
      }
    }
    console.log(token);
    let fetchData = {
      method: method,
      headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + token
      },
      body: JSON.stringify(data)
    }
    if (method == "GET" || method == "DELETE") {
      delete fetchData.body;
    }
    try {
      let response = await fetch(baseUrl + url, fetchData);
      let jsonObj = await response.json();
      resolve(jsonObj)
    } catch (error) {
      console.log(error);
      reject(error)
    }
  });
}