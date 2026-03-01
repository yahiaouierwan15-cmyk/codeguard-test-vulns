/**
 * SQL Injection — intentionally vulnerable (CodeGuard AI test fixture)
 * DO NOT USE IN PRODUCTION
 */
const mysql = require('mysql2');
const connection = mysql.createConnection({ host: 'localhost', user: 'root', database: 'app' });

// VULN CWE-89: string concatenation
function getUserByName(username) {
  const query = "SELECT * FROM users WHERE username = '" + username + "'";
  connection.query(query, (err, results) => console.log(results));
}

// VULN CWE-89: template literal in query
function getOrdersByUser(userId) {
  const query = `SELECT * FROM orders WHERE user_id = ${userId}`;
  connection.query(query, (err, results) => console.log(results));
}

// VULN CWE-89: dynamic admin query
function searchAdmin(term, table) {
  const query = "SELECT * FROM " + table + " WHERE name = '" + term + "'";
  connection.query(query);
}

module.exports = { getUserByName, getOrdersByUser, searchAdmin };
