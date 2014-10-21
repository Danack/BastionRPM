startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/mcrypt/mcrypt.spec $RPM_DIR/SPECS/mcrypt.spec
cp ../packages/mcrypt/* $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/mcrypt.spec

cp $RPM_DIR/SRPMS/*   $startDir/../repo/SRPMS/
cp $RPM_DIR/RPMS/x86_64/*  $startDir/../repo/RPMS/x86_64/


