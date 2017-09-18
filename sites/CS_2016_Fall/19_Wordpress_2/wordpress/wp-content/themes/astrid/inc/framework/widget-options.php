<?php
/**
 * Custom widget options
 *
 * @package Astrid
 */

class Atframework_Widget_Options {

  public function __construct() {

    add_action( 'in_widget_form', array( $this, 'widget_form' ), 1, 3 );
    add_action( 'admin_enqueue_scripts', array( $this, 'widget_color_picker' ), 10, 2 );
    add_filter( 'widget_update_callback', array( $this, 'widget_update'), 10, 2 );
    add_filter( 'dynamic_sidebar_params', array( $this, 'widget_output'), 99, 2 );
    
  }

  /**
   * Extra form fields
   */
  public function widget_form( $widget, $args, $instance ) {

    $background_color   = isset( $instance['background_color'] ) ? esc_attr( $instance['background_color'] ) : '';
    $text_color         = isset( $instance['text_color'] ) ? esc_attr( $instance['text_color'] ) : '';
    $widget_title_color = isset( $instance['widget_title_color'] ) ? esc_attr( $instance['widget_title_color'] ) : '';
    $image_uri          = isset( $instance['image_uri'] ) ? esc_url($instance['image_uri']) : '';    
    $sectionId          = isset( $instance['sectionId'] ) ? esc_attr($instance['sectionId']) : '';   
		$column_width 	    = isset( $instance['column_width'] ) ? esc_attr( $instance['column_width'] ) : '';
    $padding            = isset( $instance['padding'] ) ? intval( $instance['padding'] ) : '100';
    $no_container       = isset( $instance['no_container'] ) ? (bool) $instance['no_container'] : false;

  ?>

    <div class="at-styling-options">
      <h4><?php _e( 'Styling', 'astrid' ); ?><span><?php _e( 'Click to expand', 'astrid' ); ?></span></h4>
      <div class="at-styling-inner">
        <em style="font-size:12px;"><?php _e( 'Options found in this panel apply only to this widget.', 'astrid' ); ?></em>
        <p><label for="<?php echo $widget->get_field_id('sectionId'); ?>"><?php _e('Section ID', 'astrid'); ?><br></label>
        <input class="widefat" id="<?php echo $widget->get_field_id( 'sectionId' ); ?>" name="<?php echo $widget->get_field_name( 'sectionId' ); ?>" type="text" value="<?php echo $sectionId; ?>" size="3" /></p>        
        <p><label for="<?php echo $widget->get_field_id('background_color'); ?>"><?php _e('Background color', 'astrid'); ?><br></label>
        <input type="text" name="<?php echo $widget->get_field_name('background_color'); ?>" id="<?php echo $widget->get_field_id('background_color'); ?>" class="color-field" value="<?php echo $background_color; ?>" /></p>
        <p><label for="<?php echo $widget->get_field_id('text_color'); ?>"><?php _e('Text color', 'astrid'); ?><br></label>
        <input type="text" name="<?php echo $widget->get_field_name('text_color'); ?>" id="<?php echo $widget->get_field_id('text_color'); ?>" class="color-field" value="<?php echo $text_color; ?>" /></p>  
        <p><label for="<?php echo $widget->get_field_id('widget_title_color'); ?>"><?php _e('Widget title color', 'astrid'); ?><br></label>
        <input type="text" name="<?php echo $widget->get_field_name('widget_title_color'); ?>" id="<?php echo $widget->get_field_id('widget_title_color'); ?>" class="color-field" value="<?php echo $widget_title_color; ?>" /></p>       
        <p><label for="<?php echo $widget->get_field_id('image_uri'); ?>"><?php _e('Background image URL', 'astrid'); ?><br></label>
        <input class="widefat" id="<?php echo $widget->get_field_id( 'image_uri' ); ?>" name="<?php echo $widget->get_field_name( 'image_uri' ); ?>" type="text" value="<?php echo $image_uri; ?>" size="3" /></p>
        <p>
        <label for="<?php echo $widget->get_field_id('column_width'); ?>"><?php _e( 'Widget width:', 'astrid' ); ?></label>
    	  <select name="<?php echo $widget->get_field_name('column_width'); ?>" id="<?php echo $widget->get_field_id('column_width'); ?>" class="widefat">
      	<?php
      	$options = array(
      		'full' 	=> __( 'Full Width', 'astrid' ), 
      		'half' 	=> __( '1/2 Width', 'astrid' ), 
      		'third' => __( '1/3 Width', 'astrid' ), 
      	); 
      	foreach ($options as $key => $option) {
          echo '<option value="' . $key . '" id="widget-selector-' . $key . '"', $column_width == $key ? ' selected="selected"' : '', '>', esc_attr($option), '</option>';
      	}
      	?>
    	  </select>
        </p>
        <p><label for="<?php echo $widget->get_field_id('padding'); ?>"><?php _e('Top/bottom padding [px]', 'astrid'); ?><br></label>
        <input class="widefat custom_media_url" id="<?php echo $widget->get_field_id( 'padding' ); ?>" name="<?php echo $widget->get_field_name( 'padding' ); ?>" type="text" value="<?php echo $padding; ?>" size="3" /></p>        
        <p><input class="checkbox" type="checkbox" <?php checked( $no_container ); ?> id="<?php echo $widget->get_field_id( 'no_container' ); ?>" name="<?php echo $widget->get_field_name( 'no_container' ); ?>" />
        <label for="<?php echo $widget->get_field_id( 'no_container' ); ?>"><?php _e( 'Remove container?', 'astrid' ); ?></label></p>        
      </div>   
    </div>

    <script>
      jQuery(function($) {
        $( '.at-styling-options h4 span' ).click(function() {
          $( '.at-styling-inner' ).slideToggle();
          $(this).html($(this).text() == 'Click to hide' ? 'Click to expand' : 'Click to hide');
        }); 
      });   
    </script>

  <?php
  }

