#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	List
%define		pnam	Intersperse
%include	/usr/lib/rpm/macros.perl
Summary:	List::Intersperse Perl module - intersperse / unsort / disperse a list
Summary(pl.UTF-8):	Moduł Perla List::Intersperse - mieszający / rozsortowujący / rozpraszający listy
Name:		perl-List-Intersperse
Version:	1.00
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2731d6b6f199a242f3fd0bf587cc2b1e
URL:		http://search.cpan.org/dist/List-Intersperse/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List::Intersperse module provides functions that evenly distribute
elements of a list. Elements that are considered equal are spaced as
far apart from each other as possible.

%description -l pl.UTF-8
Moduł List::Intersperse udostępnia funkcje, które równomiernie
rozpraszają elementy listy. Elementy uważane za równe są umieszczane
możliwie daleko od siebie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
