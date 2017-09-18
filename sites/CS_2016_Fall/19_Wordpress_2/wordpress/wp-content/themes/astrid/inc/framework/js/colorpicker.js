			( function( $ ){
				function initColorPicker( widget ) {
					widget.find( '.color-field' ).wpColorPicker( {
						change: _.throttle( function() {
							$(this).trigger( 'change' );
						}, 1500 ),

                        clear: _.throttle( function() {
							$(this).trigger( 'change' );
						}, 1500 ),



					});
				}

				function onFormUpdate( event, widget ) {
					initColorPicker( widget );
				}

				$( document ).on( 'widget-added widget-updated', onFormUpdate );

				$( document ).ready( function() {
					$( '.color-field' ).each( function () {
						initColorPicker( $( this ) );
					} );
				} );
			}( jQuery ) );
