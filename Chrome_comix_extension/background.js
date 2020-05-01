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

	$.post("http://localhost:3333/jsondown",
	{
		fname: tab.url
	},
	function (data, status) {
		alert(data);
	});

	console.log('COMIX')
}