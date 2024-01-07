/* zoomquiet's PyBlosxom need some tiny jQuery effect
 *
	usemapName=$("img[class='attachment']").attr("alt");
	//alert("#"+usemapName);
	$("img[class='attachment']").attr("usemap","#"+usemapName);
// for http://www.dvq.co.nz/wp-content/uploads/2008/07/jquery-popup-bubble/index.html
	$(".rss-popup a").hover(function() {
	$(this).next("em").stop(true, true).animate({opacity: "show", top: "-60"}, "slow");
	}, function() {
	$(this).next("em").animate({opacity: "hide", top: "-70"}, "fast");
	});
$(document).ready(function() {
// for hide tree/archive page 's losted link!
	$("a[href='/pyblosxom/file_path.html']").addClass("jQhide");
    
});
*/

