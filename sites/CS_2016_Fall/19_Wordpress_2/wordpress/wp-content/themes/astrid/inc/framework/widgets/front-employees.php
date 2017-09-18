<?php
/**
 * Employees widget
 *
 * @package Astrid
 */

class Atframework_Employees extends WP_Widget {

	public function __construct() {
		$widget_ops = array('classname' => 'atframework_employees_widget', 'description' => __( 'Show your employees', 'astrid') );
        parent::__construct(false, $name = __('Astrid FP: Employees', 'astrid'), $widget_ops);
		$this->alt_option_name = 'atframework_employees_widget';
			
    }
	
	function form($instance) {
		$title     		= isset( $instance['title'] ) ? esc_attr( $instance['title'] ) : '';
		$number    		= isset( $instance['number'] ) ? intval( $instance['number'] ) : -1;
		$offset    		= isset( $instance['offset'] ) ? intval( $instance['offset'] ) : 0;
		$see_all   		= isset( $instance['see_all'] ) ? esc_url( $instance['see_all'] ) : '';		
		$see_all_text  	= isset( $instance['see_all_text'] ) ? esc_html( $instance['see_all_text'] ) : '';
		$pageids  		= isset( $instance['pageids'] ) ? esc_html( $instance['pageids'] ) : '';		
	?>

	<p><?php _e('This widget displays all pages that have the Single Employee page template assigned to them.', 'astrid'); ?></p>
	<p><em><?php _e('Tip: to rearrange the employees order, edit each employee page and add a value in Page Attributes > Order', 'astrid'); ?></em></p>
	<p>
	<label for="<?php echo $this->get_field_id('title'); ?>"><?php _e('Title', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('title'); ?>" name="<?php echo $this->get_field_name('title'); ?>" type="text" value="<?php echo $title; ?>" />
	</p>
	<p><label for="<?php echo $this->get_field_id( 'number' ); ?>"><?php _e( 'Number of employees to show (-1 shows all of them):', 'astrid' ); ?></label>
	<input id="<?php echo $this->get_field_id( 'number' ); ?>" name="<?php echo $this->get_field_name( 'number' ); ?>" type="text" value="<?php echo $number; ?>" size="3" /></p>
	<p><label for="<?php echo $this->get_field_id( 'offset' ); ?>"><?php _e( 'Offset (number of employees needs to be different than -1 for this option to work):', 'astrid' ); ?></label>
	<input id="<?php echo $this->get_field_id( 'offset' ); ?>" name="<?php echo $this->get_field_name( 'offset' ); ?>" type="text" value="<?php echo $offset; ?>" size="3" /></p>
	<p><label for="<?php echo $this->get_field_id( 'pageids' ); ?>"><?php _e( 'Page IDs to display in this widget (separated by commas, example: 14,810,220). Note: you can find the page ID in the URL bar while editing your page.', 'astrid' ); ?></label>
	<input id="<?php echo $this->get_field_id( 'pageids' ); ?>" name="<?php echo $this->get_field_name( 'pageids' ); ?>" type="text" value="<?php echo $pageids; ?>" size="3" /></p>	
    <p><label for="<?php echo $this->get_field_id('see_all'); ?>"><?php _e('The URL for your button [In case you want a button below your employees block]', 'astrid'); ?></label>
	<input class="widefat custom_media_url" id="<?php echo $this->get_field_id( 'see_all' ); ?>" name="<?php echo $this->get_field_name( 'see_all' ); ?>" type="text" value="<?php echo $see_all; ?>" size="3" /></p>	
    <p><label for="<?php echo $this->get_field_id('see_all_text'); ?>"><?php _e('The text for the button [Defaults to <em>See all our employees</em> if left empty]', 'astrid'); ?></label>
	<input class="widefat custom_media_url" id="<?php echo $this->get_field_id( 'see_all_text' ); ?>" name="<?php echo $this->get_field_name( 'see_all_text' ); ?>" type="text" value="<?php echo $see_all_text; ?>" size="3" /></p>	
	<?php
	}

	function update($new_instance, $old_instance) {
		$instance = $old_instance;
		$instance['title'] 			= sanitize_text_field($new_instance['title']);
		$instance['number'] 		= sanitize_text_field($new_instance['number']);
		$instance['offset'] 		= sanitize_text_field($new_instance['offset']);
		$instance['see_all'] 		= esc_url_raw( $new_instance['see_all'] );	
		$instance['see_all_text'] 	= sanitize_text_field($new_instance['see_all_text']);		
		$instance['pageids'] 		= sanitize_text_field($new_instance['pageids']);		
		    			
		$alloptions = wp_cache_get( 'alloptions', 'options' );
		if ( isset($alloptions['atframework_employees']) )
			delete_option('atframework_employees');		  
		  
		return $instance;
	}
	
	function widget($args, $instance) {
		$cache = array();
		if ( ! $this->is_preview() ) {
			$cache = wp_cache_get( 'atframework_employees', 'widget' );
		}

		if ( ! is_array( $cache ) ) {
			$cache = array();
		}

		if ( ! isset( $args['widget_id'] ) ) {
			$args['widget_id'] = $this->id;
		}

		if ( isset( $cache[ $args['widget_id'] ] ) ) {
			echo $cache[ $args['widget_id'] ];
			return;
		}

		ob_start();
		extract($args);

		$title 			= ( ! empty( $instance['title'] ) ) ? $instance['title'] : '';
		$title 			= apply_filters( 'widget_title', $title, $instance, $this->id_base );
		$see_all 		= isset( $instance['see_all'] ) ? esc_url($instance['see_all']) : '';
		$see_all_text 	= isset( $instance['see_all_text'] ) ? esc_html($instance['see_all_text']) : '';		
		$number 		= ( ! empty( $instance['number'] ) ) ? intval( $instance['number'] ) : -1;
		if ( ! $number )
			$number 	= -1;				
		$offset 		= ( ! empty( $instance['offset'] ) ) ? intval( $instance['offset'] ) : 0;
		$pageids		= isset( $instance['pageids'] ) ? esc_html($instance['pageids']) : '';
		if ($pageids) {
			$ids = explode(',', $pageids);
		} else {
			$ids = '';
		}

		$employees = new WP_Query( array(
			'post_type'			=> 'page',
			'no_found_rows' 	=> true,
			'post_status'   	=> 'publish',
			'orderby' 			=> 'menu_order',
			'order'   			=> 'ASC',
			'posts_per_page' 	=> $number,
			'post__in' 			=> $ids,			
			'offset'			=> $offset,
	        'meta_query' => array(
	            array(
	                'key' => '_wp_page_template',
	                'value' => 'page-templates/single-employee.php',
	            )
	        )			
		) );

		echo $args['before_widget'];

		if ($employees->have_posts()) :
?>
			<?php if ( $title ) echo $before_title . $title . $after_title; ?>

				<div class="employees-area clearfix">
					<?php while ( $employees->have_posts() ) : $employees->the_post(); ?>
						<div class="employee astrid-3col">
							<?php if ( has_post_thumbnail() ) : ?>
							<div class="employee-thumb">
								<?php the_post_thumbnail('astrid-small-thumb'); ?>
							</div>
							<?php endif; ?>
							<div class="employee-content">
								<h3 class="employee-title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
								<?php echo wp_trim_words( get_the_content(), 12 ); ?>
							</div>
						</div>
					<?php endwhile; ?>
				</div>

				<?php if ($see_all != '') : ?>
					<a href="<?php echo esc_url($see_all); ?>" class="button centered-button">
						<?php if ($see_all_text) : ?>
							<?php echo $see_all_text; ?>
						<?php else : ?>
							<?php echo __('See all our employees', 'astrid'); ?>
						<?php endif; ?>
					</a>
				<?php endif; ?>				
	<?php
		wp_reset_postdata();
		endif;
		echo $args['after_widget'];

		if ( ! $this->is_preview() ) {
			$cache[ $args['widget_id'] ] = ob_get_flush();
			wp_cache_set( 'atframework_employees', $cache, 'widget' );
		} else {
			ob_end_flush();
		}
	}
	
}