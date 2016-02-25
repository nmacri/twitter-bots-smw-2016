var train = function(settings) {

    document.markov = new RiMarkov(3);

    RiTa.loadString('', function(data1) {
        RiTa.loadString('data/smw.txt', function(d1) {
            RiTa.loadString('data/nietzsche.txt', function(d2) {
                RiTa.loadString('data/trump.txt', function(d3) {
                    RiTa.loadString('data/kanye.txt', function(d4) {

                        document.markov.loadText(data1);

                        if (document.settings['smw']) {
                            document.markov.loadText(d1);
                        }

                        if (document.settings['nietzsche']) {
                            document.markov.loadText(d2);
                        }

                        if (document.settings['trump']) {
                            document.markov.loadText(d3);
                        }

                        if (document.settings['kanye']) {
                            document.markov.loadText(d4);
                        }
                    });
                });
            });
        });

    });
};

$(document).ready(function() {

    document.settings = {
        "smw": true,
        "nietzsche": false,
        "trump": false,
        "kanye": false
    };

    train();
});

function do_line() {
    var main = document.getElementById('main');

    text = document.markov.generateSentences(1)[0];

    if (n > 10 && n > 1) {
        main.removeChild(document.getElementById('main').firstChild);
    }

    n += 1;

    text = text.substring(0, 1).toUpperCase() + text.substring(1, text.length);
    last = document.createElement('h5');
    $(last).text(text);
    main.appendChild(last);
}
n = 0;
setInterval(do_line, 1200);

$('.btn').click(function() {

    if ($(this).hasClass('btn-default')) {
        $(this).addClass('btn-primary').removeClass('btn-default');
        document.settings[this.id] = true;
        train();
        $('#main > h5').remove();
        n = 0;
    } else {
        $(this).removeClass('btn-primary').addClass('btn-default');
        document.settings[this.id] = false;
        train();
        $('#main > h5').remove();
        n = 0;
    }

});
