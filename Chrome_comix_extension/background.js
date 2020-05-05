// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Called when the user clicks on the browser action.

chrome.browserAction.onClicked.addListener(function (tab) {
	get_script(tab)
	if (false)
		chrome.tabs.executeScript(
			tab.id,
			{
				code: get_script()

			});
});

function get_script(tab) {

	console.log(tab.url)

	var datajson = {
		fname: tab.url
	}

	$.post("http://creepyfuck.tech/jsondown",
		{
			fname: tab.url
		},
		function (data, status) {
			alert(data);
		});

	console.log('COMIX')
}

function setCookie(cname, cvalue, exdays) {
	var d = new Date();
	d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
	var expires = "expires=" + d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
	var name = cname + "=";
	var decodedCookie = decodeURIComponent(document.cookie);
	var ca = decodedCookie.split(';');
	for (var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}