#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Intersperse
Summary:	List::Intersperse - intersperse / unsort / disperse a list
Summary(pl):	Modu³ Perla List::Intersperse - mieszaj±cy / rozsortowuj±cy / rozpraszaj±cy listy
Name:		perl-List-Intersperse
Version:	1.00
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List::Intersperse module provides functions that evenly distribute
elements of a list. Elements that are considered equal are spaced as
far apart from each other as possible.

%description -l pl
Modu³ List::Intersperse udostêpnia funkcje, które równomiernie
rozpraszaj± elementy listy. Elementy uwa¿ane za równe s± umieszczane
mo¿liwie daleko od siebie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
