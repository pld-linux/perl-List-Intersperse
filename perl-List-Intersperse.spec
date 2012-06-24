#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Intersperse
Summary:	List::Intersperse - intersperse / unsort / disperse a list
Summary(pl):	Modu� Perla List::Intersperse - mieszaj�cy / rozsortowuj�cy / rozpraszaj�cy listy
Name:		perl-List-Intersperse
Version:	1.00
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2731d6b6f199a242f3fd0bf587cc2b1e
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List::Intersperse module provides functions that evenly distribute
elements of a list. Elements that are considered equal are spaced as
far apart from each other as possible.

%description -l pl
Modu� List::Intersperse udost�pnia funkcje, kt�re r�wnomiernie
rozpraszaj� elementy listy. Elementy uwa�ane za r�wne s� umieszczane
mo�liwie daleko od siebie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
