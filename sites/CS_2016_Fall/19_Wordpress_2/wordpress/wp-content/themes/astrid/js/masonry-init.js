
//Masonry init
jQuery(function($) {
	var $container = $('.posts-layout');
	$container.imagesLoaded( function() {
		$container.masonry({
			itemSelector: '.hentry',
			isFitWidth: true,
			animationOptions: {
				duration: 500,
				easing: 'linear',
			}
	    });
	});
});