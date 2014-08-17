#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/setuptools-3.8.1.tar.gz $RPM_DIR/SOURCES/setuptools-3.8.1.tar.gz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/setuptools.spec


#cp RPMS/x86_64/apcu-4.0.6.x86_64.rpm $startDir/../repo/RPMS/x86_64/apcu-4.0.6.x86_64.rpm
#cp RPMS/x86_64/apcu-4.0.6-1.x86_64.rpm  $startDir/../repo/RPMS/x86_64/apcu-4.0.6-1.x86_64.rpm
#cp SRPMS/apcu-4.0.6-1.src.rpm  $startDir/../repo/SRPMS/apcu-4.0.6-1.src.rpm

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





