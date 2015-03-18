<?php

$specConfig = require_once "intahwebzConfig.php";


$projectName = 'intahwebz';
$version = "1.2.3";
$unmangledVersion = "1.2.3";
$release = 1;
$summary = "Teh intahwebz";

#$prepScript = "%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}";
$prepScript = "%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}";


$installDir = "/home/intahwebz/intahwebz-1.2.3/";
$installDirDest = "\$RPM_BUILD_ROOT/home/intahwebz/intahwebz-1.2.3/";


$prepScript = "
%{__mkdir} -p \$RPM_BUILD_ROOT/home/intahwebz/intahwebz-1.2.3
#cp -R intahwebz-master/* $installDir
";



$buildScript = "";

$filesMacro = "%files
%defattr(555,intahwebz,www-data)
";

$installScript = "";


if (count($specConfig['crontab'])) {
    $buildScript .= "mkdir -p \$RPM_BUILD_ROOT/etc/crond.d\n";
}

foreach ($specConfig['crontab'] as $crontabEntry) {
    $buildScript .= "cp \$RPM_BUILD_DIR/$crontabEntry \$RPM_BUILD_ROOT/etc/crond.d\n";
    $filepart = basename($crontabEntry);
    $filesMacro .= "/etc/crond.d/$filepart\n";
}


foreach ($specConfig['files'] as $file) {
    $src = $file["src"];
    $dest = $file["dest"];
    
    $dirname = dirname($dest);
    $buildScript .= "mkdir -p \$RPM_BUILD_ROOT/$dirname\n";
    $buildScript .= "cp \$RPM_BUILD_DIR/$src \$RPM_BUILD_ROOT/$dest \n";

    //todo - adjut attr
    $filesMacro .= "$dest\n";
}


$cleanScript = "rm -rf \$RPM_BUILD_ROOT";

foreach ($specConfig['dataDirectoryDefinitions'] as $dataDirectoryDefinition) {

    $modeString = "-";
    if(isset($dataDirectoryDefinition['mode'])) {
        $mode = $dataDirectoryDefinition['mode'];
        $modeString = sprintf("0%o", $mode);
    }
    
    $directories = $dataDirectoryDefinition['dirs'];
    $user = $dataDirectoryDefinition['user'];
    $group = $dataDirectoryDefinition['group'];
    
    $mode = "%attr($modeString, $user, $group) ";
    
    foreach ($directories as $directory) {
        $buildScript .= "mkdir -p \$RPM_BUILD_ROOT/$installDir/$directory \n";
        $filesMacro .= "$mode %dir $installDir/$directory\n";
    }
}

foreach ($specConfig['srcDirectories'] as $srcDirectory) {
    $filesMacro .= "$installDir/$srcDirectory/*\n";
    $buildScript .= "mkdir -p \$RPM_BUILD_ROOT/$installDir/$srcDirectory \n";
    $buildScript .= "cp -R \$RPM_BUILD_DIR/$srcDirectory/* \$RPM_BUILD_ROOT/$installDir/$srcDirectory/ \n";
}

foreach ($specConfig['srcFiles'] as $srcFile) {
    $filesMacro .= "$installDir/$srcFile\n";
    $buildScript .= "cp \$RPM_BUILD_DIR/$srcFile \$RPM_BUILD_ROOT/$installDir/$srcFile \n";
}


    
//    - Got rid of Medusa hashbang headers in various files to ease RPM
//  packaging.

$license = null;
$licenseString = "License: None";

if ($license) { 
    $licenseString = "License: $license)";
}

$fullDescription = "This is my website";

//Requires:  meld3
//Url: http://supervisord.org/
//Vendor: Mike Naberezny <mike@naberezny.com>


//#%__os_install_post        \
//#      /usr/lib/rpm/brp-compress \
//#      /usr/lib/rpm/brp-strip
//#%{nil}
//#%define __os_install_post /usr/lib/rpm/brp-compress

//# Don't try fancy stuff like debuginfo, which is useless on binary-only
//# packages. Don't strip binary too
//# Be sure buildpolicy set to do nothing
//#%define        __spec_install_post %{nil}
//#%define          debug_package %{nil}
//#%define        __os_install_post %{_dbpath}/brp-compress


//%__os_install_post %{nil}


$specContents = <<< END


%define name $projectName
%define version $version 
%define unmangled_version $unmangledVersion
%define unmangled_version $unmangledVersion
%define release $release

Summary: $summary
Name: %{name}
Version: %{version}
Release: %{release}
#Source0: %{name}-%{unmangled_version}.tar.gz
$licenseString
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
AutoReqProv: no

%description
$fullDescription

%prep
$prepScript

%build
$buildScript

%install
$installScript

%clean
$cleanScript

$filesMacro

END;


file_put_contents("./build/SPECS/intahwebz.spec", $specContents);