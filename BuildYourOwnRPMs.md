## Pages to open from https://github.com/danack/BastionRPM


./dirstructure
./pacakges/nginx/nginx.spec
http://rpm.basereality.com
./basereality.repo

## How to RPM stuff

* RPM is what you use when installing something through APT/YUM

* This talk is probably going to be quite boring for Windows users.

* Going to talk about why/what you should be doing at the end.

* Going to build nginx. Doesn't support plugins or extensions at runtime. Everything has to be compiled when nginx is built.

* Install rpmbuild (or rpm-tools).  

* Create the folders:

BUILD
BUILDROOT
RPMS
SOURCES
SPECS
SRPMS

* Put the source zip file and any other files that you want to package into the SOURCES directory.

* Make a spec file (aka download a spec file from the net). It has it's own weird-ass scripting language. Similar to make, and who doesn't like make?

  * %prep  - Extracts source files into BUILD directory. 
  * %setup -T -D -a 5 -n nginx-%{version}   Which means extract source 5 into the specified directory and don't empty the directory before extracting.
  * %build - Builds the build process
  * %install -  installs into the BUILDROOT directory.
  * %pre + %post - allows you to define stuff that gets run 
    when the package is installed e.g. turning on service.
  * %files  All files must be listed.
    The files should be in a sub-directory that 
    matches where they will be installed by the package.
    /foo/rpmbuild/BUILDROOT/usr/sbin/composer 

* Build the project

rpmbuild --define "_topdir `pwd`" -ba SPECS/composer.spec

The builds it into the BUILDROOT directory, not your system


* Copy it out of there into a permanent directory.

* Need to sign it - there's a tool to sign it with GPG.
rpm --resign RPMS/noarch/*.rpm
rpm --resign RPMS/x86_64/*.rpm

* Need to run createrepo. This stores a DB of all the RPMs available, what versions they are, what requirements they have etc. This allows yum/apt to know what can be installed and download it dependencies all at once.

createrepo RPMS/noarch
createrepo RPMS/x86_64

* Optional - generate html pages to make navigating the rpm site be nice.

* Upload to your server or S3 static site.

* Show rpm.basereality.com

* Add the repo to yum install in /etc/yum.d/basereality.repo

* That's it. You can now install packages.

<--- Need to get to here.

* Forget semver

It's okay for single libraries but for combinations of two different libraries how are you going to name them?
A decent naming practice is to use %PRODUCT%_%ROLE%_%DATE%_%VARIANT% e.g. thread safe.

* What you should be RPM'ing

  * To get exact version you want e.g. nginx, php
  
  * To get exact config you want, e.g. nginx error screen that has company dressing.

  * composer, any other standalone tools - RPM is a great way of making sure everyone on your team / all servers are using the same version.

  * Any thing that has frequent bug fixes - e.g. ImageMagick release every week.

  * Anything that isn't supported by repos, e.g. new libraries, or newer versions of libraries than provided by your builtin repos.


Removes complexity from chef/puppet in projects. 

* This is the reason I started RPM'ing my own stuff, the Nginx Chef script contains about 40 files of stuff, way too complex.
* Centralised place for configuring software removes cost of switching between chef/puppet/ansible/docker
* Faster deploy times if you have multiple sites as don't have to compile stuff.

* Less software needed on server e.g. don't need GCC or devel versions of software - not worth it by itself but nice side effect.

<--- Hope to get to here.


* Don't use it for complicated stuff.

ffmpeg and mysql. Both looked impossible to compile, both have usable executables availble.


* Security is kind of a joke. 
The private key has to be password protected. You're meant to use a 'cryptographically strong password' which basically means no-one can remember it, and so it needs to be written down onto a post it and attached the monitor.

Have a server that just downloads all the files from the RPM repo every few hours, and scan for changes in MD5 / sha1_file.

Subterfuge in releases is the most likely source of hacks.

*)Security - Import your private key to GPG. And magic stuff

gpg --import basereality-GPG-KEY.private

# These are to allow us to build signed rpms
sudo echo "%_signature gpg" > /root/.rpmmacros
sudo echo "" >> /root/.rpmmacros
sudo echo "%_gpg_name Dan Ackroyd" >> /root/.rpmmacros


