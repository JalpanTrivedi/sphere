$(document).ready(function () {
    "use strict";

	//Revolution Slider
	jQuery('#rev_slider_1').show().revolution({
		/* Options are 'auto', 'fullwidth' or 'fullscreen' */
		sliderLayout: 'auto',
		gridwidth: 1140,
		gridheight: 850,
		/* Navigation arrows and bullets */
		navigation: {
			arrows: {
				enable: true,
        style: 'hermes',
        tmp: '<div class="tp-arr-allwrapper"><div class="tp-arr-imgholder"></div><div class="tp-arr-titleholder">{{title}}</div></div>',
				hide_onleave: false,
				hide_onmobile: true,
				hide_under: 480
			}
		}
	});

});
