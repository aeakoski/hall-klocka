function init () {
  startTime()
  dateString()
  miscString()
  var t = setTimeout(init, 1000)
}

function startTime () {
  var today = new Date()
  var h = today.getHours()
  var m = today.getMinutes()

  m = checkTime(m)

  document.getElementById('clock').innerHTML = h + ':' + m
}
function checkTime (i) {
  if (i < 10) { i = '0' + i };  // add zero in front of numbers < 10
  return i
}

function dateString () {
  var d = new Date()
  var dateS = d.getFullYear() + '-' + checkTime(d.getMonth()) + '-' + checkTime(d.getDate())
  document.getElementById('date').innerHTML = dateS
}

Date.prototype.getWeek = function () {
  var onejan = new Date(this.getFullYear(), 0, 1)
  return Math.ceil((((this - onejan) / 86400000) + onejan.getDay() + 1) / 7)
}

function miscString () {
  var now = new Date()
  var days = ['Sunday', 'Monday', 'Tuesday', 'Wednsday', 'Thursday', ' Friday', 'Saturday']

  var start = new Date(now.getFullYear(), 0, 0)
  var diff = (now - start) + ((start.getTimezoneOffset() - now.getTimezoneOffset()) * 60 * 1000)
  var oneDay = 1000 * 60 * 60 * 24
  var doy = Math.floor(diff / oneDay)

  var w = now.getWeek()

  document.getElementById('day').innerHTML = (days[now.getDay()])
  document.getElementById('doy').innerHTML = ('DOY: ' + doy)
  document.getElementById('week').innerHTML = ('Week: ' + w)
}
