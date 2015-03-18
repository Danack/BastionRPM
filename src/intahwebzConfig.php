<?php

$files = [
    [
        "dest" => "/etc/supervisord.d/logBackground.supervisord.conf",
        "src" => "/autogen/logBackground.supervisord.conf"
    ],
    [
        "dest" => "/etc/nginx/sites-enabled/basereality.nginx.conf",
        "src" => "/autogen/basereality.nginx.conf"
    ],
    [
        "dest" => "/etc/php-fpm.d/basereality.php-fpm.conf",
        "src" => "/autogen/basereality.php-fpm.conf"
    ],
    [
        "dest" => "/etc/php-fpm.d/intahwebz.php-fpm.conf",
        "src" => "/autogen/intahwebz.php-fpm.conf"
    ],
    [
        "dest" => "/etc/nginx/sites-enabled/intahwebz.nginx.conf",
        "src" => "/autogen/intahwebz.nginx.conf"
    ],
];




$srcFiles=["composer.json", "composer.lock" ];


$srcDirectories = [ "basereality", "conf", "data", "fonts", "intahwebz", "lib", "node", "scripts", "src", "templates", "tools", "vendor"];


$dataDirectoryDefinitions = [
    [
        'mode' => 0775,
        'dirs' => [ "var", "var/cache", "var/log", "var/log/php-fpm", "var/log/nginx", "var/cache/wsdl", "var/files",  "var/compile/templates/", "var/session/", "var/src/"
        ],
        'user' => 'intahwebz',
        'group' => 'www-data'
    ]
];

$crontab = [
    "conf/backup_crontab"
];


$config = [
    'files' => $files,
    'srcFiles' => $srcFiles,
    'srcDirectories' => $srcDirectories,
    'dataDirectoryDefinitions' => $dataDirectoryDefinitions,
    'crontab' => $crontab
];
 

return $config;