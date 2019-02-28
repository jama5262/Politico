let baseUrl = "https://politico-andela-37.herokuapp.com/api/v2"

let performFetch = (url, method="GET", data={}) => {
  return new Promise(async (resolve, reject) => {
    let fetchData = {
      method: method,
      headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTEzNjgxNDQsIm5iZiI6MTU1MTM2ODE0NCwianRpIjoiMmMyNmZlZjktZTVkMi00OTg4LTlkZjgtZDE0ZGY0ODg1NjA4IiwiZXhwIjoxNTUxMzY5MDQ0LCJpZGVudGl0eSI6eyJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSIsInJvbGUiOiJUcnVlIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.SGAsBtHAwCcyIGssiELUjQRxry0c5fab2TsBhWJpQjI"
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