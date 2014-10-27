var videoContainers;
window.$ = function(arg) {
	return document.querySelector(arg);
}

window.onload = function() {
	videoContainers = document.querySelectorAll('.video-container');
}

window.onresize = function() {
	var heights = [];
	for (var i = 0; i < videoContainers.length; i++) {
		heights.push(videoContainers[i].offsetHeight);
	}
	for (var i = 0; i < videoContainers.length; i++) {
		videoContainers[i].firstElementChild.height = heights[i];
	};
};
