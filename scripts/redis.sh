
startDir=$(pwd)
. ./setupDirectory.sh

cp ../spec/redis.spec $RPM_DIR/SPECS/redis.spec
cp ../ini/redis/* $RPM_DIR/SOURCES/

cp ../packages/redis-2.8.13.tar.gz $RPM_DIR/SOURCES/redis-2.8.13.tar.gz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/redis.spec

cp RPMS/x86_64/* $startDir/../repo/RPMS/x86_64/
cp SRPMS/*  $startDir/../repo/SRPMS/

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





