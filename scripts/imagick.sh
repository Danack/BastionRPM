#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../spec/imagick.spec $RPM_DIR/SPECS/imagick.spec

cp ../packages/imagick-master.tar.gz $RPM_DIR/SOURCES/imagick-master.tar.gz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/imagick.spec

cp RPMS/x86_64/imagick-master-1.x86_64.rpm $startDir/../repo/RPMS/x86_64/imagick-master-1.x86_64.rpm

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





