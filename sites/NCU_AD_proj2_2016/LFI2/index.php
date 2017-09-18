<!DOCTYPE html>
<html>
  <head>

    <title>A&D CTF</title>

    <link href="styles.css" type="text/css" rel="stylesheet" media="screen" title="Main Stylesheet"/>
    <link href="styles_alt.css" type="text/css" rel="stylesheet alternative"
          media="screen" title="Alternative Stylesheet"/>

  </head>
  <body>

      <div class="banner">
        <table class="banner" summary="Banner" cellpadding="0" cellspacing="0">
          <caption class="none_display">&nbsp;</caption>
          <tbody>
            <tr>
              <td>
                <span id="headerBigTitle">&nbsp;&nbsp; The Attack and Defense of Computers CTF</span>
              </td>
            </tr>
            <tr>
              <td>
                <span id="headerSubTitle">Try the &quot;Local&nbsp;File&nbsp;Inclusion&quot; Problem</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <hr />

      <div id="menuBar">
        <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <a href="index.php" class="active_bar">
          .:- Home
        </a>
        &nbsp;&nbsp;&nbsp;
        <a href="index.php?page=test" class="passive_bar">
          .:- Test
        </a>
        &nbsp;&nbsp;&nbsp;
        <a href="index.php?page=content" class="passive_bar">
          .:- Content
        </a>
        &nbsp;&nbsp;&nbsp;
      </div>

      <hr />
      <div>
        <br/>
      </div>
      <div>
        <?php

            if (!isset($_GET['page'])){
              die("This is HOME page");
            }
            else{

              $page = $_GET['page'];

              if (strpos($page, '../') != False)
                die('Please leave here!');

              if (strpos($page, './') != False)
                die('Please leave here!');

              $page = $page . '.php';

//              if (!file_exists($page))
//                  die("File not found");

              include( $page );

              // the flag is AD{PHp_Wr4pp3r_r0ck5}

            }


        ?>
      </div>

      <hr />


    </div>

  </body>
</html>
