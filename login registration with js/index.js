function LoginResistration(type) {
  document.getElementById("registerForm").classList.add("d-none");
  document.getElementById("loginForm").classList.add("d-none");
  if (type == "register") {
    document.getElementById("registerForm").classList.remove("d-none");
  } else if (type == "login") {
    document.getElementById("loginForm").classList.remove("d-none");
  }
}
function register() {
  const fullname = document.getElementById("regFullname").value;
  const email = document.getElementById("regEmail").value;
  const password = document.getElementById("regPassword").value;
  if (!fullname) {
    alert("please enter the full name!");
    return;
  }
  if (!email) {
    alert("please enter your email");
  }
  if (!password) {
    alert("please enter your password");
  }
  const user = { fullname, email, password };
  localStorage.setItem(email, JSON.stringify(user));
  alert("Registration successfull you can now login!");
  document.getElementById("regFullname").value = "";
  document.getElementById("regEmail").value = "";
  document.getElementById("regPassword").value = "";

  LoginResistration("login");
}
function login() {
  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;
  if (!email) {
    alert("Email field required");
  }
  if (!password) {
    alert("Password is required");
  }
  const user = localStorage.getItem(email);
  if (!user) {
    alert("User is not exist!");
    return;
  }
  const perseUser = JSON.parse(user);
  if (password != perseUser.password) {
    alert("Incorrect Password");
    return;
  }
  alert("login successful!! Welcome " + perseUser.fullname);
  document.getElementById("loginEmail").value = "";
  document.getElementById("loginPassword").value = "";
}
