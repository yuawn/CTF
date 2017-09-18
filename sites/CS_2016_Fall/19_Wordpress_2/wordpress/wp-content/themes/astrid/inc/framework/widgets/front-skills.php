<?php

if ( !class_exists('Atframework_Skills') ) {
class Atframework_Skills extends WP_Widget {

	public function __construct() {
		$widget_ops = array('classname' => 'atframework_skills_widget', 'description' => __( 'Show your visitors some of your skills.', 'astrid') );
        parent::__construct(false, $name = __('Astrid FP: Skills', 'astrid'), $widget_ops);
		$this->alt_option_name = 'atframework_skills_widget';
    }
	
	function form($instance) {
		$title     			= isset( $instance['title'] ) ? esc_attr( $instance['title'] ) : '';
		$skill_one   		= isset( $instance['skill_one'] ) ? esc_html( $instance['skill_one'] ) : '';
		$skill_one_max   	= isset( $instance['skill_one_max'] ) ? absint( $instance['skill_one_max'] ) : '';
		$skill_two   		= isset( $instance['skill_two'] ) ? esc_attr( $instance['skill_two'] ) : '';
		$skill_two_max   	= isset( $instance['skill_two_max'] ) ? absint( $instance['skill_two_max'] ) : '';
		$skill_three   		= isset( $instance['skill_three'] ) ? esc_attr( $instance['skill_three'] ) : '';
		$skill_three_max 	= isset( $instance['skill_three_max'] ) ? absint( $instance['skill_three_max'] ) : '';
		$skill_four   		= isset( $instance['skill_four'] ) ? esc_attr( $instance['skill_four'] ) : '';		
		$skill_four_max  	= isset( $instance['skill_four_max'] ) ? absint( $instance['skill_four_max'] ) : '';
		$skill_five   		= isset( $instance['skill_five'] ) ? esc_attr( $instance['skill_five'] ) : '';		
		$skill_five_max  	= isset( $instance['skill_five_max'] ) ? absint( $instance['skill_five_max'] ) : '';		
	?>

	<p>
	<label for="<?php echo $this->get_field_id('title'); ?>"><?php _e('Title', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('title'); ?>" name="<?php echo $this->get_field_name('title'); ?>" type="text" value="<?php echo $title; ?>" />
	</p>

	<!-- skill one -->
	<p>
	<label for="<?php echo $this->get_field_id('skill_one'); ?>"><?php _e('First skill name', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_one'); ?>" name="<?php echo $this->get_field_name('skill_one'); ?>" type="text" value="<?php echo $skill_one; ?>" />
	</p>

	<p>
	<label for="<?php echo $this->get_field_id('skill_one_max'); ?>"><?php _e('First skill value', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_one_max'); ?>" name="<?php echo $this->get_field_name('skill_one_max'); ?>" type="text" value="<?php echo $skill_one_max; ?>" />
	</p>

	<!-- skill two -->
	<p>
	<label for="<?php echo $this->get_field_id('skill_two'); ?>"><?php _e('Second skill name', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_two'); ?>" name="<?php echo $this->get_field_name('skill_two'); ?>" type="text" value="<?php echo $skill_two; ?>" />
	</p>

	<p>
	<label for="<?php echo $this->get_field_id('skill_two_max'); ?>"><?php _e('Second skill value', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_two_max'); ?>" name="<?php echo $this->get_field_name('skill_two_max'); ?>" type="text" value="<?php echo $skill_two_max; ?>" />
	</p>	

	<!-- skill three -->
	<p>
	<label for="<?php echo $this->get_field_id('skill_three'); ?>"><?php _e('Third skill name', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_three'); ?>" name="<?php echo $this->get_field_name('skill_three'); ?>" type="text" value="<?php echo $skill_three; ?>" />
	</p>

	<p>
	<label for="<?php echo $this->get_field_id('skill_three_max'); ?>"><?php _e('Third skill value', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_three_max'); ?>" name="<?php echo $this->get_field_name('skill_three_max'); ?>" type="text" value="<?php echo $skill_three_max; ?>" />
	</p>

	<!-- skill four -->
	<p>
	<label for="<?php echo $this->get_field_id('skill_four'); ?>"><?php _e('Fourth skill name', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_four'); ?>" name="<?php echo $this->get_field_name('skill_four'); ?>" type="text" value="<?php echo $skill_four; ?>" />
	</p>

	<p>
	<label for="<?php echo $this->get_field_id('skill_four_max'); ?>"><?php _e('Fourth skill value', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_four_max'); ?>" name="<?php echo $this->get_field_name('skill_four_max'); ?>" type="text" value="<?php echo $skill_four_max; ?>" />
	</p>
							
	<!-- skill five -->
	<p>
	<label for="<?php echo $this->get_field_id('skill_five'); ?>"><?php _e('Fifth skill name', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_five'); ?>" name="<?php echo $this->get_field_name('skill_five'); ?>" type="text" value="<?php echo $skill_five; ?>" />
	</p>

	<p>
	<label for="<?php echo $this->get_field_id('skill_five_max'); ?>"><?php _e('Fifth skill value', 'astrid'); ?></label>
	<input class="widefat" id="<?php echo $this->get_field_id('skill_five_max'); ?>" name="<?php echo $this->get_field_name('skill_five_max'); ?>" type="text" value="<?php echo $skill_five_max; ?>" />
	</p>

	<?php
	}

	// update widget
	function update($new_instance, $old_instance) {
		$instance = $old_instance;
		$instance['title'] 				= sanitize_text_field($new_instance['title']);
		$instance['skill_one'] 			= sanitize_text_field($new_instance['skill_one']);
		$instance['skill_one_max'] 		= intval($new_instance['skill_one_max']);
		$instance['skill_two'] 			= sanitize_text_field($new_instance['skill_two']);
		$instance['skill_two_max'] 		= intval($new_instance['skill_two_max']);
		$instance['skill_three'] 		= sanitize_text_field($new_instance['skill_three']);
		$instance['skill_three_max']	= intval($new_instance['skill_three_max']);
		$instance['skill_four'] 		= sanitize_text_field($new_instance['skill_four']);
		$instance['skill_four_max'] 	= intval($new_instance['skill_four_max']);
		$instance['skill_five'] 		= sanitize_text_field($new_instance['skill_five']);
		$instance['skill_five_max'] 	= intval($new_instance['skill_five_max']);

		$alloptions = wp_cache_get( 'alloptions', 'options' );
		if ( isset($alloptions['atframework_skills']) )
			delete_option('atframework_skills');		  
		  
		return $instance;
	}
	
	// display widget
	function widget($args, $instance) {
		$cache = array();
		if ( ! $this->is_preview() ) {
			$cache = wp_cache_get( 'atframework_skills', 'widget' );
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
		$skill_one   	= isset( $instance['skill_one'] ) ? esc_html( $instance['skill_one'] ) : '';
		$skill_one_max  = isset( $instance['skill_one_max'] ) ? absint( $instance['skill_one_max'] ) : '';
		$skill_two   	= isset( $instance['skill_two'] ) ? esc_attr( $instance['skill_two'] ) : '';
		$skill_two_max  = isset( $instance['skill_two_max'] ) ? absint( $instance['skill_two_max'] ) : '';
		$skill_three   	= isset( $instance['skill_three'] ) ? esc_attr( $instance['skill_three'] ) : '';
		$skill_three_max= isset( $instance['skill_three_max'] ) ? absint( $instance['skill_three_max'] ) : '';
		$skill_four   	= isset( $instance['skill_four'] ) ? esc_attr( $instance['skill_four'] ) : '';		
		$skill_four_max = isset( $instance['skill_four_max'] ) ? absint( $instance['skill_four_max'] ) : '';
		$skill_five   	= isset( $instance['skill_five'] ) ? esc_attr( $instance['skill_five'] ) : '';		
		$skill_five_max = isset( $instance['skill_five_max'] ) ? absint( $instance['skill_five_max'] ) : '';

		echo $args['before_widget'];
	?>

		<?php if ( $title ) echo $before_title . $title . $after_title; ?>


		<?php
		$names 	= array($skill_one, $skill_two, $skill_three, $skill_four, $skill_five);
		$values = array($skill_one_max, $skill_two_max, $skill_three_max, $skill_four_max, $skill_five_max);

		foreach (array_combine($names, $values) as $name => $value) { ?>
			<?php if ($name !='') : ?>
			<div class="skill">
	 			<div class="name"><?php echo $name; ?></div>
	            <div class="progress-bar">
					<div class="progress-animate" style="width:<?php echo $value; ?>%"></div>
				</div>
			</div>
			<?php endif; ?> 
		<?php } ?>

	<?php
		echo $args['after_widget'];

		if ( ! $this->is_preview() ) {
			$cache[ $args['widget_id'] ] = ob_get_flush();
			wp_cache_set( 'atframework_skills', $cache, 'widget' );
		} else {
			ob_end_flush();
		}
	}
	
}
}