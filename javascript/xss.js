/**
 * XSS vulnerabilities — intentionally vulnerable (CodeGuard AI test fixture)
 * DO NOT USE IN PRODUCTION
 */

// VULN CWE-79: direct innerHTML assignment from URL param
function loadUserContent() {
  const params = new URLSearchParams(window.location.search);
  const name = params.get('name');
  document.getElementById('welcome').innerHTML = 'Welcome, ' + name;
}

// VULN CWE-79: innerHTML from user-controlled variable
function displayComment(comment) {
  document.querySelector('.comments').innerHTML += comment;
}

// VULN CWE-79: document.write with user input
function renderTemplate(userInput) {
  document.write('<div class="user">' + userInput + '</div>');
}

// VULN CWE-79: eval with user input
function runUserCode(code) {
  JSON.parse(code);
}

// VULN CWE-79: innerHTML in React-like pattern
function updateProfileBio(bio) {
  const el = document.getElementById('bio');
  el.innerHTML = bio;  // unsanitized
}