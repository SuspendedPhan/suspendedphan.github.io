var videoContainers;
window.$ = function(arg) {
	return document.querySelector(arg);
}

var resizeVideos = function () {
	var heights = [];
	for (var i = 0; i < videoContainers.length; i++) {
		heights.push(videoContainers[i].offsetHeight);
	}
	for (var i = 0; i < videoContainers.length; i++) {
		videoContainers[i].firstElementChild.height = heights[i];
	};
};

window.onload = function() {
	videoContainers = document.querySelectorAll('.video-container');
	resizeVideos();
}


window.onresize = resizeVideos;
