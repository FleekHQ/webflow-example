let user = window.localStorage.getItem('_u');

if (user) {
  let signupButton = document.querySelector('a[class*="sign-up"][class*="w-button"]');
  let signinButton = document.querySelector('a[class*="sign-in"][class*="w-button"]');

  signupButton.remove();

  signinButton.href = '/home';
  signinButton.textContent = 'Go to my files';
  signinButton.style.color = '#151515';
  signinButton.style.borderRadius = '8px';
  signinButton.style.fontWeight = '700';
  signinButton.style.backgroundImage = 'linear-gradient(114deg, #ed55eb 13%, #17e0d8 40%, #00ffc2 59%, #ffec06 93%)';
}
