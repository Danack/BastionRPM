#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../spec/php-apcu.spec $RPM_DIR/SPECS/php-apcu.spec
cp ../ini/apcu.ini $RPM_DIR/SOURCES/apcu.ini

cp ../packages/apcu-4.0.6.tgz $RPM_DIR/SOURCES/apcu-4.0.6.tgz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/php-apcu.spec


cp RPMS/x86_64/apcu-4.0.6.x86_64.rpm $startDir/../repo/RPMS/x86_64/apcu-4.0.6.x86_64.rpm
cp RPMS/x86_64/apcu-4.0.6-1.x86_64.rpm  $startDir/../repo/RPMS/x86_64/apcu-4.0.6-1.x86_64.rpm
cp SRPMS/apcu-4.0.6-1.src.rpm  $startDir/../repo/SRPMS/apcu-4.0.6-1.src.rpm

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





