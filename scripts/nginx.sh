#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/nginx/nginx.spec $RPM_DIR/SPECS/nginx.spec
cp ../packages/nginx/* $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/nginx.spec

cp $RPM_DIR/SRPMS/*   $startDir/../repo/SRPMS/
cp $RPM_DIR/RPMS/x86_64/*  $startDir/../repo/RPMS/x86_64/






