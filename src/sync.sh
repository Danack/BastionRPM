
cd ../repo

rpm --resign RPMS/noarch/*.rpm
rpm --resign RPMS/x86_64/*.rpm

createrepo RPMS/noarch
createrepo RPMS/x86_64

touch ./sign.time

cd ../src

php makeHTML.php

php -d allow_url_fopen=1 sync.php

