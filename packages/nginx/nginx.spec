
%define nginx_home %{_localstatedir}/cache/nginx
%define nginx_user nginx
%define nginx_group nginx

%define date %(date +%%Y_%%m_%%d) 
                            
%define module_list --add-module=nginx-upstream-fair-master --with-http_ssl_module --with-http_realip_module --with-http_sub_module --with-http_flv_module --with-http_mp4_module --with-http_gzip_static_module --with-http_secure_link_module --with-http_stub_status_module --with-file-aio --with-ipv6 


Summary: high performance web server
Name: nginx-basereality-%{date}
Version: 1.7.4
Release: 1%{?dist}.ngx
Vendor: nginx inc.
URL: http://nginx.org/

Source0: http://nginx.org/download/nginx-%{version}.tar.gz
Source1: nginx.logrotate
Source2: nginx.init
Source3: nginx.sysconf
Source4: nginx.conf
Source5: nginx-upstream-fair-master.tgz
Source6: mime.types


License: 2-clause BSD-like license
%if 0%{?suse_version}
Group: Productivity/Networking/Web/Servers
%else
Group: System Environment/Daemons
%endif

BuildRoot: %{_tmppath}/nginx-%{version}-%{release}-root
BuildRequires: zlib-devel
BuildRequires: pcre-devel
BuildRequires: perl
%if 0%{?suse_version}
BuildRequires: libopenssl-devel
Requires(pre): pwdutils
%else
BuildRequires: openssl-devel
Requires: initscripts >= 8.36
Requires(pre): shadow-utils
Requires(post): chkconfig
%endif
Provides: webserver

%description
nginx [engine x] is a HTTP and reverse proxy server, as well as
a mail proxy server

%package debug
Summary: debug version of nginx
Group: System Environment/Daemons
Requires: nginx
%description debug
not stripped version of nginx build with the debugging log support

%prep
# Prep extracts the source from the zip files into the build directory. There
# are built in macros for this

%setup -q -n nginx-%{version}
%setup -T -D -a 5 -n nginx-%{version}

# -T switch disables the automatic unpacking of the archive. -D switch tells the %setup 
# command not to delete the directory before unpacking and -a switch tells the %setup 
# command to unpack only the source directive of the given number after changing directory.
# n set the dest folder



%build
# Build the project.

echo %{module_list}

./configure \
        --prefix=%{_sysconfdir}/nginx/ \
        --sbin-path=%{_sbindir}/nginx \
        --conf-path=%{_sysconfdir}/nginx/nginx.conf \
        --error-log-path=%{_localstatedir}/log/nginx/error.log \
        --http-log-path=%{_localstatedir}/log/nginx/access.log \
        --pid-path=%{_localstatedir}/run/nginx.pid \
        --lock-path=%{_localstatedir}/run/nginx.lock \
        --http-client-body-temp-path=%{_localstatedir}/cache/nginx/client_temp \
        --http-proxy-temp-path=%{_localstatedir}/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=%{_localstatedir}/cache/nginx/fastcgi_temp \
        --http-uwsgi-temp-path=%{_localstatedir}/cache/nginx/uwsgi_temp \
        --http-scgi-temp-path=%{_localstatedir}/cache/nginx/scgi_temp \
        --user=%{nginx_user} \
        --group=%{nginx_group} \
         %{module_list} \
        --with-debug \
        --with-cc-opt="%{optflags} $(pcre-config --cflags)" \
        $*
        
make %{?_smp_mflags}
%{__mv} %{_builddir}/nginx-%{version}/objs/nginx \
        %{_builddir}/nginx-%{version}/objs/nginx.debug
./configure \
        --prefix=%{_sysconfdir}/nginx/ \
        --sbin-path=%{_sbindir}/nginx \
        --conf-path=%{_sysconfdir}/nginx/nginx.conf \
        --error-log-path=%{_localstatedir}/log/nginx/error.log \
        --http-log-path=%{_localstatedir}/log/nginx/access.log \
        --pid-path=%{_localstatedir}/run/nginx.pid \
        --lock-path=%{_localstatedir}/run/nginx.lock \
        --http-client-body-temp-path=%{_localstatedir}/cache/nginx/client_temp \
        --http-proxy-temp-path=%{_localstatedir}/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=%{_localstatedir}/cache/nginx/fastcgi_temp \
        --http-uwsgi-temp-path=%{_localstatedir}/cache/nginx/uwsgi_temp \
        --http-scgi-temp-path=%{_localstatedir}/cache/nginx/scgi_temp \
        --user=%{nginx_user} \
        --group=%{nginx_group} \
        %{module_list} \
        --with-cc-opt="%{optflags} $(pcre-config --cflags)" \
        $*
make %{?_smp_mflags}

%install
# Install copies the files from the BUILD directory to the BUILDROOT 


# remove default stripping
%define __spec_install_port /usr/lib/rpm/brp-compress

