jQuery(window).on('load', function() {
    jQuery('#loader-bg').hide();
});
$( function() {
    jQuery('header').load('/ORIZIN_Agent/header_menu.html');
    jQuery('head').load('/ORIZIN_Agent/etc/html/set_icon.html');
    $( 'img.lazy' ).lazyload( {
        effect: 'fadeIn',
	effect_speed: 3000,
	skip_invisible: true,
	placeholder: '/ORIZIN_Agent/icon/805.png',
    });
});