  /**
   * Update callback
   */
  public function widget_update ( $instance, $new_instance ) {
    $instance['sectionId']          = sanitize_text_field($new_instance['sectionId']);
    $instance['background_color']   = sanitize_text_field( $new_instance['background_color'] );
    $instance['text_color']         = sanitize_text_field( $new_instance['text_color'] );
    $instance['widget_title_color'] = sanitize_text_field( $new_instance['widget_title_color'] );    
	  $instance['column_width']       = sanitize_text_field($new_instance['column_width']);
    $instance['image_uri']          = esc_url_raw($new_instance['image_uri']);
    $instance['padding']            = absint($new_instance['padding']);
    $instance['no_container']       = (bool)($new_instance['no_container']);

    return $instance;
  }

  /**
   * Widget output
   */
  public function widget_output( $params ) {
    if (is_admin())
      return $params;

    global $wp_registered_widgets;
    $id = $params[0]['widget_id'];

    if (isset($wp_registered_widgets[$id]['callback'][0]) && is_object($wp_registered_widgets[$id]['callback'][0])) {
      $settings           = $wp_registered_widgets[$id]['callback'][0]->get_settings();
      $instance           = $settings[substr( $id, strrpos( $id, '-' ) + 1 )];
      $sectionId          = isset( $instance['sectionId'] ) ? esc_attr($instance['sectionId']) : '';
      $bg_color 		      = isset($instance['background_color']) ? $instance['background_color'] : null;
      $text_color 	      = isset($instance['text_color']) ? $instance['text_color'] : null;
      $widget_title_color = isset($instance['widget_title_color']) ? $instance['widget_title_color'] : null;      
	    $column_width       = isset( $instance['column_width'] ) ? esc_attr($instance['column_width']) : __( 'Full Width', 'astrid' );
      $image_uri          = isset( $instance['image_uri'] ) ? esc_url($instance['image_uri']) : '';
      $padding            = isset( $instance['padding'] ) ? intval($instance['padding']) : '100';
      $no_container       = isset( $instance['no_container'] ) ? $instance['no_container'] : false;

      if ($text_color) {
        $inherit = 'inherit';
      } else {
        $inherit = 'noinherit';
      }
      if ($sectionId) {
        $id =  ' id="' . $sectionId . '"';
      } else {
        $id = '';
      }


      $params[0]['before_widget'] = str_replace('<section', '<section' . $id . ' data-color="' . $inherit . '" style="color:' . $text_color . ';background-color:' . $bg_color . ';padding-top:' . $padding . 'px;padding-bottom:' . $padding . 'px;background-image:url(' . $image_uri . ');"', $params[0]['before_widget']);
      if ($image_uri) {
        $params[0]['before_widget'] = str_replace('<div class="atblock', '<div class="row-overlay"></div><div class="atblock', $params[0]['before_widget']);
      }
      if ($no_container) {
        $params[0]['before_widget'] = str_replace('<div class="atblock container', '<div class="atblock no-container', $params[0]['before_widget']);
      }
      if ($column_width == 'half') {
        $params[0]['before_widget'] = str_replace('class="widget', 'class="widget clearfix at-2-col', $params[0]['before_widget']);
      } elseif ($column_width == 'third') {
        $params[0]['before_widget'] = str_replace('class="widget', 'class="widget clearfix at-3-col', $params[0]['before_widget']);        	
      }
      $params[0]['before_title'] = str_replace('<h2 class="widget-title"', '<h2 class="widget-title" style="color:' . $widget_title_color . ';"', $params[0]['before_title']);

    }

    return $params;
  }

  /**
   * Color picker
   */  
  public function widget_color_picker( $hook ) {
    if ( ( 'customize.php' != $hook ) && ( 'widgets.php' != $hook ) ) {
      return;
    }     
    wp_enqueue_style( 'wp-color-picker' );     
    wp_enqueue_script( 'astrid-picker', get_template_directory_uri() . '/inc/framework/js/colorpicker.js', array( 'wp-color-picker' ), false, true );  
  }

}

new Atframework_Widget_Options();