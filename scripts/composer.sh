
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/composer/composer.spec $RPM_DIR/SPECS/composer.spec
cp ../packages/composer/composer-master.tar.gz $RPM_DIR/SOURCES/composer-master.tar.gz
cp ../packages/composer/composer.phar $RPM_DIR/SOURCES/composer.phar

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/composer.spec

. ${startDir}/copyAndRepo.sh





