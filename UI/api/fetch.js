let baseUrl = "https://politico-andela-37.herokuapp.com/api/v2"

let performFetch = async (url, method="GET", data={}) => {
  let fetchData = {
    method: method,
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTEzNjYxMTksIm5iZiI6MTU1MTM2NjExOSwianRpIjoiNmM1ZGZkNDQtYjNjMC00ZGE0LTk5YTktZGRmOWUxMzZjNDQ5IiwiZXhwIjoxNTUxMzY3MDE5LCJpZGVudGl0eSI6eyJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSIsInJvbGUiOiJUcnVlIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.TtzBsglCs377kCEwZFjywL-fao5JGa1e683Die_hCYw"
    },
    body: JSON.stringify(data)
  }

  if (method == "GET" || method == "DELETE") {
    delete fetchData.body;
  }

  try {
    let response = await fetch(baseUrl + url, fetchData);
    let jsonObj = await response.json();
    console.log(jsonObj);
  } catch (error) {
    console.log(error);
  }
}