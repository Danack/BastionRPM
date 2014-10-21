#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/imagick/imagick.spec $RPM_DIR/SPECS/imagick.spec
cp ../packages/imagick/* $RPM_DIR/SOURCES/


cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/imagick.spec

cp RPMS/x86_64/* $startDir/../repo/RPMS/x86_64/

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





