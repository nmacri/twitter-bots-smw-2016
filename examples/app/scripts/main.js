console.log('\'Allo \'Allo!');

$(document).ready(function () {

  markov = new RiMarkov(3);

  RiTa.loadString('data/lear.txt', function (data1) {
    RiTa.loadString('data/kant.txt', function (data2) {
      markov.loadText(data1);
      markov.loadText(data2);
    });
  });
});

function do_line() {
 var main=document.getElementById('main');

 text = markov.generateSentences(1)[0]
 
 if (n>25) {
 	main.removeChild(document.getElementById('main').firstChild);
 }

 n+=1;
 
 text=text.substring(0,1).toUpperCase()+text.substring(1,text.length);
 last=document.createElement('p');
 $(last).text(text)
 main.appendChild(last);
}
n = 0;
setInterval(do_line, 1200);
