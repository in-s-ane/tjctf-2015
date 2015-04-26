<?php
function getDirectoryList ($directory) {
    $results = "";

    // create a handler for the directory
    $handler = opendir($directory);

    // open directory and walk through the filenames
    while ($file = readdir($handler)) {

      // if file isn't this directory or its parent, add it to the results
      if ($file != "." && $file != "..") {
        $results .= $file . "<br>";
      }

    }

    // tidy up: close the handler
    closedir($handler);

    return $results;
}

echo getDirectoryList("..");

?>
