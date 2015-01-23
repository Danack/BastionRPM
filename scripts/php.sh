
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/php/php.spec $RPM_DIR/SPECS/php.spec
cp ../packages/php/* $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/php.spec

rc=$?
if [[ $rc != 0 ]] ; then
    echo "Failed to build rpm PHPCUSTOM"
    exit $rc
fi


. ${startDir}/copyAndRepo.sh

#cp RPMS/x86_64/*.rpm $startDir/../repo/RPMS/x86_64/
#createrepo $startDir/../repo/SRPMS
#createrepo $startDir/../repo/RPMS/x86_64





