// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        file:///C:/Users/Milenko/Desktop/Tarea_Cripto/Tarea3/PagWeb.html
// @grant        none
// @require      https://raw.githubusercontent.com/behdadahmadi/jscrypt/master/jscrypt.js
//@require       https://raw.githubusercontent.com/nodejs/node/v14.14.0/lib/crypto.js

key = "llave secreta de 3DES :o";

console.log('decrypt',CryptoJS.TripleDES.decrypt(param, key).toString(CryptoJS.enc.Utf8))



