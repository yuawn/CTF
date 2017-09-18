<?php
/*
Template Name: Widgetized
*/

get_header(); ?>

	<div id="primary" class="fullwidth">
		<main id="main" class="site-main" role="main">

			<?php global $post; ?>
			<?php $slug = $post->post_name; ?>
			<?php if ( is_active_sidebar( 'widget-area-' . $slug ) ) : ?>
		 		<?php dynamic_sidebar( 'widget-area-' . $slug ); ?>
			<?php endif; ?>

		</main><!-- #main -->
	</div><!-- #primary -->

<?php get_footer(); ?>
