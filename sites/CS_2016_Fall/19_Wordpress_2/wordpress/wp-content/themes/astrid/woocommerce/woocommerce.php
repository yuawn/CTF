<?php
/**
 * Woocommerce Compatibility 
 *
 * @package Astrid
 */


if ( !class_exists('WooCommerce') )
    return;

/**
 * Declare support
 */
add_theme_support( 'woocommerce' );

/**
 * Add and remove actions
 */
function astrid_woo_actions() {
    remove_action( 'woocommerce_before_main_content', 'woocommerce_output_content_wrapper', 10);
    remove_action( 'woocommerce_after_main_content', 'woocommerce_output_content_wrapper_end', 10);
    add_action('woocommerce_before_main_content', 'astrid_wrapper_start', 10);
    add_action('woocommerce_after_main_content', 'astrid_wrapper_end', 10);
}
add_action('wp','astrid_woo_actions');

/**
 * Archive titles
 */
function astrid_woo_archive_title() {
    echo '<h3 class="entry-title">';
    echo woocommerce_page_title();
    echo '</h3>';
}
add_filter( 'woocommerce_show_page_title', 'astrid_woo_archive_title' );

/**
 * Theme wrappers
 */
function astrid_wrapper_start() {
    echo '<div id="primary" class="content-area">';
        echo '<main id="main" class="site-main" role="main">';
}

function astrid_wrapper_end() {
        echo '</main>';
    echo '</div>';
}

/**
 * Number of columns per row
 */
function astrid_shop_columns() {
    return 3;
}
add_filter('loop_shop_columns', 'astrid_shop_columns');

/**
 * Number of related products
 */
function astrid_related_products_args( $args ) {
    $args['posts_per_page'] = 3;
    $args['columns'] = 3;
    return $args;
}
add_filter( 'woocommerce_output_related_products_args', 'astrid_related_products_args' );