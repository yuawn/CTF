<?php
/**
 * The template for displaying the footer.
 *
 * Contains the closing of the #content div and all content after.
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package Astrid
 */

?>

		</div>
	</div><!-- #content -->

	<div class="footer-wrapper">
		<?php if ( is_active_sidebar( 'footer-1' ) ) : ?>
			<?php get_sidebar('footer'); ?>
		<?php endif; ?>
		
		<?php $toggle_contact = get_theme_mod('toggle_contact_footer', 1); ?>
		<?php if ( $toggle_contact ) : ?>
		<div class="footer-info">
			<div class="container">
				<?php astrid_footer_branding(); ?>
				<?php astrid_footer_contact(); ?>
			</div>
		</div>
		<?php endif; ?>

		<footer id="colophon" class="site-footer" role="contentinfo">	
			<div class="site-info container">
				<nav id="footernav" class="footer-navigation" role="navigation">
					<?php wp_nav_menu( array( 'theme_location' => 'footer', 'depth' => '1', 'menu_id' => 'footer-menu' ) ); ?>
				</nav><!-- #site-navigation -->
				<div class="site-copyright">
					<?php do_action('astrid_footer'); ?>
				</div>
			</div><!-- .site-info -->
		</footer><!-- #colophon -->
	</div>

</div><!-- #page -->

<?php wp_footer(); ?>

</body>
</html>
