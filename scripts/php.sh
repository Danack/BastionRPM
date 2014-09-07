
startDir=$(pwd)
. ./setupDirectory.sh

cp ../spec/php.spec $RPM_DIR/SPECS/php.spec
cp ../packages/php-5.6.0RC3.tar.gz $RPM_DIR/SOURCES/php-5.6.0RC3.tar.gz
cp ../packages/apcu-4.0.6.tgz $RPM_DIR/SOURCES/apcu-4.0.6.tgz
cp ../packages/yaml-1.1.1.tgz $RPM_DIR/SOURCES/yaml-1.1.1.tgz
cp ../ini/php/* $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/php.spec

rc=$?
if [[ $rc != 0 ]] ; then
    echo "Failed to build rpm PHPCUSTOM"
    exit $rc
fi

cp RPMS/x86_64/*.rpm $startDir/../repo/RPMS/x86_64/

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





