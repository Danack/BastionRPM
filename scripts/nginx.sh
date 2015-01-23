#https://stereochro.me/ideas/rpm-for-the-unwilling

startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/nginx/nginx.spec $RPM_DIR/SPECS/nginx.spec
cp ../packages/nginx/* $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/nginx.spec

. ${startDir}/copyAndRepo.sh






