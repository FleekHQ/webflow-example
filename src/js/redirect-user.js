let user = window.localStorage.getItem('_u');

if (user) {
  window.location.href = "/home";
}
