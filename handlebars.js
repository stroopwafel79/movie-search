// const fs = require('fs');
// const handlebars = require('handlebars');

// // compile the template in strict mode
// const template = handlebars.compile(source, { strict: true });

// const result = template(data);

// console.log(result);

// // get request to json data
// $.get('handlebars.json', (result) => {
// 	console.log(`The result is: ${result}`);
// })




const source   = $("#template").innerHTML;
const template = Handlebars.compile(source, { strict: true });

const context = $.get("handlebars.json", (results) => {
	console.log(`This is the context: ${context}`);
	console.log(`This is the results: ${results}`);
});

const html = template(context);