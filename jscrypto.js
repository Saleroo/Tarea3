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
'use strict';
var fs = require('fs');
var crypto = require('crypto');

function encryptFile(sourcePath, destinationPath, algorithm, password, chunkSize, callback) {
    chunkSize = (chunkSize === 0) ? chunkSize = 665539 : chunkSize;
    var inFile = fs.createReadStream(sourcePath, { highWaterMark: chunkSize });
    var outFile = fs.createWriteStream(destinationPath);
    var encryptor = crypto.createCipher(algorithm, password);
    var size = fs.statSync(sourcePath).size;
    inFile.on('data', function(data) {
        var percentage = parseInt(inFile.bytesRead) / parseInt(size) * 100;
        var encrypted = encryptor.update(data);
        outFile.write(encrypted);
        callback(percentage);
    });
    inFile.on('close', function() {
        outFile.write(encryptor.final());
        outFile.close();
        callback(true);
    });
}

function decryptFile(sourcePath, destinationPath, algorithm, password, chunkSize, callback) {
    chunkSize = (chunkSize === 0) ? chunkSize = 665539 : chunkSize;
    var inFile = fs.createReadStream(sourcePath, { highWaterMark: chunkSize });
    var outFile = fs.createWriteStream(destinationPath);
    var decryptor = crypto.createDecipher(algorithm, password);
    var size = fs.statSync(sourcePath).size;
    inFile.on('data', function(data) {
        var percentage = parseInt(inFile.bytesRead) / parseInt(size) * 100;
        var decrypted = decryptor.update(data);
        outFile.write(decrypted);
        callback(percentage);
    });
    inFile.on('close', function() {
        outFile.write(decryptor.final());
        outFile.close();
        callback(true);
    });

}
module.exports = { encryptFile, decryptFile }
