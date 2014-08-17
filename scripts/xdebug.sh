#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../spec/php-xdebug.spec $RPM_DIR/SPECS/php-xdebug.spec
cp ../ini/xdebug.ini $RPM_DIR/SOURCES/xdebug.ini

cp ../packages/xdebug-2.2.3.tgz $RPM_DIR/SOURCES/xdebug-2.2.3.tgz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/php-xdebug.spec

cp RPMS/x86_64/xdebug-2.2.3-1.x86_64.rpm  $startDir/../repo/RPMS/x86_64/xdebug-2.2.3.x86_64.rpm
cp SRPMS/xdebug-2.2.3-1.src.rpm  $startDir/../repo/SRPMS/xdebug-2.2.3-1.src.rpm

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





