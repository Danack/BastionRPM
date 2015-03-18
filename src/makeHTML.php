<?php

//make it look more like 
//http://www.imagemagick.org/download/linux/CentOS/x86_64/

function formatBytes($bytes, $precision = 2) {
    $units = array('B', 'KB', 'MB', 'GB', 'TB');

    $bytes = max($bytes, 0);
    $pow = floor(($bytes ? log($bytes) : 0) / log(1024));
    $pow = min($pow, count($units) - 1);

    // Uncomment one of the following alternatives
    $bytes /= pow(1024, $pow);
    // $bytes /= (1 << (10 * $pow)); 

    return round($bytes, $precision) . ' ' . $units[$pow];
}

/**
 * @param $directory
 * @param $files
 */
function writeHTMLFiles($directory, $files) {

    echo "Processing ".$directory."\n";
    
    $excludeFiles = [
        ".DS_Store",
        "sign.time",
        "index.html",
        "."
    ];
    
    $contents = <<< END
<html>
<body>
<table>

    <tr>
        <th align='left'>Filename</th>
        <th align='right'>Last modified</th>
        <th align='right' style='padding-left: 100px'>Size</th>
    </tr>

END;

    foreach ($files as $file) {
//        if ($file === "index.html") {
//            continue;
//        }
//        if ($file === ".") {
//            continue;
//        }
        if (in_array($file, $excludeFiles) == true) {
            continue;
        }

        if ($file === "..") {
            $contents .= "<tr><td colspan='3'>";
            $contents .= "<a href='..'>Parent Directory</a>";
            $contents .= "</td></tr>";
        }
        else {
            $contents .= "<tr><td>";
            $filename = $directory.'/'.$file;
            $file = htmlentities($file);

            $contents .= "<a href='$file'>$file</a>";
            $contents .= "</td><td>";
            $contents .= date("j-M-Y H:i", filemtime($filename));
            $contents .= "</td><td align='right'>";
            if (is_dir($filename) == false) {
                $contents .= formatBytes(filesize($filename));
            }
            $contents .= "</td></tr>";
        }
    }
    
    $contents .= <<< END
    
    </table>
    
</body>
</html>

END;

    file_put_contents($directory."/index.html", $contents);
}


/**
 * @param $directory
 * @param bool $root
 */
function generateHTMLForDirectory($directory, $root = true) {

    $files = [];

    $directoryIterator = new DirectoryIterator($directory);

    foreach ($directoryIterator as $item) {
        if ($item->isDir()) {
            if ($item->isDot() == false) {
                generateHTMLForDirectory($item->getRealPath(), false);
            }
        }
        
        if ($root == false || $item->isDot() == false) {
            $files[] = $item->getFilename();
        }
    }

    writeHTMLFiles($directory, $files);
}

generateHTMLForDirectory('../repo');
