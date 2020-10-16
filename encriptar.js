import * as myModule from 'jscrypt.js';
var jscrypto = require('jscrypto');

jscrypto.encryptFile("A.txt","A-encrypted.txt","aes256","P@sW0rD",655000,(progress) =>{

console.log(progress);

});