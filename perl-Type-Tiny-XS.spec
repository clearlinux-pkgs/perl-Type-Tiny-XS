#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Type-Tiny-XS
Version  : 0.025
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-XS-0.025.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-XS-0.025.tar.gz
Summary  : "provides an XS boost for some of Type::Tiny's built-in type constraints"
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Type-Tiny-XS-license = %{version}-%{release}
Requires: perl-Type-Tiny-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Type::Tiny::XS - provides an XS boost for some of Type::Tiny's built-in
type constraints

%package dev
Summary: dev components for the perl-Type-Tiny-XS package.
Group: Development
Provides: perl-Type-Tiny-XS-devel = %{version}-%{release}
Requires: perl-Type-Tiny-XS = %{version}-%{release}

%description dev
dev components for the perl-Type-Tiny-XS package.


%package license
Summary: license components for the perl-Type-Tiny-XS package.
Group: Default

%description license
license components for the perl-Type-Tiny-XS package.


%package perl
Summary: perl components for the perl-Type-Tiny-XS package.
Group: Default
Requires: perl-Type-Tiny-XS = %{version}-%{release}

%description perl
perl components for the perl-Type-Tiny-XS package.


%prep
%setup -q -n Type-Tiny-XS-0.025
cd %{_builddir}/Type-Tiny-XS-0.025

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Type-Tiny-XS
cp %{_builddir}/Type-Tiny-XS-%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/perl-Type-Tiny-XS/74050aca9901d9808976cf1c0b2ef7f06f35ca1a || :
cp %{_builddir}/Type-Tiny-XS-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Type-Tiny-XS/b288b1bcff3334631a50e17207149b915027c134 || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Type::Tiny::XS.3
/usr/share/man/man3/Type::Tiny::XS::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Type-Tiny-XS/74050aca9901d9808976cf1c0b2ef7f06f35ca1a
/usr/share/package-licenses/perl-Type-Tiny-XS/b288b1bcff3334631a50e17207149b915027c134

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
