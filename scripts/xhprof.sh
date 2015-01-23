#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/xhprof/xhprof.spec $RPM_DIR/SPECS/xhprof.spec
cp ../packages/xhprof/xhprof.ini $RPM_DIR/SOURCES/xhprof.ini

cp ../zips/xhprof-0.9.4.tgz $RPM_DIR/SOURCES/xhprof-0.9.4.tgz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/xhprof.spec

. ${startDir}/copyAndRepo.sh

#cp RPMS/x86_64/*  $startDir/../repo/RPMS/x86_64/
#cp SRPMS/*  $startDir/../repo/SRPMS/
#
#createrepo $startDir/../repo/SRPMS
#createrepo $startDir/../repo/RPMS/x86_64
