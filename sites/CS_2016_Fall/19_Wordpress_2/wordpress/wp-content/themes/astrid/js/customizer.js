/**
 * customizer.js
 *
 * Theme Customizer enhancements for a better user experience.
 *
 * Contains handlers to make Theme Customizer preview reload changes asynchronously.
 */

( function( $ ) {
	// Site title and description.
	wp.customize( 'blogname', function( value ) {
		value.bind( function( to ) {
			$( '.site-title a' ).text( to );
		} );
	} );
	wp.customize( 'blogdescription', function( value ) {
		value.bind( function( to ) {
			$( '.site-description' ).text( to );
		} );
	} );
	wp.customize( 'header_text', function( value ) {
		value.bind( function( to ) {
			$( '.header-text' ).text( to );
		} );
	} );
	wp.customize( 'header_subtext', function( value ) {
		value.bind( function( to ) {
			$( '.header-subtext' ).text( to );
		} );
	} );
	wp.customize( 'header_button', function( value ) {
		value.bind( function( to ) {
			$( '.header-button' ).text( to );
		} );
	} );

	wp.customize( 'header_button_url', function( value ) {
		value.bind( function( to ) {
			if (to != '') {
				$( '.header-button' ).attr('href', to);
				$( '.header-button' ).show();
			} else {
				$( '.header-button' ).hide();				
			}
		} );
	} );

	wp.customize( 'site_title', function( value ) {
		value.bind( function( to ) {
			$( '.site-title a' ).css('color', to );
		} );
	} );
	wp.customize( 'site_description', function( value ) {
		value.bind( function( to ) {
			$( '.site-description' ).css('color', to );
		} );
	} );
	wp.customize( 'body_text_color', function( value ) {
		value.bind( function( to ) {
			$( 'body, .widget-area .widget, .widget-area .widget' ).css('color', to );
		} );
	} );		
	wp.customize( 'footer_bg', function( value ) {
		value.bind( function( to ) {
			$( '.footer-widgets, .site-footer, .footer-info' ).css('background-color', to );
		} );
	} );	

	wp.customize( 'menu_style', function( value ) {
		value.bind( function( to ) {
			if (to == 'centered') {
				$( '.site-header .container' ).css('display', 'block' );
				$( '.site-branding' ).css({'width': '100%', 'text-align': 'center', 'margin-bottom': '15px', 'padding-top': '15px'});				
				$( '.main-navigation' ).css({'width': '100%', 'float': 'none'});		
				$( '.main-navigation ul' ).css({'text-align': 'center', 'float': 'none'});		
				$( '.main-navigation li' ).css({'display': 'inline-block', 'float': 'none'});		
				$( '.main-navigation ul ul li' ).css({'display': 'block', 'text-align': 'left'});
			} else {
				$( '.site-header .container' ).css('display', '' );
				$( '.site-branding' ).css({'width': '', 'text-align': '', 'margin-bottom': '', 'padding-top': ''});			
				$( '.main-navigation' ).css({'width': '', 'float': ''});				
				$( '.main-navigation ul' ).css({'text-align': '', 'float': ''});		
				$( '.main-navigation li' ).css({'display': '', 'float': ''});		
				$( '.main-navigation ul ul li' ).css({'display': '', 'text-align': ''});
			}
		} );
	} );

	wp.customize( 'site_title_size', function( value ) {
		value.bind( function( to ) {
			$( '.site-title' ).css('font-size', to + 'px' );
		} );
	} );			
	wp.customize( 'site_desc_size', function( value ) {
		value.bind( function( to ) {
			$( '.site-description' ).css('font-size', to + 'px' );
		} );
	} );

	wp.customize( 'site_logo', function( value ) {
		var title 	= '<h1 class="site-title"><a href="#">' + wp.customize('blogname').get() + '</a></h1>';
		var desc 	= '<p class="site-description">' + wp.customize('blogdescription').get() + '</p>';
		value.bind( function( to ) {
			if (to != '') {
				$( '.site-branding' ).html('<img class="site-logo" src="' + to + '"/>');
			} else {
				$( '.site-branding' ).html(title + desc);
			}
		} );
	} );

	wp.customize('h1_size',function( value ) {
		value.bind( function( newval ) {
			$('h1').not('.site-title').css('font-size', newval + 'px' );
		} );
	});	
    wp.customize('h2_size',function( value ) {
        value.bind( function( newval ) {
            $('h2').css('font-size', newval + 'px' );
        } );
    });	
    wp.customize('h3_size',function( value ) {
        value.bind( function( newval ) {
            $('h3').css('font-size', newval + 'px' );
        } );
    });
    wp.customize('h4_size',function( value ) {
        value.bind( function( newval ) {
            $('h4').css('font-size', newval + 'px' );
        } );
    });
    wp.customize('h5_size',function( value ) {
        value.bind( function( newval ) {
            $('h5').css('font-size', newval + 'px' );
        } );
    });
    wp.customize('h6_size',function( value ) {
        value.bind( function( newval ) {
            $('h6').css('font-size', newval + 'px' );
        } );
    });
    wp.customize('body_size',function( value ) {
        value.bind( function( newval ) {
            $('body').css('font-size', newval + 'px' );
        } );
    });	

} )( jQuery );
