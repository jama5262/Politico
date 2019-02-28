window.onload = () => {
  let loginBtn = document.getElementById("loginBtn");
  loginBtn.addEventListener("click", () => {
    userData = {
      email: "emai1@gmail.com",
      password: "password1"
    }
    performFetch('/auth/login', "POST", userData, false)
    .then((data) => {
      if (data.status == 200) {
        console.log(data);
        return writeToDatabase({
          user: "1",
          token: data.data.token
        });
      } else {
        console.log(data);
      }
    })
    .then((data) => {
      if (data != null) {
        console.log(data);
      } else {
        console.log("not saved")
      }
    })
    .catch((error) => {
      console.log(error);
    })
  });
}