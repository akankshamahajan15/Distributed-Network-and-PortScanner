function openSlideMenu() {
	document.getElementById('menu').style.width = '300px';
	document.getElementById('content').style.marginLeft = '300px';
}

function closeSlideMenu() {
	document.getElementById('menu').style.width = '0px';
	document.getElementById('content').style.marginLeft = '0px';
}

function about_func() {

	document.getElementById('about_text').innerHTML = 'This is the about page when chosen from the side menu!';
	closeSlideMenu()
}
