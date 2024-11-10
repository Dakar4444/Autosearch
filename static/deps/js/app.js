const data = new Date()
console.log(data)
function calculateAge() {}

var now = new Date() //Текущя дата
var today = new Date(now.getFullYear(), now.getMonth(), now.getDate()) //Текущя дата без времени
var dob = new Date(1990, 9, 31) //Дата рождения
var dobnow = new Date(today.getFullYear(), dob.getMonth(), dob.getDate()) //ДР в текущем году
var age //Возраст
console.log(now, today, dob, dobnow)
//Возраст = текущий год - год рождения
age = today.getFullYear() - dob.getFullYear()
//Если ДР в этом году ещё предстоит, то вычитаем из age один год
if (today < dobnow) {
	age = age - 1
}

document.write(`Возраст: ${age}`)
