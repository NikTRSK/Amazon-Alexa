// const data = require('./data.json');
// eventData = data["oscars"];

// let searchterm = "Dakota Johnson";
// let person = eventData.find(function(item) {
//     return item.title == searchterm;
// });

// // console.log(data["Oscars"])
// console.log(person.title);

const Data = {
    "oscars": [{
            "description": "In Versace",
            "title": "Halle Berry",
            "url": "http://akns-images.eonline.com/eol_images/Entire_Site/2017126/rs_634x1024-170226165902-634-academy-awards-oscars-2017-arrivals-halle-berry.jpg"
        },
        {
            "description": "In Narciso Rodriguez",
            "title": "Kate McKinnon",
            "url": "http://akns-images.eonline.com/eol_images/Entire_Site/2017126/rs_634x1024-170226170353-634-kate-mckinnon.cm.22617.jpg"
        }
    ],
    "people's choice awards": [{
            "description": "&nbsp;We\"ve been waiting for tonight to see the <em>Shades of Blue</em> star pull off another winning look. Spoiler: She didn\"t disappoint in her&nbsp;black gown with a sheer beaded bust by Reem Acra and&nbsp;Salvatore Ferragamo clutch.",
            "title": "Jennifer Lopez",
            "url": "http://akns-images.eonline.com/eol_images/Entire_Site/2017018/rs_634x1024-170118174219-634-jennifer-lopez-peoples-choice-awards-2017.jpg"
        },
        {
            "description": "Before their highly anticipated performance, Ally Brooke, Normani Kordei, Lauren Jauregui and Dinah Jane prove to be the perfect match.&nbsp;",
            "title": "Fifth Harmony",
            "url": "http://akns-images.eonline.com/eol_images/Entire_Site/2017018/rs_839x1024-170118174826-634-fifth-harmony-peoples-choice-awards-2017.jpg"
        }
    ]
};

let e = Data["oscars"];

let res = e.find((item) => {
    // console.log(item.title);
    return item.title.toLowerCase() == "Kate McKinnon".toLowerCase();
});

console.log(res);