<?php
/**
 * @package Astrid
 */

//Converts hex colors to rgba for the menu background color
function astrid_hex2rgba($color, $opacity = false) {

        if ($color[0] == '#' ) {
        	$color = substr( $color, 1 );
        }
        $hex = array( $color[0] . $color[1], $color[2] . $color[3], $color[4] . $color[5] );
        $rgb =  array_map('hexdec', $hex);
        $opacity = 0.9;
        $output = 'rgba('.implode(",",$rgb).','.$opacity.')';

        return $output;
}


//Dynamic styles
function astrid_custom_styles($custom) {

	$custom = '';



	//Menu style
	$sticky_menu = get_theme_mod('sticky_menu','sticky');
	if ($sticky_menu == 'static') {
		$custom .= ".site-header.has-header { position: absolute;background-color:transparent;padding:15px 0;}"."\n";
		$custom .= ".site-header.header-scrolled {padding:15px 0;}"."\n";
		$custom .= ".header-clone {display:none;}"."\n";
	} else {
		$custom .= ".site-header {position: fixed;}"."\n";
	}

	$menu_style = get_theme_mod('menu_style','inline');
	if ($menu_style == 'centered') {
		$custom .= ".site-header .container { display: block;}"."\n";
		$custom .= ".site-branding { width: 100%; text-align: center;margin-bottom:15px;padding-top:15px;}"."\n";
		$custom .= ".main-navigation { width: 100%;float: none;}"."\n";
		$custom .= ".main-navigation ul { float: none;text-align:center;}"."\n";
		$custom .= ".main-navigation li { float: none; display: inline-block;}"."\n";
		$custom .= ".main-navigation ul ul li { display: block; text-align: left;}"."\n";
	}


	//Primary color
	$primary_color = get_theme_mod( 'primary_color', '#fcd088' );
	if ( $primary_color != '#fcd088' ) {
		$custom .= ".woocommerce .woocommerce-message:before,.woocommerce #payment #place_order,.woocommerce-page #payment #place_order,.woocommerce .cart .button, .woocommerce .cart input.button,.woocommerce-cart .wc-proceed-to-checkout a.checkout-button,.woocommerce #review_form #respond .form-submit input,.woocommerce a.button,.woocommerce div.product form.cart .button,.woocommerce .star-rating,.page-header .page-title .fa,.site-footer a:hover,.footer-info a:hover,.footer-widgets a:hover,.testimonial-title a:hover,.employee-title a:hover,.fact .fa,.service-title a:hover,.widget-area .widget a:hover,.entry-meta a:hover,.entry-footer a:hover,.entry-title a:hover,.comment-navigation a:hover,.posts-navigation a:hover,.post-navigation a:hover,.main-navigation a:hover,.main-navigation li.focus > a,a,a:hover,button,.button,input[type=\"button\"],input[type=\"reset\"],input[type=\"submit\"] { color:" . esc_attr($primary_color) . "}"."\n";
		$custom .= ".social-menu-widget a,.woocommerce span.onsale,.woocommerce #payment #place_order:hover, .woocommerce-page #payment #place_order:hover,.woocommerce .cart .button:hover, .woocommerce .cart input.button:hover,.woocommerce-cart .wc-proceed-to-checkout a.checkout-button:hover,.woocommerce #review_form #respond .form-submit input:hover,.woocommerce div.product form.cart .button:hover,.woocommerce a.button:hover,.preloader-inner ul li,.progress-animate,button:hover,.button:hover,input[type=\"button\"]:hover,input[type=\"reset\"]:hover,input[type=\"submit\"]:hover { background-color:" . esc_attr($primary_color) . "}"."\n";
		$custom .= ".woocommerce .woocommerce-message,.woocommerce #payment #place_order,.woocommerce-page #payment #place_order,.woocommerce .cart .button, .woocommerce .cart input.button,.woocommerce-cart .wc-proceed-to-checkout a.checkout-button,.woocommerce #review_form #respond .form-submit input,.woocommerce a.button,.woocommerce div.product form.cart .button,.main-navigation li a::after,.main-navigation li a::before,button,.button,input[type=\"button\"],input[type=\"reset\"],input[type=\"submit\"] { border-color:" . esc_attr($primary_color) . "}"."\n";
	}

	$site_title = get_theme_mod( 'site_title', '#ffffff' );
	$custom .= ".site-title a,.site-title a:hover { color:" . esc_attr($site_title) . "}"."\n";
	$site_desc = get_theme_mod( 'site_description', '#BDBDBD' );
	$custom .= ".site-description { color:" . esc_attr($site_desc) . "}"."\n";

	$menu_bg    = get_theme_mod( 'menu_bg', '#202529' );
	$menu_rgba 	= astrid_hex2rgba($menu_bg, 0.9);
	$custom .= ".site-header,.site-header.header-scrolled { background-color:" . esc_attr($menu_rgba) . "}"."\n";

	$body_text = get_theme_mod( 'body_text_color', '#656D6D' );
	$custom .= "body, .widget-area .widget, .widget-area .widget a { color:" . esc_attr($body_text) . "}"."\n";

	$footer_bg = get_theme_mod( 'footer_bg', '#202529' );
	$custom .= ".footer-widgets, .site-footer, .footer-info { background-color:" . esc_attr($footer_bg) . "}"."\n";


	//Fonts
	$body_fonts 	= get_theme_mod('body_font_family', 'font-family: \'Open Sans\', sans-serif;');
	$headings_fonts = get_theme_mod('headings_font_family', 'font-family: \'Josefin Sans\', sans-serif;');
	$custom 		.= "body {" . wp_kses_post($body_fonts) . "}"."\n";
	$custom 		.= "h1, h2, h3, h4, h5, h6, .fact .fact-number, .fact .fact-name {" . wp_kses_post($headings_fonts) . "}"."\n";

    $site_title_size = get_theme_mod( 'site_title_size', '36' );
    $custom .= ".site-title { font-size:" . intval($site_title_size) . "px; }"."\n";
    $site_desc_size = get_theme_mod( 'site_desc_size', '14' );
    $custom .= ".site-description { font-size:" . intval($site_desc_size) . "px; }"."\n";

	$h1_size = get_theme_mod( 'h1_size', '36' );
	$custom .= "h1 { font-size:" . intval($h1_size) . "px; }"."\n";
    $h2_size = get_theme_mod( 'h2_size', '30' );
    $custom .= "h2 { font-size:" . intval($h2_size) . "px; }"."\n";
    $h3_size = get_theme_mod( 'h3_size', '24' );
    $custom .= "h3 { font-size:" . intval($h3_size) . "px; }"."\n";
    $h4_size = get_theme_mod( 'h4_size', '16' );
    $custom .= "h4 { font-size:" . intval($h4_size) . "px; }"."\n";
    $h5_size = get_theme_mod( 'h5_size', '14' );
    $custom .= "h5 { font-size:" . intval($h5_size) . "px; }"."\n";
    $h6_size = get_theme_mod( 'h6_size', '12' );
    $custom .= "h6 { font-size:" . intval($h6_size) . "px; }"."\n";
    $body_size = get_theme_mod( 'body_size', '14' );
    $custom .= "body { font-size:" . intval($body_size) . "px; }"."\n";

	//Output all the styles
	wp_add_inline_style( 'astrid-style', $custom );	
}
add_action( 'wp_enqueue_scripts', 'astrid_custom_styles' );