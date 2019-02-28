let openDatabase = () => {
  let request = indexedDB.open('politico', 1);
  request.onupgradeneeded = (event) => {
		let db = event.target.result;
		console.log(db);
		if (!db.objectStoreNames.contains('userToken')) {
			db.createObjectStore('userToken', {keyPath: "user"});
		}
	}
	return request;
}

let closeDatabase = () => {
  db.close();
}

let writeToDatabase = (data) => {
  return new Promise(async (resolve) => {
    let request = await openDatabase();
    request.onsuccess = (event) => {
      let db = event.target.result;
      let transaction = db.transaction("userToken", "readwrite");
      let store = transaction.objectStore("userToken");
      store.put(data);
      resolve("token saved")
      transaction.complete = () => {
        console.log("complete");
        closeDatabase(db);
      }
    }
  });
}

let readFromDatabase = () => {
  return new Promise(async (resolve, reject) => {
    let request = await openDatabase();
    request.onsuccess = (event) => {
      let db = event.target.result;
      let transaction = db.transaction("userToken", "readonly");
      let store = transaction.objectStore("userToken");
      let read = store.get("1");
      read.onsuccess = (event) => {
        if (event.target.result != null) {
          resolve(event.target.result.token);
        } else {
          console.log("No access token");
          reject("No access token")
        }
      }
    }
  });  
}

