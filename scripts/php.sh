
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/php/php.spec $RPM_DIR/SPECS/php.spec
cp ../packages/php/php.ini $RPM_DIR/SOURCES/php.ini
cp ../packages/php/php-cli.ini $RPM_DIR/SOURCES/php-cli.ini
cp ../packages/php/php-fpm.conf $RPM_DIR/SOURCES/php-fpm.conf
cp ../zips/apcu/apcu-4.0.6.tgz $RPM_DIR/SOURCES/apcu-4.0.6.tgz
cp ../zips/yaml/yaml-1.1.1.tgz $RPM_DIR/SOURCES/yaml-1.1.1.tgz
cp ../zips/php/php-5.6.7.tar.gz $RPM_DIR/SOURCES/php-5.6.7.tar.gz


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





