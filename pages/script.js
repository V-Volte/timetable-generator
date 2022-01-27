let t = document.getElementById("ttdiv")


fname = '../tables_mt_test.json'
let i = 0;

function construct() {
    $.getJSON(fname, function(json) {
        json.forEach(table => {
            let t = document.createElement('div');
            t.classList += 'ttablediv';
            let j = 0;
            let days = table.days;
            days.forEach(day => {
                let d = document.createElement('div');
                let d0 = document.createElement('div');
                d0.classList += 'dayheading';
                d0.innerHTML = getDay(j);
                t.appendChild(d0);
                let hours = day.hours;
                hours.forEach(hour => {
                    let h = document.createElement('div');
                    h.innerHTML = hour.period.subject;
                    h.classList += 'hour';
                    t.appendChild(h);
                });
                j++;
            })
            document.body.innerHTML += "Table " + ++i + '<br>';
            document.body.appendChild(t);
            document.body.innerHTML += '<br><br>';
        })
    })
}

function constructFromJSON(t) {
    let i = 0;
    $.getJSON(fname, function(json) {
        let days = json.days;
        console.log(json.name);
        days.forEach(day => {
            let d = document.createElement('div');
            let d0 = document.createElement('div');
            d0.classList += 'dayheading';
            d0.innerHTML = getDay(i);
            t.appendChild(d0);
            let hours = day.hours;
            hours.forEach(hour => {
                let h = document.createElement('div');
                h.innerHTML = hour.period.subject;
                h.classList += 'hour';
                t.appendChild(h);
            });
            i++;
        });

        // let e = document.createElement('div');
        // e.classList += "day"
        // let d0 = document.createElement('div');
        // d0.classList += "dayheading";
        // let hs = days[0].hours;
        // e.appendChild(d0);
        // hs.forEach(elem => {
        //     let d = document.createElement('div');
        //     d.classList += 'period'
        //     d.innerHTML = elem.period.subject;
        //     e.appendChild(d);
        // });
        // t.appendChild(e);
    })
}

function getDay(i) {
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    return days[i];
}

construct();

//constructFromJSON();