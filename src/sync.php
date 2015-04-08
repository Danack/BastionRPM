<?php

require_once(realpath(__DIR__).'/../vendor/autoload.php');

require_once(realpath(__DIR__).'/../../BastionRPMConfig.php');


use Aws\S3\S3Client;
use Bastion\S3Sync;
use Bastion\S3ACLNoRestrictionGenerator;

$aclGenerator = new S3ACLNoRestrictionGenerator();

if (ini_get('allow_url_fopen') == false) {
    echo "Needs to be run with allow_url_fopen enabled.";
    exit(-1);
}

if (false) {
    //Theoretically this should be used
    $syncTime = filemtime("sign.time");
    $now = time();
    if (($now - $syncTime) > 5) {
        echo "sign.time is more than 5 seconds old - the RPM files have not been signed recently, so aborting upload.";
        exit(-1);
    }
}


$urlList = [
    "/index.html",
    "/RPMS/noarch/index.html",
    "/RPMS/x86_64/index.html",
    "/RPMS/index.html",
];



$s3Client = S3Client::factory([
    'key' => $s3Key,
    'secret' => $s3Secret,
    'region' => $s3Region
]);

$s3Client->getConfig()->set('curl.options', array(CURLOPT_VERBOSE => true));

$sync = new S3Sync($rpmBucketName, $aclGenerator,  $s3Client);

$sync->putFile("../repo/index.html", "index.html");
$sync->putFile("../repo/basereality-GPG-KEY.public", "basereality-GPG-KEY.public");
$sync->syncDirectory("../repo/RPMS", "RPMS");
$sync->syncDirectory("../repo/RPMS/x86_64", "RPMS/x86_64");
$sync->syncDirectory("../repo/SRPMS", "SRPMS");
$sync->finishProcessing();