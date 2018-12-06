#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Type-Tiny-XS
Version  : 0.014
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-XS-0.014.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-XS-0.014.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtype-tiny-xs-perl/libtype-tiny-xs-perl_0.012-2.debian.tar.xz
Summary  : "provides an XS boost for some of Type::Tiny's built-in type constraints"
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Type-Tiny-XS-lib = %{version}-%{release}
Requires: perl-Type-Tiny-XS-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Type::Tiny::XS - provides an XS boost for some of Type::Tiny's built-in
type constraints

%package dev
Summary: dev components for the perl-Type-Tiny-XS package.
Group: Development
Requires: perl-Type-Tiny-XS-lib = %{version}-%{release}
Provides: perl-Type-Tiny-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-Type-Tiny-XS package.


%package lib
Summary: lib components for the perl-Type-Tiny-XS package.
Group: Libraries
Requires: perl-Type-Tiny-XS-license = %{version}-%{release}

%description lib
lib components for the perl-Type-Tiny-XS package.


%package license
Summary: license components for the perl-Type-Tiny-XS package.
Group: Default

%description license
license components for the perl-Type-Tiny-XS package.


%prep
%setup -q -n Type-Tiny-XS-0.014
cd ..
%setup -q -T -D -n Type-Tiny-XS-0.014 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Type-Tiny-XS-0.014/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Type-Tiny-XS
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/perl-Type-Tiny-XS/COPYRIGHT
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Type-Tiny-XS/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Type-Tiny-XS/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Type/Tiny/XS.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Type/Tiny/XS/Util.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Type::Tiny::XS.3
/usr/share/man/man3/Type::Tiny::XS::Util.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Type/Tiny/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Type-Tiny-XS/COPYRIGHT
/usr/share/package-licenses/perl-Type-Tiny-XS/LICENSE
/usr/share/package-licenses/perl-Type-Tiny-XS/deblicense_copyright
