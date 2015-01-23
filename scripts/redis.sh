
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/redis/redis.spec $RPM_DIR/SPECS/redis.spec
cp ../packages/redis/* $RPM_DIR/SOURCES/


cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/redis.spec

. ${startDir}/copyAndRepo.sh


#cp RPMS/x86_64/* $startDir/../repo/RPMS/x86_64/
#cp SRPMS/*  $startDir/../repo/SRPMS/

#createrepo $startDir/../repo/SRPMS
#createrepo $startDir/../repo/RPMS/x86_64





