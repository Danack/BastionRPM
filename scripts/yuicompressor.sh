
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/yuicompressor/yuicompressor.spec $RPM_DIR/SPECS/yuicompressor.spec
cp ../packages/yuicompressor/* $RPM_DIR/SOURCES/


cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/yuicompressor.spec

cp RPMS/x86_64/* $startDir/../repo/RPMS/x86_64/
cp SRPMS/*  $startDir/../repo/SRPMS/

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