%{__rm} -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/nginx
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/nginx/html $RPM_BUILD_ROOT%{_datadir}/nginx/

%{__rm} -f $RPM_BUILD_ROOT%{_sysconfdir}/nginx/*.default
%{__rm} -f $RPM_BUILD_ROOT%{_sysconfdir}/nginx/fastcgi.conf

%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/log/nginx
%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/run/nginx
%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/cache/nginx

%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/nginx/sites-enabled
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/nginx/sites-available
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/nginx/conf.d
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/nginx/nginx.conf
%{__install} -m 644 -p %{SOURCE4} \
   $RPM_BUILD_ROOT%{_sysconfdir}/nginx/nginx.conf
%{__install} -m 644 -p %{SOURCE6} \
      $RPM_BUILD_ROOT%{_sysconfdir}/nginx/mime.types

%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__install} -m 644 -p %{SOURCE3} \
   $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/nginx


# install SYSV init stuff
%{__mkdir} -p $RPM_BUILD_ROOT%{_initrddir}



%{__install} -m755 %{SOURCE2} \
   $RPM_BUILD_ROOT%{_initrddir}/nginx
#%endif


# install log rotation stuff
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
%{__install} -m 644 -p %{SOURCE1} \
   $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/nginx
%{__install} -m755 %{_builddir}/nginx-%{version}/objs/nginx.debug \
   $RPM_BUILD_ROOT%{_sbindir}/nginx.debug
%{__strip} $RPM_BUILD_ROOT%{_sbindir}/nginx

%clean
%{__rm} -rf $RPM_BUILD_ROOT





%files
%defattr(-,root,root)

%{_sbindir}/nginx

%dir %{_sysconfdir}/nginx
%dir %{_sysconfdir}/nginx/conf.d
%dir %{_sysconfdir}/nginx/sites-enabled
%dir %{_sysconfdir}/nginx/sites-available

%config(noreplace) %{_sysconfdir}/nginx/nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/mime.types
%config(noreplace) %{_sysconfdir}/nginx/fastcgi_params
%config(noreplace) %{_sysconfdir}/nginx/scgi_params
%config(noreplace) %{_sysconfdir}/nginx/uwsgi_params
%config(noreplace) %{_sysconfdir}/nginx/koi-utf
%config(noreplace) %{_sysconfdir}/nginx/koi-win
%config(noreplace) %{_sysconfdir}/nginx/win-utf

%config(noreplace) %{_sysconfdir}/logrotate.d/nginx
%config(noreplace) %{_sysconfdir}/sysconfig/nginx
%{_initrddir}/nginx

%dir %{_datadir}/nginx
%dir %{_datadir}/nginx/html
%{_datadir}/nginx/html/*

%attr(0755,root,root) %dir %{_localstatedir}/cache/nginx
%attr(0755,root,root) %dir %{_localstatedir}/log/nginx

%files debug
%{_sbindir}/nginx.debug



%pre
# Add the "nginx" user
getent group %{nginx_group} >/dev/null || groupadd -r %{nginx_group}
getent passwd %{nginx_user} >/dev/null || \
    useradd -r -g %{nginx_group} -s /sbin/nologin \
    -d %{nginx_home} -c "nginx user"  %{nginx_user}
usermod -a -G www-data nginx
exit 0

%post
# Register the nginx service
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add nginx
    /sbin/chkconfig --level 2345 nginx on
    # print site info
    cat <<BANNER
----------------------------------------------------------------------

Thanks for using NGINX!

Custom build for basereality

----------------------------------------------------------------------
BANNER
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service nginx stop > /dev/null 2>&1
    /sbin/chkconfig --del nginx
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service nginx upgrade &>/dev/null || :
fi









%changelog
* Thu Mar 15 2012 Sergey Budnevitch <sb@nginx.com>
- 1.0.14
- OpenSUSE init script and SuSE specific changes to spec file added

* Mon Mar  5 2012 Sergey Budnevitch <sb@nginx.com>
- 1.0.13

* Mon Feb  6 2012 Sergey Budnevitch <sb@nginx.com>
- 1.0.12
- banner added to install script

* Thu Dec 15 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.11
- init script enhancements (thanks to Gena Makhomed)
- one second sleep during upgrade replaced with 0.1 sec usleep

* Tue Nov 15 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.10

* Tue Nov  1 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.9
- nginx-debug package added

* Tue Oct 11 2011 Sergey Budnevitch <sb@nginx.com>
- spec file cleanup (thanks to Yury V. Zaytsev)
- log dir permitions fixed
- logrotate creates new logfiles with nginx owner
- "upgrade" argument to init-script added (based on fedora one)

* Sat Oct  1 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.8
- built with mp4 module

* Fri Sep 30 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.7

* Tue Aug 30 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.6
- replace "conf.d/*" config include with "conf.d/*.conf" in default nginx.conf

* Tue Aug 10 2011 Sergey Budnevitch
- Initial release
