
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/php/php7.spec $RPM_DIR/SPECS/php7.spec
cp ../packages/php/* $RPM_DIR/SOURCES/
cp ../zips/php-src-master.tar.gz $RPM_DIR/SOURCES/php-src-master.tar.gz

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/php7.spec

rc=$?
if [[ $rc != 0 ]] ; then
    echo "Failed to build rpm PHPCUSTOM"
    exit $rc
fi


. ${startDir}/copyAndRepo.sh






