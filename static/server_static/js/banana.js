$(function(){
	var calculate = function(){
		var windowHeight = $(window).height();
		var windowScroll = $(window).scrollTop()
		var windowScrollPos =  windowScroll + windowHeight;
		var documentHeight = $(document).height();
		
		var percentageScrolled = windowScroll / windowHeight * 100;
		var percentageFold = 100 - percentageScrolled;

		var head = $("head");
		var unpeel = percentageScrolled;
		var fold = percentageFold;
		var slide = ((percentageScrolled*2)-100)* -1;

		var styleTemplate = `
			#unpeeled {
				clip-path: polygon(0% ${fold}%, 100% ${fold}%, 100% 100%, 0% 100%);
			}
			#fold {
				transform: translateY(${slide}%);
				clip-path: polygon(0% ${unpeel}%, 100% ${unpeel}%, 100% 100%, 0% 100%);
			}`;

		if ( !head.find("#peel").length) {
			head.append('<style id="peel">${styleTemplate}</style>');
		} else {
			$("#peel").html(styleTemplate)
		}
	}
	$(window).scroll(function() {
		calculate();
	});	
	$("html, body").animate({ scrollTop: $(document).height() }, 0);
});
