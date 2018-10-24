now = new Date
theYear=now.getYear()
if (theYear < 1900)
theYear=theYear+1900

$('.footer-bottom-line .footer-powered').html('<a href="https://atdigitals.com" style="color: #aaa" target="_blank">Designed and Maintained by AT Digitals</a>');
$('.footer-bottom-line div').first().html('<a href="https://apinternationalfilms.com" style="color: #aaa" target="_blank">'+theYear+' &copy; AP International.</a>');
$('.navbar-brand.ellipsis span').html('<b>AP International - Rights Management</b>');

