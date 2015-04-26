var fs = require("fs")

// This code was written by Tyler Akins and placed in the public domain.
// Feel free to use this code if you so desire.
// It would be nice if you left this header intact.  http://rumkin.com

var MorseIndexes = new Array("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",'0',"1","2","3","4","5","6","7","8","9",".",",","?","-","=",":",";","(",")","/",'"',"$","'","\n","_","@","[Error]","[Error]","[Error]","[Error]","[Wait]","[Understood]","[End of message]","[End of work]","[Starting signal]","[Invitation to transmit]","!","!","+","~","#","&","\2044");
var MorseCodes = new Array(".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----.",".-.-.-","--..--","..--..","-....-","-...-","---...","-.-.-.","-.--.","-.--.-","-..-.",".-..-.","...-..-",".----.",".-.-..","..--.-",".--.-.","......",".......","........",".........",".-...","...-.",".-.-.","...-.-","-.-.-","-.-","---.","-.-.--",".-.-.",".-...","...-.-",". ...","-..-.");

function getIndex(arr, str)
{
    var i = 0;
    while (arr[i])
    {
        if (arr[i] == str)
        {
            return i;
        }
        i ++;
    }
    return -1;
}

function decode(str)
{
   var out = "";
   var addSpace = 0;
   
   // Reformat string, trying to change odd things into dots
   // and hyphens
   tmp = "";
   for (var i = 0; i < str.length; i ++)
   {
      if (str.charCodeAt(i) < 27)
      {
         tmp += ' ' + str.charAt(i) + ' ';
      }
      else if (str.charCodeAt(i) == 8211 || str.charCodeAt(i) == 8212 ||
               str.charAt(i) == '_')
      {
         // Compensate for weird hyphens
         tmp += '-';
      }
      else if (str.charCodeAt(i) == 8226 || str.charCodeAt(i) == 8901)
      {
         // Compensate for odd dots
         tmp += '.';
      }
      else
      {
         tmp += str.charAt(i);
      }
   }
  
   str = tmp.split(' ');
   for (var i = 0; i < str.length; i ++)
   {
      var idx = getIndex(MorseCodes, str[i]);
      
      if (idx >= 0)
      {
         out += MorseIndexes[idx];
	 addSpace = 1;
      }
      else
      {
         if (str[i].charCodeAt(0) == 10 || str[i].charCodeAt(0) == 13)
	 {
	    out += str[i];
     	 }
	 else if (addSpace)
	 {
	    out += ' ';
	 }
	 addSpace = 0;
      }
   }
   return out;
}

fs.readFile("pdf_data.txt", "utf8", function(err, data) {
    if (err) {
        return console.log(err);
    }
    console.log(decode(data));
});
