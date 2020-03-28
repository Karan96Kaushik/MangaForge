/*
 * blueimp Gallery Demo JS
 * https://github.com/blueimp/Gallery
 *
 * Copyright 2013, Sebastian Tschan
 * https://blueimp.net
 *
 * Licensed under the MIT license:
 * https://opensource.org/licenses/MIT
 */

/* global blueimp, $ */

var _r = 'DAKOTA JOHNSON Nude - AZNude'

function _carousel(__folder) {
	'use strict'

	// Load demo images from flickr:
	$.get({
		url: '/json',
		data: {
			folder: __folder
		}
	}).done(function (result) {
		var carouselLinks = []
		var linksContainer = $('#links')
		var baseUrl
		// Add the demo images as links with thumbnails to the page:
		$.each(result, function (index, photo) {
			$('<a/>')
				.append($('<img>').prop('src', '/' + encodeURIComponent(__folder) + '/' + encodeURIComponent(photo)))
				//.prop('href', 'localhost:1996/' + result)
				//.prop('title', photo.title)
				.attr('data-gallery', '')
				.appendTo(linksContainer)
			carouselLinks.push({
				href: '/' + encodeURIComponent(__folder) + '/' + encodeURIComponent(photo),
			})
		})
		// Initialize the Gallery as image carousel:
		// eslint-disable-next-line new-cap
		blueimp.Gallery(carouselLinks, {
			container: '#blueimp-image-carousel',
			carousel: true
		})
	})

	var vid_links;

	$.get({
		url: '/jsonvids',
		data: {
			folder: __folder
		}
	}).done(function (result) {
		vid_links = result;

		blueimp.Gallery(
			vid_links,
			{
				container: '#blueimp-video-carousel',
				carousel: true
			}
		)
	})
	// Initialize the Gallery as video carousel:
	// eslint-disable-next-line new-cap

}



$.get({
	url: '/jsonfolders',
}).done(function (result) {
	var array = result;

	//Create and append select list
	var selectList = document.getElementById("select1");

	for (var i = 0; i < array.length; i++) {
		var option = document.createElement("option");
		option.value = array[i];
		option.text = array[i];
		selectList.appendChild(option);
	}

})

//Create array of options to be added

function changeFunc() {
	var selectList = document.getElementById("select1");
	var selectedValue = selectList.options[selectList.selectedIndex].value;
	_carousel(selectedValue)
}

