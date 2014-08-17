<?php

require_once(realpath(__DIR__).'/../vendor/autoload.php');

use Aws\S3\S3Client;
use Bastion\S3Sync;
use Bastion\S3ACLNoRestrictionGenerator;

$aclGenerator = new S3ACLNoRestrictionGenerator();

$s3Key = '***REMOVED***';
$s3Secret = '***REMOVED***';
$s3Region = 'eu-west-1';
$bucketName = 'satis.basereality.com';



$s3Client = S3Client::factory([
  'key' => $s3Key,
  'secret' => $s3Secret,
  'region' => $s3Region
]);

//$s3Client->getConfig()->set('curl.options', array(CURLOPT_VERBOSE => true));

$sync = new S3Sync("rpm.basereality.com", $aclGenerator,  $s3Client);

$sync->putFile("../repo/index.html", "index.html");
$sync->syncDirectory("../repo/RPMS", "RPMS");
$sync->syncDirectory("../repo/SRPMS", "SRPMS");
$sync->finishProcessing();